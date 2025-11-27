from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=400, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_latest = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title