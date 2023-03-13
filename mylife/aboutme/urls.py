from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.about_me, name="about_me"),
    path('education/', views.education, name="education"),
    path('contact/', views.contact, name="contact"),
    path('skills/', views.skills, name="skills"),
    path('experience/', views.experience, name="experience"),
    path('interests/', views.interests, name="interests"),
    path('blog/', views.blog, name="blog"),
    path('thank-you/', views.thanks, name="thanks"),

]