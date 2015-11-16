import datetime
from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently ?'


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.choice_text


class Subscriber(models.Model):
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=63)
    lastname = models.CharField(max_length=63)
    date_added = models.DateTimeField('date_added')

class List(models.Model):
    name = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(Subscriber)
    date_created = models.DateTimeField('date_created')

