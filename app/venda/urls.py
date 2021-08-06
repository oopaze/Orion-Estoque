from django.urls import path
from django.urls.conf import include

from .views import create_venda, VendasListView, detail_venda, update_venda, delete_venda

urlpatterns = [
    path("", VendasListView.as_view(), name="list_vendas"),
    path('add/', create_venda, name="create_venda"),
    path('detail/<int:id>/', detail_venda, name="detail_venda"),
    path('update/<int:id>/', update_venda, name="update_venda"),
    path('delete/<int:id>/',delete_venda,name="delete_venda"),
]