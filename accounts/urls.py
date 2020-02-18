from django.contrib import admin
from django.urls import path, include
from .views import SignUpView
app_name = "accounts"
urlpatterns = [
   path('', SignUpView.as_view(), name="signup" )
]
