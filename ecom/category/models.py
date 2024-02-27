from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255, null = False)
    isActive = models.BooleanField(null = False)
    createdAt = models.DateField(auto_now_add = True)
    modifyAt = models.DateField(auto_now = True)
    
    class Meta:
        app_label = "category"
        db_table = "category"
        verbose_name = _("category")
        verbose_name_plural = _("category")

    def __str__(self):
        return self.name