from django.core.checks import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from common import models
from .models import Question
from .forms import QuestionForm
from django.utils import timezone
# Create your views here.

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw','')
    so = request.GET.get('so','recent')
    #정렬



    #조회
    #q_list = Question.objects.order_by('-create_date')
    q_list = Question.objects.order_by('-create_date')

    if kw:
        q_list =q_list.filter(
            Q(subject__icontains=kw)|
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()

    paginator = Paginator(q_list,10)
    page_obj = paginator.get_page(page)
    context = {'q_list':page_obj,'page':page,'kw':kw,'so':so}
    return render(request,'pybo/index.html',context)


def detail(request,q_id):
    q_data = get_object_or_404(Question,pk=q_id)
    #q_data = Question.objects.get(id=q_id)
    context = {'q_data':q_data}
    return render(request,'pybo/detail.html',context)


@login_required(login_url='common:login')
def a_register(request,q_id):
    #q.author = request.user
    q_data = get_object_or_404(Question,pk=q_id)
    q_data.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
    return redirect('pybo:detail',q_id=q_data.id)


@login_required(login_url='common:login')
def q_register(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.author = request.user
            q.create_date=timezone.now()
            q.save()
            return redirect('pybo:index')
    else :
        form = QuestionForm()
    return render(request,'pybo/q_register.html',{'form':form})

def up(request,q_id):
    return render(request,'pybo/up.html')

def delete(request,q_id):
    q = get_object_or_404(Question,pk=q_id)
    if request.user != q.author:
        messages.error(request,'삭제권한이 없습니다')
        return redirect('pybo:detail',q_id=q_id)
    q.delete()
    return redirect('pybo:index')
