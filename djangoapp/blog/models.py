from django.db import models
from utils.rands import new_slugify


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    name = models.CharField(max_length=55)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        default=None,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.name)
        return super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=55)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        default=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.name)
            return super().save(*args, **kwargs)
