from django.db import models

# Model for your profile information
class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    short_bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name

# Model for your learning journey entries
class LearningEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    screenshot = models.ImageField(upload_to='entry_screenshots/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.created_at})"
