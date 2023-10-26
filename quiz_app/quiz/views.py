from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site

from django.views import View
import json
import string
import random

from quiz.models import *

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "home.html")


class CreateQuizView(View):
    def get(self, request):
        return render(request, "create_quiz.html", {'created':False})

    def post(self, request):

        json_data = request.POST['data']
        password = request.POST['password']
        data = json.loads(json_data)
        quiz = self.__generate_quiz(password)
        self.__set_questions(quiz, data)
        url = get_current_site(request).domain + '/' + quiz.code
        return render(request, "create_quiz.html", {'created':True, 'code':quiz.code, 'url':url})


    def __generate_quiz(self, password):
        code = self.__generate_quiz_code()
        return Quiz.objects.create(code=code, password=password)

    def __generate_quiz_code(self):
        letters = string.ascii_lowercase + string.digits
        while True:
            code = ''.join(random.choices(letters, k=6))
            if code not in Quiz.objects.values_list('code'):
                break
        return code

    def __set_questions(self, quiz, data):
        for question_data in data:
            question = Question.objects.create(
                quiz=quiz, text=question_data['text'])
            for choice in question_data['options']:
                Choice.objects.create(
                    question=question, text=choice['text'], is_correct=choice['isCorrect'])


class TakeQuizView(View):
    def get(self, request, **kwargs):
        quizCode = kwargs['code']
        quiz = Quiz.objects.get(code=quizCode)
        return render(request, "take_quiz.html", {'quiz': quiz, 'is_taken':False})
    
    def post(self, request):
        data = json.loads(request.POST['form__data'])
        score = 0

        for question in data['questions']:
            question_instance = Question.objects.get( pk = int(question['question']))
            if question_instance.choices.get(is_correct=True).text == question.get('choice', None):
                score += 1

        quiz = Quiz.objects.get(pk=int(data['id']))
        Response.objects.create(quiz=quiz, score=score, name=data['name'])
        return render(request, "take_quiz.html", {'is_taken':True, 'score':score, 'total_questions' : len(data['questions'])})
        

class ResultView(View):
    def get(self, request):
        return render(request, "see_result.html", {'is_showing':False, 'has_errors':False})
    
    def post(self, request):
        data = request.POST
        try:
            quiz = get_object_or_404(Quiz, code=data['code'])
            if quiz.password == data['password']:
                responses = quiz.responses.all()
            else:
                raise ValueError("Password wrong")
            return render(request, "see_result.html", {'is_showing':True, "responses" : responses})
        except:
            return render(request, "see_result.html", {'is_showing':False, "has_errors" : True})
