from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from home.views import NotificationEmailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^thank-you/$', TemplateView.as_view(template_name='thank_you.html')),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
	url(r'^$', NotificationEmailView.as_view()),
)
