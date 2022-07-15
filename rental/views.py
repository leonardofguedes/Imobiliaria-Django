from django.shortcuts import render, get_object_or_404
from .models import Imovel
from django.http import Http404
from django.db.models import Q
from utils.pagination import make_pagination
import os
from django.views.generic import ListView


PER_PAGE = int(os.environ.get('PER_PAGE', 6))

class ListViewBase(ListView):
    model = Imovel
    context_object_name = 'imoveis'
    ordering = ['-id']
    template_name = 'rental/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get('imoveis'),
            PER_PAGE
        )
        ctx.update(
            {'imoveis': page_obj,
             'pagination_range': pagination_range
             }
        )
        return ctx

class ListViewHome(ListViewBase):
    template_name = 'rental/pages/home.html'

class ListViewSearch(ListViewBase):
    template_name = 'rental/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('q', '')
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term) |
                Q(city__icontains=search_term) |
                Q(district__icontains=search_term),
            )
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q','')
        ctx.update({
            'page_title': f'Procure por "{search_term}" |',
            'search_term': search_term,
            'additional_url_query': f'&q={search_term}',
        })
        return ctx

def imovel(request, category_id):
    imovel = get_object_or_404(Imovel, pk=category_id, is_published=True,)
    return render(request, 'rental/pages/imovel.html', context={
        'imovel': imovel,
        'title': f'{imovel.title} - Imobiliaria Girassol ',
        'is_detail_page': True,
    })
