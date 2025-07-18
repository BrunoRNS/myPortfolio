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

from ..services.sendMessage import SendMessage

from ..forms.forms import ContactForm

from django.http import JsonResponse

import dns.resolver

import re

def has_mx_records(domain):
    """
    Checks if a domain has any MX records.

    :param domain: The domain to be checked.
    :return: True if the domain has any MX records, False otherwise.
    """
    
    try:
        
        mx_records = dns.resolver.resolve(domain, 'MX')
        return len(mx_records) > 0
    
    except:
        
        return False

# A constant regular expression to validate email addresses
EMAIL_REGEXP = r"^(?!(?:(?:\x22?\x5C[\x00-\x7E]\x22?)|(?:\x22?[^\x5C\x22]\x22?)){255,})(?!(?:(?:\x22?\x5C[\x00-\x7E]\x22?)|(?:\x22?[^\x5C\x22]\x22?)){65,}@)(?:(?:[\x21\x23-\x27\x2A\x2B\x2D\x2F-\x39\x3D\x3F\x5E-\x7E]+)|(?:\x22(?:[\x01-\x08\x0B\x0C\x0E-\x1F\x21\x23-\x5B\x5D-\x7F]|(?:\x5C[\x00-\x7F]))*\x22))(?:\.(?:(?:[\x21\x23-\x27\x2A\x2B\x2D\x2F-\x39\x3D\x3F\x5E-\x7E]+)|(?:\x22(?:[\x01-\x08\x0B\x0C\x0E-\x1F\x21\x23-\x5B\x5D-\x7F]|(?:\x5C[\x00-\x7F]))*\x22)))*@(?:(?:(?!.*[^.]{64,})(?:(?:(?:xn--)?[a-z0-9]+(?:-[a-z0-9]+)*\.){1,126}){1,}(?:(?:[a-z][a-z0-9]*)|(?:(?:xn--)[a-z0-9]+))(?:-[a-z0-9]+)*)|(?:\[(?:(?:IPv6:(?:(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){7})|(?:(?!(?:.*[a-f0-9][:\]]){7,})(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){0,5})?::(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){0,5})?)))|(?:(?:IPv6:(?:(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){5}:)|(?:(?!(?:.*[a-f0-9]:){5,})(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){0,3})?::(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){0,3}:)?)))?(?:(?:25[0-5])|(?:2[0-4][0-9])|(?:1[0-9]{2})|(?:[1-9]?[0-9]))(?:\.(?:(?:25[0-5])|(?:2[0-4][0-9])|(?:1[0-9]{2})|(?:[1-9]?[0-9]))){3}))\]))$"

@ratelimit(key='ip', rate='2/d', method='POST', block=True)
def send_message(request):
    """
    Handles a POST request to send a message to me.

    :param request: Request object from Django.
    :return: A JSON response with a success or error message.

    Success:
    {
        "success": true
    }

    Error:
    {
        "error": "A string describing the error"
    }

    Status codes:
    200 - Success
    400 - Invalid email or invalid formulary or SPAM
    405 - Method not allowed
    500 - Internal Server Error
    """
    
    try:
    
        if request.method == 'POST':
        
            form = ContactForm(request.POST)
        
            if form.is_valid():

                name: str = form.cleaned_data['name']
                email: str = form.cleaned_data['email']
                message: str = form.cleaned_data['message']
                
                if ( not (len(re.findall(EMAIL_REGEXP, email)) == 1)) or \
                   ( not (has_mx_records(email.split("@")[1]))):
                    
                    print("Invalid email, exiting...")
                    
                    return JsonResponse({'error': 'Invalid email'}, status=400)
                
                try:
                    
                    sender: SendMessage = SendMessage()
                    
                    sender.send_message(author=email, title=name, message=message)
                
                except Exception as e:
                    
                    if "SPAM" in e.__str__():
                    
                        return JsonResponse({'error': 'SPAM, refusing...'}, status=400)

                    else:
                        
                        return JsonResponse({'error': e.__str__()}, status=400)
            
                return JsonResponse({'success': True}, status=200)

            print(form.errors)
            
            return JsonResponse({'error': 'Invalid formulary'}, status=400)
    
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    except:
        
        return JsonResponse({'error': 'An Internal Server Error occurred'}, status=500)
