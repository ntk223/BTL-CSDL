from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    #ForeignKey is a relationship. It tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    #votes is an integer field. It stores a whole number.



