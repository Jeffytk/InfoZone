from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    email = models.EmailField(unique=True, blank=False, verbose_name="Correo Electrónico")
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Post(models.Model):
    CATEGORIAS = [
        ('astronomia', 'Astronomía'),
        ('tecnologia', 'Tecnología'),
        ('salud', 'Salud'),
        ('historia', 'Historia'),
        ('entretenimiento', 'Entretenimiento'),
        ('gastronomia', 'Gastronomía'),
    ]
    titulo = models.CharField(max_length=255)
    mensaje = models.TextField()
    autor = models.ForeignKey('UsuarioPersonalizado', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS)

    def __str__(self):
        return f"[{self.get_categoria_display()}] {self.titulo}"

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey('UsuarioPersonalizado', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=30, choices=Post.CATEGORIAS)  # <--- NUEVO CAMPO

    def __str__(self):
        return f"[{self.get_categoria_display()}] {self.autor} en {self.post.titulo}"
