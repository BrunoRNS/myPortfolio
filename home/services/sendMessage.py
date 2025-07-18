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

class SendMessage:
    
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the SendMessage class with a notification token.

        This constructor sets up the authentication using a notification token
        from the Django settings and establishes a GitHub API access instance.
        It also retrieves the authenticated user's information.
    
        Parameters:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """

        self.auth: Auth.Token = Auth.Token(settings.NOTIFICATION_TOKEN)

        self.access: Github = Github(auth=self.auth)
        self.repo = self.access.get_repo("BrunoRNS/notifications")


    def send_message(self, author: str, title: str, message: str) -> None:
        """
        Creates an issue on the authenticated user's GitHub account with the given author, title and message.

        Parameters:
            author (str): The name of the author of the message.
            title (str): The title of the message.
            message (str): The message to be sent.

        Returns:
            None
        """
        
        if self.verify_spam(author):
            
            raise Exception("Spam detected")
        
        self.create_issue(title=f"{author}: {title}", body=message)
        
    def create_issue(self, title: str, body: str) -> None:
        """
        Creates an issue on the authenticated user's GitHub account.
        """
        
        self.repo.create_issue(title=title, body=body)
    
    def verify_spam(self, email) -> bool:
        """
        Verifies if the email is a spammer.
        
        To verify it we check the email, if the email send a message and I havent closed yet
        it will be refused;
        
        Parameters:
            email (str): The email to be verified. 
        """
        
        for title in self.repo.get_issues(state="open", sort="created", direction="desc"):
            
            if email in title.title:
                
                return True
        
        return False
        
        