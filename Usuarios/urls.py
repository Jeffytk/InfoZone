from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('acerca/', views.acerca_view, name='acerca'),
    path('aportar/', views.aportar_view, name='aportar'),
    path('comunidad/', views.comunidad_view, name='comunidad'),
    
    
    
    path('tecnologia/', views.tecnologia_view, name='tecnologia'),
    path('gastronomia/', views.gastronomia_view, name='gastronomia'),
    path('astronomia/', views.astronomia_view, name='astronomia'),
    path('entretenimiento/', views.entretenimiento_view, name='entretenimiento'),
    path('salud/', views.salud_view, name='salud'),
    path('historia/', views.historia_view, name='historia'),
    
    
    
    
    path('forotecnologia/', views.forotecnologia_view, name='forotecnologia'),
    path('forogastronomia/', views.forogastronomia_view, name='forogastronomia'),
    path('foroastronomia/', views.foroastronomia_view, name='foroastronomia'),
    path('foroentretenimiento/', views.foroentretenimiento_view, name='foroentretenimiento'),
    path('forosalud/', views.forosalud_view, name='forosalud'),
    path('forohistoria/', views.forohistoria_view, name='forohistoria'),
    
    
    
    
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='usuarios/password_reset.html',
             email_template_name='usuarios/password_reset_email.html',
             subject_template_name='usuarios/password_reset_subject.txt'
         ), 
         name='password_reset'),
    
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='usuarios/password_reset_done.html'
         ), 
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='usuarios/password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),
    
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='usuarios/password_reset_complete.html'
         ), 
         name='password_reset_complete'),



    path('foroastronomia/', views.foroastronomia_view, name='foroastronomia'),
    path('foroastronomia/<int:post_id>/', views.detalle_post_view, name='detalle_post'),
    path('forotecnologia/', views.forotecnologia_view, name='forotecnologia'),
    path('forotecnologia/<int:post_id>/', views.detalle_post_view, name='detalle_post'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    
]
