
from django.contrib import admin
from django.urls import path,include

from apicore import votesapis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/', votesapis.question_view, name='question_view')
    
]
