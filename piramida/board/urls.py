from django.urls import path
from board.views import board_page


urlpatterns = [
    path('', board_page, name='basket_page'),
]
