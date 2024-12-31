from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def gallery(request):
    return render(request, "gallery.html")
