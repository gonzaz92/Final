from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from mi_blog.models import Post, Avatar, Mensaje
from mi_blog.forms import UsuarioForm

def index(request):
    posts = Post.objects.order_by('-fecha_publicacion').all()
    return render(request, 'mi_blog/index.html', {'posts': posts})

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post

class PostCrear(LoginRequiredMixin,CreateView):
    model = Post
    success_url = reverse_lazy('mi_blog_listar')
    fields = '__all__'

class PostBorrar(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('mi_blog_listar')

class PostActualizar(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = reverse_lazy('mi_blog_listar')
    fields = '__all__'

class UserSingUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('mi_blog_listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('mi_blog_listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('mi_blog_index')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('mi_blog_listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('mi_blog_listar')

class MensajeDetail(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje

class MensajeCrear(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy('mi_blog_mensajes_crear')
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin,DeleteView):
    model = Mensaje
    success_url = reverse_lazy('mi_blog_mensajes_listar')