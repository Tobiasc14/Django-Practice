from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)