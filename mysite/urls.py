# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib import admin
from sopa.views import *
from sopa import views


# manage.py migrate --run-syncdb

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', Login.as_view(), name="login"),
    url(r'^$', views.home,name='home'),
    url(r'^logout$', logout, name="logout", kwargs={'next_page': '/'}),
    url(r'^new_user$', RegistroUsuario.as_view(), name='nuevo_usuario'),
    url(r'^usuarios/miperfil/edit/(?P<pk>.+)/$', EditUsuario.as_view(), name='edit_usuario'),
    url(r'^empresas/$', views.lista_empresas, name='lista_empresas'),
    url(r'^empresas/new/$', crearempresa.as_view(), name='nueva_Empresa'),
    url(r'^empresas/edit/(?P<pk>.+)/$', editarempresa.as_view(), name='edita_Empresa'),
    url(r'^empresas/buscar/$', views.buscar_empresa, name='buscar_empresa'),
    url(r'^empresas/(?P<pk>.+)/$', views.detalle_empresa, name='detalle_empresa'),
    url(r'^usuarios/miperfil/$', views.miperfil, name='mi_perfil'),
    url(r'^usuarios/buscar/$', views.buscar_usuario, name='buscar_usuario'),
    url(r'^usuarios/$', views.lista_usuarios, name='lista_usuarios'),
    url(r'^usuarios/(?P<u>.+)/$', views.detalle_usuario, name='detalle_usuarios'),
    url(r'^encuesta/$', views.lista_encuestas, name='lista_encuestas'),
    url(r'^encuesta/buscar/$', views.buscar_encuesta, name='buscar_encuesta'),
    url(r'^encuesta/nueva/(?P<e>.+)/(?P<d>.+)/(?P<t>.+)$', EncuestaWizard.as_view([PreguntasFundamentalesForm, PreguntasBasicasForm, PreguntasOpcionalesForm, PreguntasAnecdoticasForm])),
    url(r'^encuesta/detalle/(?P<pk>.+)/$', views.detalle_encuesta, name='detalle_encuesta'),
    url(r'^encuesta/eliminar/(?P<pk>.+)/$', views.eliminar_encuesta, name='eliminar_encuesta'),
    url(r'^ayuda/$', views.ayuda, name='ayuda'),
    ]
