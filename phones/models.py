from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="phones/images/")
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = "phones"
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
