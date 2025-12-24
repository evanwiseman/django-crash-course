from django.http import HttpRequest, HttpResponse
from django.views import View


# Create your views here.
def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")


class HelloEthiopia(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Hello Ethiopia")
