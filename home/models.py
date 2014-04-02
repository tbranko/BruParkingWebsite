from django.db import models

class NotificationEmail(models.Model):
	email = models.EmailField(blank=False, null=False, unique=False)
	ip = models.IPAddressField(default='0.0.0.0')
	create_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Emails"

	def __unicode__(self):
		return (self.email)
