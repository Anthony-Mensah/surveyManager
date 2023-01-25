from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def list(request):
    surveys = Survey.objects.all()

    context = {
    'surveys':surveys,
    }
    return render(request, 'list.html', context)


def create(request):
    survey_form = SurveyForm()
    user = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        question = request.POST.get('question')
        answer_type = request.POST.get('answer_type')

        survey = Survey.objects.create(
        name = name,
        question = question,
        answer_type = answer_type,
        user = user,
        slug = name.replace(" ", "-")
        )
        survey.save()

        if answer_type == 'choice':
            return redirect('base:choice', survey.slug)
        else:
            return redirect('/')

    context = {
    'survey_form':survey_form
    }
    return render(request, 'create.html', context)

def edit(request, slug):
    survey = get_object_or_404(Survey, slug=slug)
    survey_form = SurveyForm(instance=survey)
    if request.method == 'POST':
        survey_form = SurveyForm(request.POST, instance=survey)
        if survey_form.is_valid():
            survey_form.save()
            return redirect('/')

    context = {
    'survey_form':survey_form
    }
    return render(request, 'edit.html', context)

def answer(request, slug):
    survey = get_object_or_404(Survey, slug=slug)
    choices = Choice.objects.filter(survey=survey)
    print('question: ', survey.answer_type)
    print('Choice: ', choices)

    if request.method == 'POST':
        answer = request.POST.get('answer')
        print('Answer: ', type(answer))

        survey_answer = SurveyAnswer.objects.create(
        answer = answer,
        survey = survey,
        )
        survey_answer.save()
        return redirect('/')

    context = {
    'survey':survey,
    'choices':choices
    }
    return render(request, 'answer.html', context)

def choice(request, slug):
    survey = get_object_or_404(Survey, slug=slug)

    if request.method == 'POST':
        choice = request.POST.get('choice')
        new_choice = Choice.objects.create(
        name = choice,
        survey = survey
        )
        new_choice.save()
        return redirect('base:choice', slug)

    return render(request, 'choice.html')
