from django.urls import path, include
from proj_teste.clientes.views import persons_list

urlpatterns = [
    path('list/', persons_list),
]