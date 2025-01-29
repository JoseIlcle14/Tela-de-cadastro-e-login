from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.users_login, name= 'login'),
    path("site/", views.site, name='site')
]