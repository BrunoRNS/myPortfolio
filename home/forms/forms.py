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

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input jss28',
            'placeholder': 'John Doe',
            'id': 'Name'
        })
    )
    email = forms.EmailField(
        min_length=5,
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input jss28',
            'placeholder': 'John@doe.com',
            'id': 'Email'
        })
    )
    message = forms.CharField(
        min_length=10,
        max_length=2000,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-message jss29',
            'placeholder': 'Type your message....',
            'rows': 4,
            'id': 'Message'
        })
    )