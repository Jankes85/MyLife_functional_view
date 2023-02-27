from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.about_me),
    path('education/', views.education),
    path('courses/', views.courses),
    path('experience/', views.experience),
    path('interests/', views.interests),

]