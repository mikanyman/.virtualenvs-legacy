# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

""" http://feedfrog.net/blog/2008/nov/15/generic-url-base-view-count-django/ """
""" http://feedfrog.net/blog/2008/oct/7/getting-know-your-client-using-django-middleware/ """

class PathCount(models.Model):
    path = models.CharField(max_length=250, null=True, blank=True, verbose_name=_(u'Sivut joita ei lasketa'))

    def __unicode__(self):
        return '%s' % self.path
    class Meta:
        verbose_name = _(u'poikkeus')
        verbose_name_plural = _(u'Poikkeukset')

class ViewCount(models.Model):
    url = models.CharField(unique=True, max_length=1000, verbose_name=_(u'Sivun osoite'))
    count = models.IntegerField(default=1, verbose_name=_(u'Latausten määrä'))

    def __unicode__(self):
        return "%s-%s" % (self.url, self.count)
    class Meta:
        verbose_name = _(u'laskuri')
        verbose_name_plural = _(u'Laskurit')
