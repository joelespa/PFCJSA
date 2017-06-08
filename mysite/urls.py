from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib import admin
from sopa.views import *
from sopa import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Login.as_view(), name="login"),
    url(r'^home/', views.home,name='home'),
    url(r'^logout$', logout, name="logout", kwargs={'next_page': '/'}),
    url(r'^new_user$', RegistroUsuario.as_view(), name='nuevo_usuario'),
    url(r'^empresas/$', views.lista_empresas, name='lista_empresas'),
    url(r'^empresas/new/$', views.nueva_empresa, name='nueva_empresa'),
    url(r'^usuarios/miperfil/$', views.miperfil, name='mi_perfil'),
    url(r'^usuarios/$', views.lista_usuarios, name='lista_usuarios'),
    url(r'^usuarios/(?P<u>.+)/$', views.detalle_usuario, name='detalle_usuarios'),
    ]
