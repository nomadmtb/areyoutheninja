import requests

class ImgurAPI:

   def __init__(self):
      self.__clientid = None
      token_file = None

      # Try to open the file in read-mode
      try:
         token_file = open("TOKENS.txt", "r")
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

      json_str = requests.get(channel, headers=header)
      print(json_str.text)
