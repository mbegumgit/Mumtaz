from django.shortcuts import render
from .models import BeeWord, Score

# Create your views here.

def index(request):
    return render(request, "Bee/index.html", {
        "Words": BeeWord.objects.all()
    })