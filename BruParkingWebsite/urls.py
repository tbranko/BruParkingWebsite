from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from home.views import NotificationEmailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', NotificationEmailView.as_view()),
	url(r'^i18n/', include('django.conf.urls.i18n')),
)
