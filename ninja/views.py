from django.shortcuts import render
from django.http import JsonResponse
import json

# Index view
def index(request):
   return render(request, 'index.html', {})

def isninja(request):
   res = {
         "is_ninja": None,
         "message": None,
         "status": None,
         "image": None
   }

   return JsonResponse(res, content_type="application/json")
