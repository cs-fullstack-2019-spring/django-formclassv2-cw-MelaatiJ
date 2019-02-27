from django.urls import path
from . import views

#paths to two pages
urlpatterns = [
    path("", views.index, name="index"),
    path("apply/", views.apply, name="apply"),
    # path("applicant/", views.applicant, name="applicant")
    # path("applicant/", views.applicant, name="applicant"),

]