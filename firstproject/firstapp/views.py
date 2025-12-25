from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import ReservationForm


# Create your views here.
def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")


class HelloEthiopia(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Hello Ethiopia")


def home(request: HttpRequest) -> HttpResponse:
    form = ReservationForm()

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")

    return render(request, "index.html", {"form": form})