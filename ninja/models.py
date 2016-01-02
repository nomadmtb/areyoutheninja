from django.db import models
import hashlib
from datetime import datetime
from lib.imgur import ImgurAPI
import json

# Create your models here.

class NinjaResult(models.Model):

   test_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
   ip_address = models.CharField(max_length=200, blank=False, null=False)
   uuid = models.CharField(max_length=250, unique=True, blank=False, null=False)
   image = models.CharField(max_length=200, blank=False, null=False)
   message = models.CharField(max_length=300, blank=False, null=False)
   is_ninja = models.BooleanField(default=False, blank=False, null=False)
   source_api = models.CharField(max_length=250, unique=False, blank=False, null=False)

   def save(self, *args, **kwargs):

      # Generate a new uuid if needed
      if self.pk is None:
         self.uuid = hashlib.sha1(str(datetime.now()) + self.ip_address + "SaltyMcSaltSalt").hexdigest()

      # Call built-in save method
      super(NinjaResult, self).save(*args, **kwargs)

class ResultSource(models.Model):

   created_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
   source_api = models.CharField(max_length=200, blank=False, null=False)
   result_message = models.CharField(max_length=500, blank=False, null=False)
   is_ninja = models.BooleanField(default=False)

   def get_data(self):

      api = ImgurAPI()
      image_url = None
      data = {}

      try:
         data["image_url"] = api.get_random_image(self.source_api)
      except:
         return False

      data["source_api"] = self.source_api
      data["result_message"] = self.result_message
      data["is_ninja"] = self.is_ninja

      return data



