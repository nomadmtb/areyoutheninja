from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from lib.imgur import ImgurAPI
from models import NinjaResult
from models import ResultSource
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
   sources = ResultSource.objects.all()
   index = random.randint(0,(len(sources)-1))
   selected_source = sources[index]

   data = selected_source.get_data()

   result = NinjaResult(
         is_ninja=data["is_ninja"],
         image=data["image_url"],
         ip_address=request.META['REMOTE_ADDR'],
         message=data["result_message"],
         source_api=data["source_api"]
   )

   result.save()

   if data is not False:
      return JsonResponse(data, content_type="application/json")
   else:
      return JsonResponse({error: "Error getting data from db"}, content_type="application/json")
