from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from .models import Question
from .models import Choice


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[0:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    # context = {
      #  'question': Question.objects.filter(pk=request.GET['question_id']),
       # 'error_message': error_message
    # }
    # return render(request, 'polls/detail.html', context=context)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_id)
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "you didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
