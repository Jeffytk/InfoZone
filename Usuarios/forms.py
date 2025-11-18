from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")  
    email = forms.EmailField(label="Correo electrónico", required=True)  
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)  
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput) 
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']