from django.urls import path

from . import views
from .views import QuoteList

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('show', QuoteList.as_view(), name='show-quotes'),
]
