from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Post, Comentario

Usuario = get_user_model()

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")  
    email = forms.EmailField(label="Correo electrónico", required=True)  
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)  
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name' , 'last_name', 'password1', 'password2']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'mensaje']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']