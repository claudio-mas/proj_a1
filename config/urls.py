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
from apps.estoque.views import index, ajax_carregar_grupos, ajax_carregar_produtos, ajax_obter_preco_produto
from apps.clientes.views import lista_clientes
from django.conf import settings
from django.conf.urls.static import static
from apps.clientes import views
from apps.orcamentos.views import lista_orcamentos, editar_orcamento, excluir_orcamento, detalhar_orcamento, adicionar_item_orcamento
from apps.orcamentos.views import editar_item_orcamento, excluir_item_orcamento, itens_orcamento
from apps.orcamentos.views import OrcamentoCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('clientes/', lista_clientes, name='clientes'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:pk>/', views.confirmar_exclusao, name='confirmar_exclusao'),
    path('excluir/<int:pk>/confirmar/', views.excluir_cliente, name='excluir_cliente'),
    path('novo/', views.novo_cliente, name='novo_cliente'),
    path('lista-orcamentos/', lista_orcamentos, name='lista_orcamentos'),
    path('orcamento/novo/', OrcamentoCreateView.as_view(), name='novo_orcamento'),
    path('orcamento/editar/<int:id>/', editar_orcamento, name='editar_orcamento'),
    path('orcamento/excluir/<int:id>/', excluir_orcamento, name='excluir_orcamento'),
    path('orcamento/<int:orcamento_id>/', detalhar_orcamento, name='detalhar_orcamento'),
    path('orcamento/<int:orcamento_id>/adicionar_item/', adicionar_item_orcamento, name='adicionar_item_orcamento'),
    path('orcamento/<int:orcamento_id>/item/<int:item_id>/editar/', editar_item_orcamento, name='editar_item_orcamento'),
    path('orcamento/<int:orcamento_id>/item/<int:item_id>/excluir/', excluir_item_orcamento, name='excluir_item_orcamento'),
    path('orcamento/<int:orcamento_id>/itens/', itens_orcamento, name='itens_orcamento'),
    path('ajax/carregar-grupos/', ajax_carregar_grupos, name='ajax_carregar_grupos'),
    path('ajax/carregar-produtos/', ajax_carregar_produtos, name='ajax_carregar_produtos'),
    path('ajax/obter-preco-produto/', ajax_obter_preco_produto, name='ajax_obter_preco_produto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
