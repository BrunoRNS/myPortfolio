from django.shortcuts import render

# Home Page
def home(request):
    return render(request, 'home/index.html')

# Terms and Agreement Page
def terms(request):
    return render(request, 'terms/index.html')

# Contact Me Page
def contact(request):
    return render(request, 'contact/index.html')