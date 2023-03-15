from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=1, choices=(("u", "publiczna"), ("r", "prywatna")), null=True, blank=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

