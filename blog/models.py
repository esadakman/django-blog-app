from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, default='blog_default.png',upload_to='user_directory_path')  
    blog_view = models.IntegerField(default=0, blank=True) 
    likes = models.ManyToManyField(User, blank=True, related_name="collected_votes") 
    blog_comment = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_user", null=True)  
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.post.title}"
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
        