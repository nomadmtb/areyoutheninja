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

   # Test message
   messages.add_message(request, messages.WARNING, "Click the button to see if you are the ninja.");

   return render(request, 'index.html', {})

# Route will respond with the image/subreddit information
def isninja(request):

   # Get all source objects out of the database
   sources = ResultSource.objects.all()

   # Generate a random index into the sources
   index = random.randint(0,(len(sources)-1))

   # Select the correct source
   selected_source = sources[index]

   # Call the get_data method that will interact with the api
   data = selected_source.get_data()

   # Track the result
   result = NinjaResult(
         is_ninja=data["is_ninja"],
         image=data["image_url"],
         ip_address=request.META['REMOTE_ADDR'],
         message=data["result_message"],
         source_api=data["source_api"],
   )

   # Save the result
   result.save()

   # Get the UUID
   data["uuid"] = result.uuid

   # Return the response to the user
   if data is not False:
      return JsonResponse(data, content_type="application/json")
   else:
      return JsonResponse({error: "Error getting data from db"}, content_type="application/json")
