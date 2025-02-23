from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def terms(request):
    return render(request, 'terms/index.html')

def contact(request):
    return render(request, 'contact/index.html')