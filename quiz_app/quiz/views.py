from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

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
        return render(request, "create_quiz.html")

    def post(self, request):

        json_data = request.POST['data']
        password = request.POST['password']
        data = json.loads(json_data)
        quiz = self.__generate_quiz(password)
        self.__set_questions(quiz, data)
        return HttpResponseRedirect(reverse('home'))

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
    def get(self, request):
        return render(request, "take_quiz.html")


class ResultView(View):
    def get(self, request):
        return render(request, "see_result.html")
