from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MyModel(MPTTModel):
    name = models.CharField(max_length=60)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children')
    slug = models.SlugField(max_length=60, verbose_name='url', unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

