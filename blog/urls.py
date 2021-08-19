from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="career-home"),
    path('about/', views.about, name="career-about"),
    path('test/',views.test, name="career-test"),
]
