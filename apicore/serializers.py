from rest_framework import serializers
from .models import Question, Choice



    


class ChoiceSerializer(serializers.Serializer):
    poll_question_choice = serializers.CharField(max_length=255)
    poll_question_choice_id = serializers.IntegerField(read_only=True)
    def create(self, validated_data):
        return Choice.objects.create(**validated_data)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
#Choice Serializer

class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    poll_question = serializers.CharField(max_length=255)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    # published_not_longage = serializers.BooleanField(read_only=True)
    #Create new question

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    #Updating question
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    choices = ChoiceSerializer(many=True, read_only=True)

#Choice serializer after the polls
class ChoiceSerializerAfterVotes(ChoiceSerializer):
    votes = serializers.IntegerField(read_only=True)

#Results serializer
class PollQuestionSerializer(QuestionSerializer):
    choices = ChoiceSerializerAfterVotes(many=True, read_only=True)
   

    
