# coding=utf-8
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

from blog.views import HomeView

urlpatterns = [
                  url(r'^$', HomeView.as_view(), name='home'),
                  url(r'^docs/', include('documents.urls')),
                  url(r'^brief/', include('brief.urls')),
                  url(r'^blog/', include('blog.urls')),
                  url(r'^albums/', include('albums.urls')),
                  url(r'^translation/', include('translation.urls')),
                  url(r'^resource/', include('resource.urls')),

                  # 将后台的url修改下
                  url(r'^admin/$',
                      RedirectView.as_view(url='/', permanent=True)),
                  url(r'^backend/', include(admin.site.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
