from django.db import models
from django.utils.translation import ugettext as _

class Lehti(models.Model):
    numero = models.CharField(max_length=3)
    vuosi = models.DateField()

    def __unicode__(self):
        return u'%s-&s' % (self.label, self.label)
    
    class Meta:
        #ordering = ['order'] -- order -kenttaa ei ole...
        verbose_name_plural = _(u'Lehdet')
        verbose_name = _(u'Lehti')