from .views import Roomview
from django.urls import path

urlpatterns = [
    path('',Roomview.as_view())
]
