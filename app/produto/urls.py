
from django.urls import path
from django.urls.conf import include

from .views import delete_produto, detail_produto, list_produtos, create_produto, update_produto

urlpatterns = [
    path('', list_produtos, name="list_produtos"),
    path('<int:id>/', detail_produto, name="detail_produto"),
    path('add/',create_produto, name="create_produto"),
    path('update/<int:id>/', update_produto, name="update_produto"),
    path('delete/<int:id>/', delete_produto, name="delete_produto")
]
