import requests
import json
import random
from django.conf import settings

class ImgurAPI:

   def __init__(self):
      self.__clientid = None
      token_file = None

      # Try to open the file in read-mode
      try:
         token_file = open("{0}/ninja/lib/TOKENS.txt".format(settings.BASE_DIR), "r")
      except:
         pass

      # Try to read the first line with the client-id
      try:
         self.__clientid = token_file.readline().strip('\n')
      except:
         pass

      # Print the client-id as a sanity check
      print("ClientID = {0}".format(self.__clientid))

      # Close the file
      token_file.close()

   # Function will get a random image from the requested channel
   def get_random_image(self, channel):

      if self.__clientid is None:
         raise ValueError("ClientID not initialized")

      header = {
            "Authorization": "Client-ID {0}".format(self.__clientid)
      }

      res = requests.get(channel, headers=header)
      json_str = res.text
      imgur_data = json.loads(json_str)

      image_url = imgur_data["data"][random.randint(0, (len(imgur_data["data"]) - 1))]["link"]

      return image_url
