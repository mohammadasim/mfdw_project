from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> The Meandco HomePage</h1>")
