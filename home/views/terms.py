from django.shortcuts import render

# Terms and Agreement Page
def terms(request):
    return render(request, 'home/terms/index.html')