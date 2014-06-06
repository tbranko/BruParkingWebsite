from home.forms import NotificationEmailForm
from django.views.generic.edit import CreateView
from .models import NotificationEmail

class NotificationEmailView(CreateView):
	template_name = 'home.html'
	form_class = NotificationEmailForm
	
	
	model = NotificationEmail
	
	def get_form_kwargs(self):
		kwargs = {}
		if self.request.method in ('POST'):
			#kwargs.update({'data': self.request.POST})
			kwargs['data'] = {}
			kwargs['data']['email'] = self.request.POST.get('email')
			kwargs['data']['ip'] = self.request.META.get('HTTP_X_FORWARDED_FOR','') or self.request.META.get('REMOTE_ADDR')
		
		return kwargs

	def get_success_url(self):
		#return CreateView.get_success_url(self)
		success_url = 'thank-you/'
		
		if (self.request.LANGUAGE_CODE == 'nl'):
			success_url = 'bedankt/'
		
		if (self.request.LANGUAGE_CODE == 'fr'):
			success_url = 'merci/'
		
		return success_url