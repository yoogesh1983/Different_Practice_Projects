from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.forms import DateInput
from YMSBlog.models import EmailForm, Comment, Post


class EmailSendRequest(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = EmailForm

        # I want all fields present inside model
        fields = '__all__'


class CommentRequest(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class AddUserRequest(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'is_staff')

class AddPostRequest(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body', 'tags', 'status')