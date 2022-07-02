from django.http import Http404
from django.shortcuts import render, redirect
from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(request):
    """Esse métododo view não carregará templates;
       Ela apenas lê dados, confere-os e manda os dados para o register_view
    """
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    return redirect('authors:register')