from django.http import HttpResponse

def home_page(request):
    print("my home page")
    return HttpResponse("<h1>this is home page<h1>")