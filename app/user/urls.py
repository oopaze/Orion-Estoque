from django.urls import path


from . import views

urlpatterns = [
    path("detail/", views.user_detail_view, name="self_detail_user"),
    path("update/", views.update_user, name="self_update_user")
]
