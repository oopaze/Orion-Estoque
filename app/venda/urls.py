from django.urls import path
from django.urls.conf import include

from .views import add_produto_save, create_venda, VendasListView, detail_venda, finalizar_venda, update_venda, delete_venda, get_bairros, add_produto

urlpatterns = [
    path("", VendasListView.as_view(), name="list_vendas"),
    path('add/', create_venda, name="create_venda"),
    path('detail/<int:id>/', detail_venda, name="detail_venda"),
    path('add_produtos/<int:id>/', add_produto, name="venda_adicionar_produtos"),
    path('finalizar/<int:id>/', finalizar_venda, name="finalizar_venda"),
    path('produtos/<int:id>/', add_produto_save, name="adicionar_produtos"),
    path('update/<int:id>/', update_venda, name="update_venda"),
    path('delete/<int:id>/',delete_venda,name="delete_venda"),
    path('bairros/', get_bairros, name="get_bairros")
]