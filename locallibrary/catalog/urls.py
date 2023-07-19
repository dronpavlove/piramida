from django.urls import path
from .views import proba_page


urlpatterns = [
    path('', proba_page, name='proba_page'),
]
