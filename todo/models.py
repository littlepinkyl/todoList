from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime

# Create your models here.

class Todoitem(models.Model):
        item_title = models.CharField(max_length=50)
        created_time = models.DateTimeField('CreatedTime',auto_now_add=True)
        deadline_time = models.DateTimeField('Deadline',null=True)
        isDone = models.BooleanField(default=False)

        def __unicode__(self):
            return self.item_title

        def doIt(self):
            self.isDone = True







