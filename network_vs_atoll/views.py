from django.shortcuts import render


def home(request):
    return render(request, 'network_vs_atoll/home.html')