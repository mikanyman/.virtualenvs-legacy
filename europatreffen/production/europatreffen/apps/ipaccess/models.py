from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class IPAccess(models.Model):
    ip = models.IPAddressField(_('ip'), unique=True, db_index=True)
    user = models.ForeignKey(User, verbose_name=_('user that authenticates'))

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = _('IP Access')
        verbose_name_plural = _('IP Accesses')