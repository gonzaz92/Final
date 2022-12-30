from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from mi_blog.models import Post, Avatar, Mensaje
from mi_blog.forms import UsuarioForm
from django.db.models import Q

def index(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.order_by('-id').all()
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) |
                                    Q(sub_titulo__icontains = queryset) |
                                    Q(texto__icontains = queryset)).distinct()
    return render(request, 'mi_blog/index.html', {'posts': posts})

def about(request):
    return render(request, 'mi_blog/about.html')

class PostDetalle(DetailView):
    model = Post

class PostListar(LoginRequiredMixin,ListView):
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