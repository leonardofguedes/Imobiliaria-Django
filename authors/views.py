from django.http import Http404
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


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

    if form.is_valid():
        form.save()
        messages.success(request, 'Your user is created, please log in.')

        del(request.session['register_fomr_data'])

    return redirect('authors:register')