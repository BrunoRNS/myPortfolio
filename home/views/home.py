""" 
Project: server - My Portfolio
Author: Bruno Rian Nunes de Souza
License: GNU General Public License v3.0

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License, version 3, as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

from django_ratelimit.decorators import ratelimit

from django.shortcuts import render
from django.core.cache import cache

from typing import Dict, List

from ..forms.forms import ContactForm

from django import forms

@ratelimit(key='ip', rate='3/s', method='GET', block=True)
def home(request):
    """
    The home view is responsible for rendering the home page. It will pass the
    context to the template which will render the page.

    The context is a dictionary with the following keys:

    - user: A dictionary containing the user's informations.
    - skills: A list of dictionaries containing the user's skills.
    - projects: A list of dictionaries containing the user's projects.
    - view_all_url: A string with the url to view all projects.

    The user dictionary has the following keys:

    - name: A string with the user's name.
    - title: A string with the user's title.
    - bio: A string with the user's bio.
    - about: A string with the user's about.
    - social_links: A dictionary with the user's social links.

    The skills dictionary has the following keys:

    - name: A string with the skill's name.
    - image: A string with the skill's image.

    The projects dictionary has the following keys:

    - title: A string with the project's title.
    - description: A string with the project's description.
    - github_url: A string with the project's github url.
    - demo_url: A string with the project's demo url.
    - languages: A list of strings with the project's languages.

    The view_all_url is a string with the url to view all projects.
    """
    
    context: Dict[
        str,    str |
                forms.Form |
                Dict[str, str | Dict[str, str]] | 
                List[Dict[str, str]] | 
                List[Dict[str, str | List[str]]]
    ]
    """
    EXAMPLE CONTEXT:
    context = {
    'user': {
        'name': "Bruno RNS",
        'title': "Web Developer",
        'bio': "There wasn't a bird in the sky, but that was not what caught her attention...",
        'about': "My name's Bruno. I'm a web designer and developer based in São Paulo, BR. During the day I work as a lead developer...",
        'social_links': {
            'discord': "https://www.discord.com/",
            'github': "https://github.com/",
            'email': "https://gmail.com/",
        }
    },
    
    'skills': [
        {'name': 'HTML', 'image': 'html.6a342d61.svg'},
        {'name': 'Fastify', 'image': 'fastify.1b930a41.svg'},
        {'name': 'Blender', 'image': 'blender.b96901d1.svg'},
        {'name': 'Figma', 'image': 'figma.1cd44608.svg'},
        {'name': 'Javascript', 'image': 'javascript.e9360603.svg'},
        {'name': 'CSS', 'image': 'css.43b6f4bd.svg'},
        {'name': 'React', 'image': 'react.2b6a0717.svg'},
        {'name': 'Django', 'image': 'django.d51a8aa4.svg'},
        ...
    ],
    
    or with fontAwesomeClass:
    
    'skills': [
        {'name': 'HTML', 'fontAwesomeClass': 'fab fa-html5'},
        {'name': 'CSS', 'fontAwesomeClass': 'fab fa-css3-alt'},
        ...
    ],    
    
    'projects': [
            {
                'title': 'Employee Management',
                'description': 'This project aims to build an employee management system...',
                'github_url': 'https://github.com/user/repo1',
                'demo_url': 'https://demo.user/repo1',
                'languages': ['React', 'CSS', 'Material Ui'],
            },
            {
                'title': 'Railway Tracking',
                'description': 'This project is a railway tracking system...',
                'github_url': 'https://github.com/user/repo2',
                'demo_url': 'https://demo.user/repo2',
                'languages': ['Django', 'Tailwind CSS'],
            },
            {
                'title': 'Weather App',
                'description': 'Weather forecast systems and applications...',
                'github_url': 'https://github.com/user/repo3',
                'demo_url': 'https://demo.user/repo3',
                'languages': ['Django', 'CSS', 'Material Ui'],
            }
        ],

        'view_all_url': '/projects',
        
    }
    """
    context = {
        'user': {
            'name': "Bruno RNS",
            'title': "Web Developer",
            'bio': "There wasn't a bird in the sky, but that was not what caught her attention...",
            'about': "My name's Bruno. I'm a web designer and developer based in São Paulo, BR. During the day I work as a lead developer...",
            'social_links': {
                'discord': "https://www.discord.com/",
                'github': "https://github.com/BrunoRNS",
            }
        },
        'skills': [
                {"name": "Django", "image": "https://img.icons8.com/external-tal-revivo-filled-tal-revivo/240/external-django-a-high-level-python-web-framework-that-encourages-rapid-development-logo-filled-tal-revivo.png"},
                {"name": "HTML", "image": "https://img.icons8.com/plasticine/100/html-5.png"},
                {"name": "CSS", "image": "https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/240/external-cascading-style-sheets-language-used-for-describing-the-presentation-of-a-document-logo-shadow-tal-revivo.png"},
                {"name": "JS", "image": "https://img.icons8.com/fluency/48/javascript.png"},
                {"name": "Python", "image": "https://img.icons8.com/plasticine/400/python.png"},
                {"name": "Flask", "image": "/static/media/Flask.png"},
                {"name": "Java", "image": "https://img.icons8.com/3d-fluency/375/java-coffee-cup-logo.png"},
                {"name": "Spring Boot", "image": "https://img.icons8.com/color/480/spring-logo.png"},
                {"name": "SNES", "image": "/static/media/snes.png"},
                {"name": "C", "image": "https://img.icons8.com/plasticine/400/c-programming.png"},
                {"name": "Game Development", "image": "https://img.icons8.com/external-flaticons-lineal-color-flat-icons/100/external-gaming-addiction-flaticons-lineal-color-flat-icons.png"},
                {"name": "Linux", "image": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/100/external-linux-a-family-of-open-source-unix-like-operating-systems-based-on-the-linux-kernel-logo-color-tal-revivo.png"},
                {"name": "Windows", "image": "https://img.icons8.com/office/480/windows-10.png"},
                {"name": "Bash/Shell", "image": "https://img.icons8.com/fluency/240/bash.png"},
                {"name": "Debian", "image": "https://www.debian.org/logos/openlogo-nd-100.png"},
                {"name": "Ubuntu", "image": "/static/media/ubuntu.png"},
                {"name": "Julia", "image": "/static/media/julia.png"},
                {"name": "Jupyter Notebooks", "image": "https://img.icons8.com/fluency/240/jupyter.png"},
        ],
        'projects': [],
        'view_all_url': 'https://github.com/BrunoRNS?tab=repositories',
    }
    
    cache_key = "github_projects_brunorns"
    projects = cache.get(cache_key)
    
    if not projects:
        
        from ..services.getGithubData import GetGithubData
        getGithubData = GetGithubData()
        
        projects = getGithubData.get_repos_with_more_stars(3)
        
        cache.set(cache_key, projects, timeout=86400)
    
    context['projects'] = projects
    
    context['form'] = ContactForm()
    
    return render(request, 'index.html', context)
