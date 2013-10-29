from django.db import models

class Model(models.Model):
    """
    Stores a single Model skel
    """
    name = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)
