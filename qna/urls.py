from django.urls import path
from . import views

app_name = 'qna' 

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('post_question/', views.post_question, name='post_question'),
    path('provide_answer/<int:question_id>/', views.provide_answer, name='provide_answer'),
    path('like/<int:question_id>/', views.like_question, name='like_question'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),


]
