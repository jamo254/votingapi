from django.db import models
import datetime
from django.utils import timezone
# Модели для опоросов
class Question(models.Model):
    poll_question = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField('date published', blank=False)
    end_date = models.DateTimeField('end date', blank=True)
    
    def __str__(self):
        return self.poll_question
    
    def checking_publishing_date(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.start_date <= now

#Модель для Выбора
class Choice(models.Model):
    poll_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    poll_question_choice = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.poll_question_choice
    
    
