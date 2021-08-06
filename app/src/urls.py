from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LogoutView

from user.views import CustomLoginView
from .views import home


urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('user/', include('user.urls'), name="user"),
    path('produto/', include('produto.urls'), name="produto"),
    path('venda/', include('venda.urls'), name="venda"),
    
]



