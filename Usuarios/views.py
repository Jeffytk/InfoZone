from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import FormularioRegistro

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