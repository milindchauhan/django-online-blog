from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "blog/home.html")

def about(request):
    return HttpResponse("<h1>Blog About</h1>")
