from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import response
from django.template.loader import render_to_string

from .models import Question, Choice


# Create your views here.
@login_required()
def home(request):
    return render(request,'app1/home.html')

@login_required()
def test(request):
    return render(request,'app1/navbar.html')


@login_required
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "app1/index.html", context)


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return JsonResponse({"success": False, "error": "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()


        htmlContent = render_to_string('app1/result.html',{'question': question})
        return HttpResponse(htmlContent)


@login_required
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "app1/detail.html", {"question": question})

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "app1/result.html", {"question": question})
