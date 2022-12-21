from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    TemplateView
)
from .models import Reg
from .forms import RegCustom
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin


# Create your views here.
class RegCreate(LoginRequiredMixin, CreateView):
    model = Reg
    form_class= RegCustom
    template_name = "rgritration/RegCreate.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #fields = "__all__"


class RegList(LoginRequiredMixin, ListView):
    model = Reg
    template_name = "rgritration/RegList.html"
    context_object_name = "Reg"
    

class RegDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView,):
    model = Reg
    template_name = 'rgritration/RegDetail.html'
    fields = "__all__"
    context_object_name = "Reg"
    def test_func(self):
        user = self.get_object()
        return user.author == self.request.user



class RegUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView ):
    model = Reg
    template_name = 'rgritration/Regupdate.html'
    fields = "__all__"
    
    def test_func(self):
        user = self.get_object()
        return user.author == self.request.user


class RegTemplate(LoginRequiredMixin, TemplateView,):
    template_name = 'rgritration/thank.html'
    # def test_func(self):
    #     user = self.get_object()
    #     return user.author == self.request.user


class home(CreateView):
    template_name = 'rgritration/home.html'