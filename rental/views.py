from django.shortcuts import render, get_object_or_404
from .models import Imovel
from django.http import Http404
from django.db.models import Q
from utils.pagination import make_pagination
import os

PER_PAGE = os.environ.get('PER_PAGE', 6)

def home(request):
    imoveis = Imovel.objects.filter(
        is_published=True
    ).order_by('-category_id')
    page_obj, pagination_range = make_pagination(request, imoveis, PER_PAGE)
    return render(request, 'rental/pages/home.html',
                  context={
                      'imoveis': page_obj,
                      'pagination_range': pagination_range,
                  })


def imovel(request, category_id):
    imovel = get_object_or_404(Imovel, pk=category_id, is_published=True,)
    return render(request, 'rental/pages/imovel.html', context={
        'imovel': imovel,
        'title': f'{imovel.category.name} - Imobiliaria Girassol ',
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()
    imoveis = Imovel.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(city__icontains=search_term),
        ), is_published=True
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, imoveis, PER_PAGE)
    return render(request, 'rental/pages/search.html', {
        'page_title': f'Search for "{search_term}" | Imóveis',
        'search_term': search_term,
        'imoveis': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })