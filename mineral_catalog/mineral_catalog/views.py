from django.shortcuts import render


def home(request):
    '''This is the webpages main homepage.'''
    return render(request, 'layout.html')
