...
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from myapp import views

admin.autodiscover()

urlpatterns = [
    url(r'^favicon.ico$', RedirectView.as_view(
                          url=staticfiles_storage.url('favicon.ico'),
                          permanent=False), name="favicon"),
    url(r'^$', views.home, name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
]
