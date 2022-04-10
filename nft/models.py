from django.db.models import (
    CharField, Model, ImageField, ManyToManyField, DateTimeField, ForeignKey, CASCADE
    )

class Image(Model):
    name = CharField(max_length=120)
    image = ImageField(null=True, blank=True)
    uploaded_on = DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name


class Collection(Model):
    name = CharField(max_length=120)
    images = ManyToManyField(Image)
    created_on = DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name