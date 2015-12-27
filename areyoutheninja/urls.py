from django.conf.urls import patterns, include, url
from django.contrib import admin
from ninja import views as ninja_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'areyoutheninja.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', ninja_views.index, name="index"),
    url(r'^api/', include('ninja.urls')),

# Only during DEV!
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
