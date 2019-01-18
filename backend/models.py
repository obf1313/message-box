from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    answer_date = models.DateTimeField('date answer')

    def __str__(self):
        return self.question_text
