"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from mi_blog.views import (index, about, PostDetalle, PostListar, PostCrear, PostBorrar, 
                        PostActualizar, UserSingUp, UserLogin, UserLogout, AvatarActualizar,
                        UserActualizar, MensajeCrear, MensajeListar, MensajeBorrar, MensajeDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='mi_blog_index'),
    path('mi_blog/about', about, name='mi_blog_about'),
    path('mi_blog/crear', PostCrear.as_view(), name='mi_blog_crear'),
    path('mi_blog/<int:pk>/detalle', PostDetalle.as_view(), name='mi_blog_detalle'),
    path('mi_blog/listar', PostListar.as_view(), name='mi_blog_listar'),
    path('mi_blog/<int:pk>/actualizar', staff_member_required(PostActualizar.as_view()), name='mi_blog_actualizar'),
    path('mi_blog/<int:pk>/borrar', staff_member_required(PostBorrar.as_view()), name='mi_blog_borrar'),
    path('mi_blog/singup', UserSingUp.as_view(), name='mi_blog_singup'),
    path('mi_blog/login', UserLogin.as_view(), name='mi_blog_login'),
    path('mi_blog/logout', UserLogout.as_view(), name='mi_blog_logout'),
    path('mi_blog/user/<int:pk>/actualizar', UserActualizar.as_view(), name='mi_blog_user_actualizar'),
    path('mi_blog/avatar/<int:pk>/actualizar', AvatarActualizar.as_view(), name='mi_blog_avatar_actualizar'),
    path('mi_blog/mensajes/crear', MensajeCrear.as_view(), name='mi_blog_mensajes_crear'),
    path('mi_blog/mensajes/listar', MensajeListar.as_view(), name='mi_blog_mensajes_listar'),
    path('mi_blog/mensajes/<int:pk>/detalle', MensajeDetail.as_view(), name='mi_blog_mensajes_detalle'),
    path('mi_blog/mensajes/<int:pk>/borrar', staff_member_required(MensajeBorrar.as_view()), name='mi_blog_mensajes_borrar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
