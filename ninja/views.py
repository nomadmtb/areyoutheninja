from django.shortcuts import render
from django.http import JsonResponse
from lib.imgur import ImgurAPI
import random

sub_reddits = [
      ("cat", "https://api.imgur.com/3/gallery/r/lolcats"),
      ("ninja", "https://api.imgur.com/3/gallery/r/ninja"),
      ("fail", "https://api.imgur.com/3/gallery/r/fail"),
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

   if (chance <= 25):
      index = 2
   elif (chance > 25 and chance <= 75):
      index = 1
   elif (chance > 75 and chance <= 100):
      index = 3

   print("Selected Index is: {0} w/ chance og {1}".format(index, chance))

   return JsonResponse(res, content_type="application/json")
