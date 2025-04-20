from django.shortcuts import render

# Home Page
def home(request):

    stylesheet: dict[str: list[str]] = {
        'css_files': ["home/col_img.css", "home/col_portfolio.css"],
        'scss_files': ["global/global.scss", "home/page.scss", "home/col_dropbtn.scss"],
    }
    
    return render(request, 'home/index.html', stylesheet)