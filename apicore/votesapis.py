from .models import Question

from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

#Создание вопросов для опросов
@csrf_exempt
def question_view(request):
    if request.method == 'GET':
        return HttpResponse("Вопрос не создан")
    elif request.method == 'POST':
        poll_question = request.POST['poll_question']
        title = request.POST['title']
        start_date = datetime.strptime(request.POST['start_date'],'%Y-%m-%d')
        Question.objects.create(poll_question=poll_question,title=title, start_date=start_date)
        return HttpResponse("Вопрос создан")
    else:
        return "Попробуйте снова"
    
