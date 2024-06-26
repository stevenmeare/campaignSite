from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.

# Shows a list of polls
def index(request):
    '''
    This function returns a list of the latest 5 questions.
    The questions are ordered by publication date.

    :param request: The request object.
    :type request: HttpRequest

    :return: A list of the latest 5 questions.
    :rtype: HttpResponse

    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

# Shows question template
def detail(request, question_id):
    '''
    This function returns a question template.
    
    :param request: The request object.
    :type request: HttpRequest
    
    :param question_id: The id of the question.
    :type question_id: int

    :return: A question template.
    :rtype: HttpResponse
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# Shows poll result
def results(request, question_id):
    '''
    This function returns the results of a poll.

    :param request: The request object.
    :type request: HttpRequest

    :param question_id: The id of the question.
    :type question_id: int

    :return: The results of a poll.
    :rtype: HttpResponse
    '''

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Posts form choice, or returns error
def vote(request, question_id):
    '''
    This function allows users to vote on a poll.
    
    :param request: The request object.
    :type request: HttpRequest
    
    :param question_id: The id of the question.
    :type question_id: int

    :exception: Choice.DoesNotExist: If the choice does not exist.
    
    :return: The results of a poll.
    :rtype: HttpResponseRedirect
    '''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )
    

    