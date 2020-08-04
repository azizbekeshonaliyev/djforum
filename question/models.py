from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.forms import ModelForm

class Tag(models.Model):
    STATUES = (
        ('active', 'Active'),
        ('in_active', 'In active'),
    )
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=STATUES)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.name


class TagForm(ModelForm):
    class Meta:
        fields = ['name', 'status', 'pub_date']

class Question(models.Model):
    STATUES = (
        ('checking', 'Checking'),
        ('waiting', 'Waiting'),
        ('completed', 'Completed')
    )
    title = models.CharField(max_length=200)
    desc = HTMLField(default='')
    pub_date = models.DateTimeField(default=None, blank=True, null=True)
    tags  = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_count = models.IntegerField(default=0)
    viewed = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    unlike_count = models.IntegerField(default=0)
    status = models.CharField(max_length=100, choices=STATUES, default='checking')


