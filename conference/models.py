from django.db import models

TYPE = (("talk", "Talk"), 
        ("tutorial", "Tutorial"),
        ("pk", "PK"))
          
class TalkTutorial(models.Model):
    speaker = models.CharField(max_length=32)
    title = models.CharField(max_length=512)
    abstract = models.CharField(max_length=1024)
    slides = models.CharField(max_length=64)
    video = models.CharField(max_length=512)
    type = models.CharField(max_length=10, choices=TYPE)
    def __unicode__(self):
        title = self.title
        return '%s'%(title)

    
