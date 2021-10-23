from .models import Question

from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

#Создание вопросов для опросов
csrf_exempt
@api_view(['GET', 'POST'])
def question_view(request):
    if request.method == 'GET':
        return HttpResponse("Вопрос не создан")
    elif request.method == 'POST':
        poll_question = request.data['poll_question']
        title = request.data['title']
        start_date = datetime.strptime(request.data['start_date'],'%Y-%m-%d')
        Question.objects.create(poll_question=poll_question,title=title, start_date=start_date)
        return HttpResponse("Вопрос создан", status=201)
    else:
        return "Попробуйте снова"
    
