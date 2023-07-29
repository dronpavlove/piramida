from django.urls import path
from .views import proba_page, CategoryListView


urlpatterns = [
    # path('', proba_page, name='proba_page'),
    path('', CategoryListView.as_view(), name='category')
]
