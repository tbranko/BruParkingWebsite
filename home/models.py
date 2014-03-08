from django.db import models

class NotificationEmail(models.Model):
    email = models.EmailField(blank=False, null=False, unique=True)
    ip = models.IPAddressField(default='0.0.0.0')
    create_date = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = "Emails"

    def __str__(self):
        return (self.email)
