# specs/frontpg/models.py

from django.db import models
from django.utils.translation import ugettext as _

class Article(models.Model):
    headline = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    box = models.CharField(max_length=7, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.headline

    class Meta:
        ordering = ('headline',)
        verbose_name = _(u'kirjoitus')
        verbose_name_plural = _(u'Kirjoitukset')