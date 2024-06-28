from django.urls import path

from . import views
from summarization.views import home

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("aboutus/", views.aboutpage, name ="aboutpage" )
]