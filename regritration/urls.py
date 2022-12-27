from django.urls import path
from .views import RegCreate, RegList, RegDetail, RegUpdate, RegTemplate, homedetail, home
from . import views


urlpatterns = [
    path("ll", RegCreate.as_view(), name="home"),
    path("list-items/", RegList.as_view(), name="listss"),
    path("list-d/<int:pk>", RegDetail.as_view(), name="detail"),
    path("list-d/<int:pk>/update", RegUpdate.as_view(), name="update"),
    path("thank/", RegTemplate.as_view(), name='thank'),
    path("listsss/<int:pk>/", homedetail.as_view(), name='homedetail'),
    # path("list-d/<int:pk>/1", .as_view(), name="detail2"),
    path("", home.as_view(), name="home1"),
]