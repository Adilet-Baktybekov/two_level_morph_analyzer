from django.urls import path
from analyzer_website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('analyzer', views.analyzer, name='analyzer'),
    path('validate', views.validate, name='validate')
]
