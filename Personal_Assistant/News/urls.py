from django.urls import path, include

from . import views

app_name = "News"

urlpatterns = [
    path("", views.main, name="main"),
    path("", views.display_requests_page, name="display_requests_page"),
    path('users/', include('users.urls')),
]