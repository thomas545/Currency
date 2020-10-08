from django.urls import path
from . import views


urlpatterns = [
    path("rate/", views.CurrencyAPIView.as_view(), name="get_currency"),
    path("rates/", views.CurrencyView.as_view(), name="currency"),
]
