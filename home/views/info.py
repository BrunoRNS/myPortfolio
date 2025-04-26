from django.shortcuts import render

# Info Page
def info(request):
    return render(request, 'home/info/index.html')