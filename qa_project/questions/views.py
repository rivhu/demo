from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    # Get all questions from the database
    questions = Question.objects.all()
    selected_question = None
    
    # Check if a specific question was clicked
    question_id = request.GET.get('id')
    if question_id:
        selected_question = get_object_or_404(Question, id=question_id)
        
    return render(request, 'index.html', {
        'questions': questions,
        'selected_question': selected_question
    })

# Create your views here.
