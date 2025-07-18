from django import forms

class ContactForm(forms.Form):
    """
    A form to send email to my contact.
    """
    
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input jss28',
            'placeholder': 'John Doe'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input jss28',
            'placeholder': 'John@doe.com'
        })
    )
    
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-message jss29',
            'placeholder': 'Type your message....',
            'rows': 4
        })
    )
