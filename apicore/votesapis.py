from .models import Question, Choice

from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer, PollQuestionSerializer
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
import json
#Создание вопросов для опросов
#decorators enable use to work with json
csrf_exempt
@api_view(['GET', 'POST'])
def question_view(request):
    if request.method == 'GET':
        questions =  Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
        
        return HttpResponse(json.dumps(questions), content_type='application/json')
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            # return Response("Вопрос создан", status=status.HTTP_201_CREATED)
            return Response(QuestionSerializer(question).data, status=status.HTTP_201_CREATED)
        
    
 #Getting the question details
 #Получение вопроса для опроса
@api_view(['GET', 'PATCH', 'DELETE'])  
def poll_question_details(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(QuestionSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         question.delete()
         return Response("Вопрос удален",status=status.HTTP_204_NO_CONTENT)
     
#Размещение вариантов ответа на вопрос
@api_view(['POST'])
def choice_details(request, pk):
    question = Question.objects.get(pk=pk)
    # question = get_object_or_404(Question, pk=pk)
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        poll_question_choice = serializer.save(poll_question=question)
        return Response(ChoiceSerializer(poll_question_choice).data, status=status.HTTP_201_CREATED)
    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
 #Обновление голосов по конкретному вопросу   
@api_view(['PATCH'])
def polls_voting(request, pk):
    question = Question.objects.get(pk=pk)
    serializer = VoteSerializer(data=request.data)
    if serializer.is_valid():
        poll_question_choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], poll_question=question)
        poll_question_choice.votes += 1
        poll_question_choice.save()
        return Response("Voted")
    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Получение результатов опросов
@api_view(['GET'])
def poll_question_results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    serializer = PollQuestionSerializer(question)
    return Response(serializer.data)
