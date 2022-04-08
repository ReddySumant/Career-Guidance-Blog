
from django import forms
from .models import Post, Comment, newauth

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('name', 'text')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

        
class RegisterForm(forms.ModelForm):

    class Meta():
        model = newauth
        fields = ('name', 'email', 'about', 'phone', 'file', 'username', 'password')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'email': forms.TextInput(attrs={'class': 'textinputclass'}),
            'about': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            'phone': forms.TextInput(attrs={'class': 'textinputclass'}),
            'file': forms.FileField(),
            'username': forms.TextInput(attrs={'class': 'textinputclass'}),
            'password': forms.TextInput(attrs={'class': 'textinputclass'}),
        }