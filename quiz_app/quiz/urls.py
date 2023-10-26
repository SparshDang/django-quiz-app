from django.urls import path

from quiz.views import *

urlpatterns = [
    path("", HomeView.as_view(), name='home' ),
    path("create", CreateQuizView.as_view(), name='create' ),
    path("take", TakeQuizView.as_view(), name='take' ),
    path("result", ResultView.as_view(), name='result' ),
]