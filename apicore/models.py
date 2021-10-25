from django.db import models
import datetime
from django.utils import timezone

# Модели для опоросов
#Question model
class Question(models.Model):
    poll_question = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField('date published', default=timezone.now, blank=False)
    end_date = models.DateTimeField('end date', blank=False)

    def __str__(self):
        return self.poll_question
    
    def choices(self):
        if not hasattr(self, '_choices'):
            self._choices = self.choice_set.all()
        return self._choices

    # def published_not_longage(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.start_date <= now
#Choice Model

class Choice(models.Model):
    poll_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    poll_question_choice = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.poll_question_choice
