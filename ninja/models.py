from django.db import models
import hashlib
from datetime import datetime

# Create your models here.

class NinjaResult(models.Model):

   test_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
   ip_address = models.CharField(max_length=200, blank=False, null=False)
   uuid = models.CharField(max_length=250, blank=False, null=False)
   image = models.CharField(max_length=200, blank=False, null=False)
   message = models.CharField(max_length=300, blank=False, null=False)

   def save(self, *args, **kwargs):

      # Generate a new uuid if needed
      if self.pk is None:
         self.message_id = hashlib.sha1(str(datetime.now()) + self.ip_address + "SaltyMcSaltSalt").hexdigest()

      # Call built-in save method
      super(NinjaResult, self).save(*args, **kwargs)
