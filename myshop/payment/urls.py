from django.urls import path
from .views import *

app_name = "payment"
urlpatterns = [
    path("", payment, name="payment"),
]
