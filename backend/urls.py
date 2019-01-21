from django.urls import path

from . import views

app_name = 'messageBox'
urlpatterns = [
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login, name='login'),
    path('user/getUserInfo/', views.get_user_info, name='get_user_info'),
    path('question/getQuestionList/', views.get_question_list, name='get_question_list'),
    path('question/AskQuestion/', views.ask_question, name='ask_question'),
    path('question/AnswerQuestion/', views.answer_question, name='answer_question'),
]
