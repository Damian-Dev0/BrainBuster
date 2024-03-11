from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Question, Answers

# Create your tests here.
class TestModels(TestCase):
    
    def test_question_str_return_type(self):
        question = Question.objects.create(Question_Text="Testfrage")
        self.assertEqual(type(question.__str__()), str)
    
    def test_question_str_value(self):
        question = Question.objects.create(Question_Text="Testfrage")
        self.assertEqual(question.__str__(), question.Question_Text)
        
    def test_question_str_with_umlauts(self):
        question = Question.objects.create(Question_Text="Anzahl der Länder in Europa?")
        self.assertEqual(question.__str__(), question.Question_Text)

    # Test the str-Method in models.py
    # 
    # def test_question_str_with_empty_text(self):  
    #     question = Question.objects.create(Question_Text="")
    #     self.assertEqual(question.__str__(), "")
    
    def test_answer_creation(self):
        question = Question.objects.create(Question_Text="Testfrage")
        answer = Answers.objects.create(Question=question, Answer="Antwort A", Is_Correct=False)
        self.assertEqual(answer.Question, question)
        self.assertEqual(answer.Answer, "Antwort A")
        self.assertFalse(answer.Is_Correct)
 
    def test_valid_answer_without_is_correct(self):
        question = Question.objects.create(Question_Text="Testfrage")
        answer = Answers.objects.create(Question=question, Answer="Antwort", Is_Correct=False)
        self.assertEqual(answer.Is_Correct, False)
        answer.save()  # Should not raise any errors
    
    def test_valid_answer_with_is_correct(self):
        question = Question.objects.create(Question_Text="Testfrage")
        answer = Answers.objects.create(Question=question, Answer="Antwort", Is_Correct=True)
        self.assertEqual(answer.Is_Correct, True)
        answer.save()  # Should not raise any errors
    
    def test_multiple_answers(self):
        question = Question.objects.create(Question_Text="Testfrage")
        answer1 = Answers.objects.create(Question=question, Answer="Antwort A", Is_Correct=True)
        answer2 = Answers.objects.create(Question=question, Answer="Antwort B", Is_Correct=False)
        self.assertTrue(answer1.Is_Correct)
        self.assertFalse(answer2.Is_Correct)
        number_of_answers=[answer1, answer2]
        self.assertEqual(number_of_answers.__len__(), 2)  # Access related objects using manager