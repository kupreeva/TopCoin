from django.shortcuts import render
from .models import Coin
# Create your views here.


def main_page(request):
    coins = Coin.objects.all()
    return render(request, 'coinlist/main_page.html', {'coins': coins})
