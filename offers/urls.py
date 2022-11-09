from django.urls import path

from .views import *

urlpatterns = [
    path('', OffersView.as_view(), name='offers'),
    path('create', OfferCreateView.as_view(), name='offer_create'),
]
