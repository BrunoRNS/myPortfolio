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

from django.conf import settings
from github import Github, Auth

from github.Repository import Repository

from sortedcontainers import SortedDict as TreeMap

from typing import Dict, List

class GetGithubData:
    
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the GetGithubData class with authentication token.

        This constructor sets up the authentication using a GitHub token
        from the Django settings and establishes a GitHub API access
        instance. It also retrieves the authenticated user's information.
        Parameters:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        
        self.auth: Auth.Token = Auth.Token(settings.GITHUB_TOKEN)

        self.access: Github = Github(auth=self.auth)
        self.user = self.access.get_user()

    def get_repos_with_more_stars(self, count: int) -> List[Dict[str, str | List[str]]]:
        """
        Retrieves a list of the authenticated user's repositories sorted by the number of stars.
        The returned list will contain dictionaries with the following keys:
        - title: The title of the repository.
        - description: The description of the repository.
        - github_url: The URL of the repository on GitHub.
        - demo_url: The URL of the deployed application, or the repository URL if none is available.
        - languages: A list of languages used in the repository, sorted by the percentage of code written in each language.
        This function takes an integer parameter, which is the number of repositories to return.
        The function will return at most 'count' repositories.
        """
        
        all_repos: List[Repository] = [repo for repo in self.user.get_repos()]
        
        repo_and_stars: Dict[int, Repository] = TreeMap()
        
        repos_to_return: List[Dict[str, str | List[str]]] = []
        """
        ['title': repo['name'],
        'description': repo['description'],
        'github_url': repo['html_url'],
        'demo_url': repo['homepage'] or repo['html_url'],
        'languages': repo['get_languages'].keys()]
        """
        
        for repo in all_repos:
            repo_and_stars[repo.stargazers_count] = repo

        for _, repo in reversed(repo_and_stars.items()):
            
            repo: Repository
        
            if count == 0:
                break
            
            languages = repo.get_languages()
            
            total_bytes = sum(languages.values())
            
            repos_to_return.append({
                'title': repo.name,
                'description': repo.description,
                'github_url': repo.html_url,
                'demo_url': repo.homepage or repo.html_url,
                'languages':
                    [
                        lang for lang, bytes in languages.items() 
                        if ((bytes / total_bytes) * 100) > 2
                    ],

            })
            
            count -= 1
        
        return repos_to_return
