from django.db import models
from django.contrib.auth.models import User
from filebrowser.fields import FileBrowseField

class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True, null=True)
    document = FileBrowseField("PDF", max_length=200, directory="documents/", extensions=[".pdf",".doc",".odt"], blank=True, null=True)
    html = FileBrowseField("HTML", max_length=200, directory="html/", extensions=[".html"], blank=True, null=True)

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        #return "/some/url/%i/" % self.id
        return '/rockart/research/lhtml/saraakallio_html/skallio1.html'
    