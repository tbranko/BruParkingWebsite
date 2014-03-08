# forms.py
from django import forms
from home.models import NotificationEmail

class NotificationEmailForm(forms.ModelForm):
	email = forms.EmailField
	error_css_class = 'has-error'
	
	class Meta:
		model = NotificationEmail
		fields = ['email', 'ip']
		widgets = { 'email': forms.TextInput(attrs={'class':'form-control home-input', 'placeholder':'Email'}) }
		
	def clean(self):
		super(NotificationEmailForm, self).clean() #if necessary
		if 'email' in self._errors:
			# Get "uncleaned" data
			data_email = self.data["email"]
			# Strip spaces
			data_email.replace(" ", "")
			if data_email == "":
				raise forms.ValidationError(('Missing email'), code='missing_email')
			else:
				del self.data["email"]
		return self.cleaned_data
	
	def clean_email(self):
		email = self.cleaned_data['email']
		email_from_db = NotificationEmail.objects.get(email=email)
		if (email_from_db):
			pass
	
	def full_clean(self):
		super(NotificationEmailForm, self).full_clean()
		email = self.data['email'] or ''
		email_from_db = NotificationEmail.objects.get(email=email)
		if (email_from_db and self._errors['email']):
			del self._errors['email']
		
		return self.cleaned_data
	
	def save(self):
		email = self.data['email']
		email_from_db = NotificationEmail.objects.get(email=email)
		if (email_from_db):
			pass
		else:
			super(NotificationEmailForm, self).save()