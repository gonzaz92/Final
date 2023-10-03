from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mi_blog.models import Post
from ckeditor.widgets import CKEditorWidget

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    texto = forms.CharField(widget=CKEditorWidget())