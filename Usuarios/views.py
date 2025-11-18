from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FormularioRegistro, PostForm, ComentarioForm
from .models import Post, Comentario
from django import forms


def index_view(request):
    return render(request, 'index.html')

def registro_view(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('index')
    else:
        form = FormularioRegistro()
    return render(request, 'Usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                return redirect('index')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'Usuarios/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login')

@login_required
def perfil_view(request):
    return render(request, 'Usuarios/perfil.html')

def index_view(request):
    return render(request, 'index.html')

def editar_perfil(request):
    return render(request, 'Usuarios/editar_perfil.html')

def acerca_view(request):
    return render(request, 'paginas/acercade.html')

def aportar_view(request):
    return render(request, 'paginas/aportar.html')

def comunidad_view(request):
    return render(request, 'paginas/comunidad.html')




def forotecnologia_view(request):
    return render(request, 'paginas/foro/tecnologia.html')

def forosalud_view(request):
    return render(request, 'paginas/foro/salud.html')

def forohistoria_view(request):
    return render(request, 'paginas/foro/historia.html')

def forogastronomia_view(request):
    return render(request, 'paginas/foro/gastronomia.html')

def foroentretenimiento_view(request):
    return render(request, 'paginas/foro/entretenimiento.html')

def foroastronomia_view(request):
    return render(request, 'paginas/foro/astronomia.html')



def tecnologia_view(request):
    return render(request, 'paginas/categorias/tecnologia.html')

def salud_view(request):
    return render(request, 'paginas/categorias/salud.html')

def historia_view(request):
    return render(request, 'paginas/categorias/historia.html')

def gastronomia_view(request):
    return render(request, 'paginas/categorias/gastronomia.html')

def entretenimiento_view(request):
    return render(request, 'paginas/categorias/entretenimiento.html')

def astronomia_view(request):
    return render(request, 'paginas/categorias/astronomia.html')




def foroastronomia_view(request):
    posts = Post.objects.filter(categoria='astronomia').order_by('-fecha')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.categoria = 'astronomia'
            post.save()
            return redirect('foroastronomia')
    else:
        form = PostForm()
    return render(request, 'paginas/foro/astronomia.html', {'posts': posts, 'form': form})


def forotecnologia_view(request):
    posts = Post.objects.filter(categoria='tecnologia').order_by('-fecha')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.categoria = 'tecnologia'
            post.save()
            return redirect('forotecnologia')
    else:
        form = PostForm()
    return render(request, 'paginas/foro/tecnologia.html', {'posts': posts, 'form': form})


def foroentretenimiento_view(request):
    posts = Post.objects.filter(categoria='entretenimiento').order_by('-fecha')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.categoria = 'entretenimiento'
            post.save()
            return redirect('foroentretenimiento')
    else:
        form = PostForm()
    return render(request, 'paginas/foro/entretenimiento.html', {'posts': posts, 'form': form})

def forogastronomia_view(request):
    posts = Post.objects.filter(categoria='gastronomia').order_by('-fecha')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.categoria = 'gastronomia'
            post.save()
            return redirect('forogastronomia')
    else:
        form = PostForm()
    return render(request, 'paginas/foro/gastronomia.html', {'posts': posts, 'form': form})


def forohistoria_view(request):
    posts = Post.objects.filter(categoria='historia').order_by('-fecha')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.categoria = 'historia'
            post.save()
            return redirect('forohistoria')
    else:
        form = PostForm()
    return render(request, 'paginas/foro/historia.html', {'posts': posts, 'form': form})


def forosalud_view(request):
    posts = Post.objects.filter(categoria='salud').order_by('-fecha')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.categoria = 'salud'
            post.save()
            return redirect('forosalud')
    else:
        form = PostForm()
    return render(request, 'paginas/foro/salud.html', {'posts': posts, 'form': form})



def detalle_post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comentarios = Comentario.objects.filter(post=post).order_by('fecha')
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_post', post_id=post_id)
    else:
        form = ComentarioForm()
    return render(request, 'paginas/foro/detalle_post.html', {'post': post, 'comentarios': comentarios, 'form': form})



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'Usuarios/editar_perfil.html', {'form': form})