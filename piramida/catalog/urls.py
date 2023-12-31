from django.urls import path
from .views import CategoryListView, ProductListView


urlpatterns = [
    # path('', proba_page, name='proba_page'),
    path('', CategoryListView.as_view(), name='category'),  # product-detail
    path("<int:pk>/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductListView.as_view(), name="product-detail"),
]
