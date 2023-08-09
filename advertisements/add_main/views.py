from django.shortcuts import render


def index(request):
    context = {'advertisements': ''}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')
