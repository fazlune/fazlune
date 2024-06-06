from django.urls import path
from products import views
from .views import CreateProduct

app_name = 'products'
urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('products/<slug:slug>/', views.detail_page, name='detail'),
    path('products/<slug:slug>/<int:id>', views.delete_reviews, name='delete-reviews'),
    path('products/<slug:slug>/edit/<int:id>', views.edit_reviews, name='edit-reviews'),
    path('create/', CreateProduct.as_view(), name='create'),
    path('technoshop/author/', views.author_page, name='author')
]
