from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="images", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to=r"images/%Y/%m/%d")
    description = models.TextField(blank=True)
    # db_index 会在数据库中为created_time创建索引
    created_time = models.DateField(auto_now_add=True, db_index=True)
    # 这里引入多对多关系，以前没有用过
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="images_like", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.description:
            self.description = "Here is no description"
        super(Image, self).save(*args, **kwargs)
           