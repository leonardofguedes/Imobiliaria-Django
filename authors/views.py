from django.shortcuts import render
from .forms import RegisterForm


def register_view(request):
    if request.Post:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'authors/pages/register_view.html',
                  {'form': form,
                   })
