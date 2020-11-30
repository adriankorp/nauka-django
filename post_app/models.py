from django.db.models import Model, CharField, ForeignKey, DateTimeField, DO_NOTHING, TextField, SlugField
# Create your models here
from django_extensions.db.fields import AutoSlugField
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(Model):
    name = CharField(max_length=128)
    slug = AutoSlugField(populate_from='name', max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(Model):
    title = CharField(max_length=128)
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    text = TextField(default='')
    created_at = DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
