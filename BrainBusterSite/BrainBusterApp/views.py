from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Answers, Category, Score
from BrainBusterApp.forms import CustomUserCreationForm
from django.urls import reverse
import random
from django.contrib.auth import login, get_user_model

def get_top_scores():
    User = get_user_model()
    scores = Score.objects.order_by('-Points')[:10]

    top_scores = []
    for score in scores:
        user_and_score = {
            "user": User.objects.filter(id=score.User_ID)[0].username,
            "score": score.Points
        }
        top_scores.append(user_and_score)
    return top_scores


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
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse(index))
        # stay on page if registration not successful
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm, "message": "Passwort ist nicht sicher genug"}
        )

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

            # user info
            user = request.user
            current_user_score = Score.objects.filter(User_ID = user.id)[0]
            # add 10 points per correct answer to user score
            points = score * 10
            current_user_score.Points += points
            current_user_score.save()

            # get top ten ranking
            rankings = get_top_scores()

            return render(
            request, 
            'score.html', 
            {
                "score": score,
                "total": total,
                "user_points": current_user_score.Points,
                "rankings": rankings
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

def rankings(request):
    rankings = get_top_scores()
    return render(
        request, 
        'rankings.html',
        {
            "rankings": rankings
        }
    )