from django.urls import path
from .views import RegCreate, RegList, RegDetail, RegUpdate, RegTemplate
from . import views


urlpatterns = [
    path("ll", RegCreate.as_view(), name="home"),
    path("list-items/", RegList.as_view(), name="listss"),
    path("list-d/<int:pk>", RegDetail.as_view(), name="detail"),
    path("list-d/<int:pk>/update", RegUpdate.as_view(), name="update"),
    path("thank/", RegTemplate.as_view(), name='thank'),
]