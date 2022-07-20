from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from authors.forms.imovel_form import AuthorImovelForm
from rental.models import Imovel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class Dashboard_Imovel(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)


    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get_imovel(self, id=None):
        imovel = None

        if id is not None:
            imovel = Imovel.objects.filter(
                author=self.request.user,
                pk=id,
            ).first()

            if not imovel:
                raise Http404()

        return imovel

    def render_imovel(self, form):
        return render(
            self.request,
            'authors/pages/dashboard_imovel.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):
        imovel = self.get_imovel(id)
        form = AuthorImovelForm(instance=imovel)
        return self.render_imovel(form)

    def post(self, request, id=None):
        imovel = self.get_imovel(id)
        form = AuthorImovelForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=imovel
        )

        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.author = request.user
            if imovel.author.is_staff:
                imovel.save()
                messages.success(request, 'Seu imóvel foi salvo com sucesso!')
                return redirect(reverse(
                    'authors:dashboard_imovel_edit', args=(imovel.id,)))
            if imovel.author.is_staff == False:
                imovel.is_published = False
                imovel.save()

                messages.success(request, 'Seu imóvel foi salvo com sucesso!')
                return redirect(reverse(
                    'authors:dashboard_imovel_edit', args=(imovel.id,)))

        return self.render_imovel(form)

@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class Dashboard_Delete(Dashboard_Imovel):
    def post(self, *args, **kwargs):
        imovel = self.get_imovel(self.request.POST.get('id'))
        imovel.delete()
        messages.success(self.request, 'Deleted Successfully')
        return redirect(reverse('authors:dashboard'))
