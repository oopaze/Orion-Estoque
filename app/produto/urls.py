
from django.urls import path
from django.urls.conf import include

from .views import delete_produto, detail_produto, create_produto, update_produto, ProdutosListView

urlpatterns = [
    path('', ProdutosListView.as_view(), name="list_produtos"),
    path('<int:id>/', detail_produto, name="detail_produto"),
    path('add/',create_produto, name="create_produto"),
    path('update/<int:id>/', update_produto, name="update_produto"),
    path('delete/<int:id>/', delete_produto, name="delete_produto")
]
