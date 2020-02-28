from django.urls import path

from . import views
from .views import QuoteList, QuoteView

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('show/<int:pk>', QuoteView.as_view(), name='quote-details'),
    path('show', QuoteList.as_view(), name='show-quotes'),
]
