from django.shortcuts import render

# Home Page
def home(request):
    stylesheet: dict[str: list[str]] = {
        'css_files': ["home/col_img.css", "home/col_portfolio.css"],
        'scss_files': ["global/global.scss", "home/page.scss", "home/col_dropbtn.scss"],
    }
    return render(request, 'home/index.html', stylesheet)

# Terms and Agreement Page
def terms(request):
    return render(request, 'terms/index.html')

# Contact Me Page
def contact(request):
    return render(request, 'contact/index.html')