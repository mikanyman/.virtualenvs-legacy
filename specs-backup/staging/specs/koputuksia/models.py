from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.title
    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __unicode__(self):
        return u'%s' % self.headline
    class Meta:
        ordering = ('headline',)
    class Admin:
        list_display = ('headline',)

class Category(models.Model):
    name = models.CharField(max_length=50)
    ordinal = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name
    class Meta:
        ordering = ('ordinal',)
    class Admin:
        list_display = ('name',)

class Issue(models.Model):
    name = models.CharField(max_length=10)
    ordinal = models.IntegerField(blank=True, null=True)
    current = models.BooleanField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name
    class Meta:
        ordering = ('ordinal',)
    class Admin:
        list_display = ('name', 'current',)

class Juttu(models.Model):
    issue = models.ForeignKey(Issue, to_field='name')
    pub_date = models.DateTimeField('date published')
    categorys = models.ManyToManyField(Category)
    slug = models.SlugField(unique_for_date='pub_date')
    byline = models.CharField("Esirivi", max_length=200, blank=True, null=True)
    headline = models.CharField("Otsikko", max_length=200)
    summary = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #db_table = 'koputuksia_juttu' # ennen oli 'juttu'
        #verbose_name_plural = 'jutut'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
    class Admin:
        list_display = ('pub_date', 'headline', 'author',)
    def __unicode__(self):
        return u'%s' % self.headline

    def get_absolute_url(self):
        # return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
        return "/sites/specs/koputuksia/%s/%s/" % (self.issue, self.id)
