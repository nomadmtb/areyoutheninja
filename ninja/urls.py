from django.conf.urls import url
from . import views

urlpatterns = [
      url(r'isninja$', views.isninja, name='isninja'),
]
