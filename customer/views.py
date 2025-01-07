from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import CustomerForm

from .models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = "customers"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.customer.all()


class CustomerCreateView(CreateView):
    model = Customer
    success_url = "/customer"
    form_class = CustomerForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save
        return HttpResponseRedirect(self.get_success_url)


class CustomerUpdateView(UpdateView):
    model = Customer
    success_url = "/customer"
    form_class = CustomerForm


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = "/customer"
    template_name = "customer/customer_delete.html"


class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = "customer"
