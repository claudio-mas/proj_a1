"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from apps.estoque.views import index
from apps.clientes.views import lista_clientes
from django.conf import settings
from django.conf.urls.static import static
from apps.clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('clientes/', lista_clientes, name='clientes'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:pk>/', views.confirmar_exclusao, name='confirmar_exclusao'),
    path('excluir/<int:pk>/confirmar/', views.excluir_cliente, name='excluir_cliente'),
    path('novo/', views.novo_cliente, name='novo_cliente'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)