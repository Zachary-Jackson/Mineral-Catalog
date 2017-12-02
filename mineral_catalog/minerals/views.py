from django.shortcuts import get_object_or_404, render

from .models import Mineral


def detail(request, pk):
    '''This is the main detail page for a mineral.'''
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html', {'mineral':
                                                            mineral})


def detail_home(request):
    '''This is a detail page if no mineral is selected.'''
    return render(request, 'mineral_detail.html')
