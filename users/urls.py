from django.urls import path
from users.api import CreateUserView, RetrieveUserDetailsView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name="register"),
    path('<int:pk>/', RetrieveUserDetailsView().as_view(), name="retrieve user details")
]
