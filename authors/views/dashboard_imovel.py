from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from authors.forms.imovel_form import AuthorImovelForm
from rental.models import Imovel


class Dashboard_Edit(View):
    def get_imovel(self, id=None):
        imovel = None

        if id is not None:
            imovel = Imovel.objects.filter(
                is_published=False,
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
            # Agora, o form é válido e eu posso tentar salvar
            imovel = form.save(commit=False)

            imovel.author = request.user
            imovel.is_published = False
            imovel.save()

            messages.success(request, 'Seu imóvel foi salvo com sucesso!')
            return redirect(reverse('authors:dashboard_imovel_edit', args=(imovel.id,))
                            )
        return self.render_imovel(form)