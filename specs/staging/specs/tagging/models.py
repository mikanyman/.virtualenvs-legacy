from django.db import models

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'tagging_tag'

class Taggeditem(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.ForeignKey(TaggingTag)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.IntegerField()
    class Meta:
        db_table = u'tagging_taggeditem'
        
