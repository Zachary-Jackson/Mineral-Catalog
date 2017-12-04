from django.shortcuts import render

from minerals.models import Mineral


def home(request):
    '''This is the webpages main homepage.'''
    objects = Mineral.objects.all()
    return render(request, 'minerals/layout.html', {'minerals': objects})
