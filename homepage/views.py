from django.shortcuts import render
from qna.models import Question

def homepage(request):
    questions = Question.objects.all()
    return render(request, 'homepage.html', {'questions': questions})
