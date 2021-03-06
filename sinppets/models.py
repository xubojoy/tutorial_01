from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]

LANGUANGE_CHOICES = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item,item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUANGE_CHOICES,default='python',max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,default='friendly',max_length=100)
    owner = models.ForeignKey('auth.User', related_name="snippets")

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.owner

    def __repr__(self):
        return self.owner