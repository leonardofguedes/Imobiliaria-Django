from django.shortcuts import render, get_object_or_404
from .models import Imovel, Category

def home(request):
    imoveis = Imovel.objects.all()
    return render(request, 'rental/pages/home.html',
                  context={'imoveis': imoveis,}
                  )


def imovel(request, category_id):
    """
    imovel = Imovel.objects.filter(
        pk = category_id
    ).order_by('-id').first()
    return render(request, 'rental/pages/imovel.html', context={
        'imovel': imovel,
        'is_detail_page': True,
    })
    """
    imovel = get_object_or_404(Imovel, pk=category_id, is_published=True,)
    return render(request, 'rental/pages/imovel.html', context={
        'imovel': imovel,
        'is_detail_page': True,
    })