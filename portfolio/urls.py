from django.urls import path
from . import views as portfolio_views

app_name = "portfolio"

urlpatterns = [
    path("", portfolio_views.UserHome.as_view(), name="home"),
]
