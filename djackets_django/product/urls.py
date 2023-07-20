from django.urls import path, include

from . import views


urlpatterns = [
   path('latest-products/', views.LatestProductList.as_view()),
   path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDeatilsView.as_view()),
   path('products/<slug:category_slug>/', views.CategoryDeatils.as_view()),
] 
