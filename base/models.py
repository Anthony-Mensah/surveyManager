from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
ANSWER_TYPE = (
    ('text', 'text'),
    ('number', 'number'),
    ('choice', 'multiple choice')
)

class Survey(models.Model):
    name = models.CharField(max_length=200)
    question = models.TextField()
    answer_type = models.CharField(max_length=15, choices=ANSWER_TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    # a slugfield cannot have space between them rather hyphen (-)
    def get_absolute_url(self):
        return reverse('base:answer', kwargs={'slug': self.slug})

    def __str__(self):
        return self.question

class SurveyAnswer(models.Model):
    answer = models.CharField(max_length=100)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer[:50]

class Choice(models.Model):
    name = models.CharField(max_length=20)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
