from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.about_me, name="about_me"),
    path('education/', views.education, name="education"),
    path('courses/', views.courses, name="courses"),
    path('skills/', views.skills, name="skills"),
    path('experience/', views.experience, name="experience"),
    path('interests/', views.interests, name="interests"),
    path('blog/', views.blog, name="blog"),

]