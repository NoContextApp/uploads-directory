from django.db import models
import os 
import uuid
# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "platform"
        verbose_name_plural = "platforms"
        ordering = ["-id"]
        
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ["-id"]
        
        
def file_path_and_name(instance, filename):
    """Change the filename to 'uuid.ext"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("files/", filename)

        
class File(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    reply_count = models.IntegerField(blank=True, null=True)
    like_count = models.IntegerField(blank=True, null=True)
    repost_count = models.IntegerField(blank=True, null=True)
    
    upvotes_count = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    source = models.URLField()
    file = models.FileField(upload_to=file_path_and_name)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.file}"
    
    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"
        ordering = ["-id"]