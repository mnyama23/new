from django.urls import path
from .views import login_view
from .views import next

urlpatterns = [
    path("", login_view, name="login"),
    path("continue", next, name="next"),
]
