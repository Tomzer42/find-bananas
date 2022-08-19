from django.db import models
from datetime import datetime

class Bananas(models.Model):
    timestamp = models.DateTimeField()
    nb_bananas_1 = models.IntegerField()
    nb_bananas_2 = models.IntegerField()
    nb_bananas_3 = models.IntegerField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = datetime.utcnow()
        return super(Bananas, self).save(*args, **kwargs)
