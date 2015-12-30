from django.shortcuts import render
from django.http import JsonResponse
from lib.imgur import ImgurAPI
from models import NinjaResult
import random

sub_reddits = [
      ("ninja", "https://api.imgur.com/3/gallery/r/ninja"),
      ("cat", "https://api.imgur.com/3/gallery/r/lolcats"),
      ("fail", "https://api.imgur.com/3/gallery/r/fail"),
      ("aww", "https://api.imgur.com/3/gallery/r/aww"),
]

# Index view
def index(request):
   return render(request, 'index.html', {})

# Route will respond with the image/subreddit information
def isninja(request):
   res = {
         "is_ninja": None,
         "message": None,
         "status": None,
         "image": None
   }

   chance = random.randint(0,100)
   index = None

   if (chance <= 10):
      index = 0
   elif (chance > 10 and chance <= 40):
      index = 1
   elif (chance > 40 and chance <= 70):
      index = 2
   elif (chance > 70 and chance <= 100):
      index = 3

   print("Selected Index is: {0} with a chance of {1}".format(index, chance))

   if (index is 0):
      res["is_ninja"] = True
   else:
      res["is_ninja"] = False

   if (index is 0):
      res["message"] = "You ARE the ninja! Congrats!"
   elif (index is 1):
      res["message"] = "Sorry. Cat's are not ninjas."
   elif (index is 2):
      res["message"] = "Sorry but you failed. You are not a ninja."
   elif (index is 3):
      res["message"] = "Awwwwww. Cute, but not a ninja."

   try:
      api = ImgurAPI()
      res["image"] = api.get_random_image(sub_reddits[index][1])
   except:
      res["image"] = None
      res["status"] = False

   res["status"] = True

   # Save a copy to the DB
   ip = request.META['REMOTE_ADDR']
   img = res["image"]
   mes = res["message"]

   db_result = NinjaResult(ip_address=ip, image=img, message=mes)
   db_result.save()

   return JsonResponse(res, content_type="application/json")
