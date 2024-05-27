from django.urls import path
from users.api import CreateUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name="register")
]
