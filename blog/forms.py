from django import forms
from .models import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['blog_topic','blog_post','author']
        labels={
            'blog_topic': '',
            'blog_post':'',
            'author':''
        }


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:

        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user    