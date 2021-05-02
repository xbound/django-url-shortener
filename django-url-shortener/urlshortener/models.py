from django.db import models
from hashlib import md5


class UrlManager(models.Manager):
    def create(self, url: str):
        hashed_url = md5(url.encode()).hexdigest()[:10]
        return super().create(url=url, hashed_url=hashed_url)
    
    def create_or_get(self, url: str) -> 'Url':
        try:
            url = self.get_queryset().get(url=url)
        except Url.DoesNotExist:
            url = self.create(url)
        return url


class Url(models.Model):
    url = models.URLField(unique=True)
    hashed_url = models.CharField(unique=True, max_length=10)

    objects = UrlManager()

    def __str__(self):
        return f"{self.__class__.__name__} {self.url} {self.hashed_url}"