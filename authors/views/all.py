from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from authors.forms.register_form import RegisterForm
from authors.forms.login import LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rental.models import Imovel
from authors.forms.imovel_form import AuthorImovelForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
        'form_action': reverse('authors:register_create'),
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
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Your user is created, please log in.')

        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create')
    })



def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')

    return redirect(reverse('authors:dashboard'))

@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        messages.error(request, 'Invalid logout request')
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Invalid logout user')
        return redirect(reverse('authors:login'))

    messages.success(request, 'Logged out successfully')
    logout(request)
    return redirect(reverse('authors:login'))

@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    imoveis = Imovel.objects.filter(
        is_published=False,
        author=request.user
    )
    return render(request, 'authors/pages/dashboard.html',
        context={'imoveis': imoveis,}
                  )


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_imovel_new(request):
    form = AuthorImovelForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        imovel: Imovel = form.save(commit=False)

        imovel.author = request.user
        imovel.is_published = False

        imovel.save()

        messages.success(request, 'Salvo com sucesso!')
        return redirect(
            reverse('authors:dashboard_imovel_edit', args=(imovel.id,))
        )

    return render(
        request,
        'authors/pages/dashboard_imovel.html',
        context={
            'form': form,
            'form_action': reverse('authors:dashboard_imovel_new')
        }
    )

@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_imovel_delete(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    id = POST.get('id')

    imovel = Imovel.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()

    if not imovel:
        raise Http404()

    imovel.delete()
    messages.success(request, 'Deleted successfully.')
    return redirect(reverse('authors:dashboard'))