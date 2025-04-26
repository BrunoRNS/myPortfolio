from django.shortcuts import render

# Home Page
def home(request):

    stylesheet: dict[str: list[str]] = {
        'css_files': ["home/home/col_img.css", "home/home/col_portfolio.css"],
        'scss_files': ["global/global.scss", "home/home/page.scss"],
        'template_name': ["home"],
    }
    
    return render(request, 'home/home/index.html', context=stylesheet)