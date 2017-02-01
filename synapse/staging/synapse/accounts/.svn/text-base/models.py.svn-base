from django.db import models
from django.contrib.auth.models import User



# http://www.turnkeylinux.org/blog/django-profile

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    # url = models.URLField("Website", blank=True)
    # company = models.CharField(max_length=50, blank=True)
    # home_address = models.TextField()
    # phone_numer = models.PhoneNumberField()

User.profile = property(lambda u:
        UserProfile.objects.get_or_create(user=u)[0])