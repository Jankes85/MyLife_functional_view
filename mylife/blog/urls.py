from django.urls import path
from . import views

urlpatterns = [
    path('blank/', views.blank, name="blank"),
    path("calendar_current/", views.calendar_current, name="calendar_current"),
    path("calendar_current/<int:year>/<int:month>", views.calendar_change, name="calendar_change"),

]