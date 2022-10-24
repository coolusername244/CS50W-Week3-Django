from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lee", views.lee, name="lee"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet"),
    
]