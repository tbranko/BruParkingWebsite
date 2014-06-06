from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns
#from django.utils.translation import ugettext as _

from home.views import NotificationEmailView

from .sitemaps import StaticViewSitemap


from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = patterns('',
	url(r'i18n/', include('django.conf.urls.i18n')),
	url(r'favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
	url(r'^/sitemap\.xml$', RedirectView.as_view(url='/sitemap.xml')),
	# Serve sitemap.xml in static way, for now
	#url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

)

urlpatterns += i18n_patterns('',
	url(r'thank-you/$', TemplateView.as_view(template_name='thank_you.html'), name='thank-you'),
	url(r'bedankt/$', TemplateView.as_view(template_name='thank_you.html'), name='bedankt'),
	url(r'merci/$', TemplateView.as_view(template_name='thank_you.html'), name='merci'),
	url(r'^$', NotificationEmailView.as_view(), name='home'),
)
