from django.shortcuts import render
from django.http import HttpResponse

from .models import Review


# Create your views here.

def index(request):
    reviews = Review.objects.order_by("-date")
    context = {
        "list_of_reviews": reviews
    }
    return render(request, "courses/index.html", context = context)