from django import forms
from .models import Product
from django.contrib.auth.models import User 
from .models import Comment

#product form receive all in4 from product
class ProductForm(forms.ModelForm): #this form is present in Django form
    #in order to provide any kind of meta in4 about this form
    #we again create another class inside
    class Meta:
        #create field
        model = Product #receive related in4 of product
        fields = ['name', 'description', 'price', 'file']

        #the form is created above => then pass form to view 
        #from the view, pass to a template and render form

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
    

    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError['Password field do not match']
        return self.cleaned_data['password2']
    
    #The cleaned_data dictionary contains the field names as keys and the 
    #cleaned values as corresponding values. Use this when you want to customize fields
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control ',
        'placeholder': 'Enter comment here ...',
        'rows': '5',
        'style': 'width: 100%; resize: both;',
    }))

    

    