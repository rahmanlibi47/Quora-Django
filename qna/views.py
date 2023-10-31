from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
from django.http import JsonResponse
from .models import Question, Like, Answer

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'question_detail.html', {'question': question})

def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user 
            question.save()
            return redirect('question_list') 
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form})



def provide_answer(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)  
            answer.question_id = question_id 
            answer.author = request.user 
            answer.save() 

            return redirect('qna:question_detail', question_id=question_id)
    else:
        form = AnswerForm()

    return render(request, 'answer_form.html', {'form': form, 'question_id': question_id})

@login_required
def like_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    user = request.user

    already_liked = Like.objects.filter(user=user, liked_question=question).exists()

    if already_liked:
        like = Like.objects.get(user=user, liked_question=question)
        like.delete()
        liked = False
    else:
        like = Like(user=user, liked_question=question)
        like.save()
        liked = True

    likes_count = question.like_set.count()

    return JsonResponse({'liked': liked, 'likes_count': likes_count})


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    user = request.user

    already_liked = Like.objects.filter(user=user, liked_answer=answer).exists()

    if already_liked:
        like = Like.objects.get(user=user, liked_answer=answer)
        like.delete()
        liked = False
    else:
        like = Like(user=user, liked_answer=answer)
        like.save()
        liked = True

    likes_count = answer.like_set.count()

    return JsonResponse({'liked': liked, 'likes_count': likes_count})