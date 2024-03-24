from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Answers, Category
from BrainBusterApp.forms import CustomUserCreationForm
from django.urls import reverse
import random

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse(index))

def question(request):
    # redirect to homepage if category isn't set or is get request
    if request.method == 'GET' or not request.POST.get('category'):
        return redirect(index) 
    # question category
    selected_category = request.POST.get('category')

    # get already answered question
    if selected_category in request.session:
        answered_questions = request.session[selected_category]
    else:
        answered_questions = {}

    # handle user answer
    if request.POST.get('user_answer'):
        # get question, user answer and correct answer
        question = request.POST.get('question')
        question_id = Question.objects.filter(Question_Text = question)[0].Question_ID
        user_answer = request.POST.get('user_answer')
        correct_answer = Answers.objects.filter(Question = question_id, Is_Correct = True)[0].Answer
        is_correct = user_answer == correct_answer

        # mark question as anwered
        answered_questions[question_id] = is_correct
        request.session[selected_category] = answered_questions

        return render(
            request,
            'question.html', 
            {
                "question": question,
                "result": {"answer": correct_answer, "is_correct": is_correct},
                "category": selected_category
            }
        )
    
    # load question
    else:
        # get category id
        category_id = Category.objects.filter(Category = selected_category)[0].Category_ID
        
        # fetch questions that haven't been answered yet
        unanswered_questions = Question.objects.filter(Category = category_id).exclude(Question_ID__in = answered_questions.keys())
        
        # show score and update total score if all questions have been answered
        if not unanswered_questions:
            # reset answered questions
            del request.session[selected_category]

            # calculate score
            question_results = answered_questions.values()
            total = len(question_results)
            score = 0
            for result in question_results:
                score += result

            # add 10 points per correct answer to user score
            points = score * 10
            if "total_score" in request.session:
                request.session["total_score"] = request.session["total_score"] + points
            else:
                request.session["total_score"] = points

            return render(
            request, 
            'score.html', 
            {
                "score": score,
                "total": total,
                "user_points": request.session["total_score"]
            }
        )    

        # select random question and answers
        question = random.choice(unanswered_questions)
        answers = Answers.objects.filter(Question=question.Question_ID)

        return render(
            request, 
            'question.html', 
            {
                "question": question,
                "answers": answers,
                "category": selected_category
            }
        )

def login(request):
    return render(request, 'login.html')