from django.shortcuts import render

# Info Page
def info(request):
    return render(request, 'info/index.html')