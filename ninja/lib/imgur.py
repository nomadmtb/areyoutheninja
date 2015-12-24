import requests

class ImgurAPI:

   def __init__(self):
      self.__clientid = None
      token_file = None

      try:
         token_file = open("TOKENS.txt", "r")
      except:
         pass

      try:
         self.__clientid = token_file.read_line()
      except:
         pass
