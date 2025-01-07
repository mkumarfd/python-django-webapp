from django.urls import path

from . import views

urlpatterns = [
    path('customer', views.CustomerListView.as_view(), name="customer.list"),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(),
         name="customer.detail"),
    path('customer/new', views.CustomerCreateView.as_view(), name="customer.new"),
    path('customer/<int:pk>/edit',
         views.CustomerUpdateView.as_view(), name="customer.update"),
    path('customer/<int:pk>/delete',
         views.CustomerDeleteView.as_view(), name="customer.delete"),
]
