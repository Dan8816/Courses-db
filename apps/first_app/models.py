from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<course: {} | {}, {}, {}>".format(self.id, self.name, self.desc, self.created_at)