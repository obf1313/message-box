from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

    def user_vo(self):
        return {'id': self.id, 'username': self.username}


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200, blank=True, null=True)
    # date published 备注名
    pub_date = models.DateTimeField('date published')
    answer_date = models.DateTimeField('date answer', blank=True, null=True)

    def __str__(self):
        return self.question_text

    def question_vo(self):
        return { 'id': self.id, 'user_id': self.user_id, 'question_text': self.question_text, 'answer_text': self.answer_text, 'pub_date': self.pub_date, 'answer_date': self.answer_date }


