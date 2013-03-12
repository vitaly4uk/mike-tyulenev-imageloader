from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField


class ImageItem(models.Model):
    name = models.CharField(max_length=200)
    image = ImageField(upload_to="upload")

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})
