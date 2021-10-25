
from django.contrib import admin
from django.urls import path, include

from apicore import votesapis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', votesapis.question_view, name='question_view'),
    path('questions/<int:pk>/', votesapis.poll_question_details),
    path('questions/<int:pk>/choices/',
         votesapis.choice_details, name='choice_details'),
    path('questions/<int:pk>/vote/', votesapis.polls_voting, name='polls_voting'),
    path('questions/<int:pk>/results/',
         votesapis.poll_question_results, name='poll_question_results')

]
