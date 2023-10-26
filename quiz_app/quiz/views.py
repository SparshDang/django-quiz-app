from django.shortcuts import render

from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
    
class CreateQuizView(View):
    def get(self, request):
        return render(request, "create_quiz.html")
    
class TakeQuizView(View):
    def get(self, request):
        return render(request, "take_quiz.html")
class ResultView(View):
    def get(self, request):
        return render(request, "see_result.html")