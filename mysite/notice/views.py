from django.core.checks import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'notice/index.html')

'''

from .models import Question
from .forms import QuestionForm
from django.utils import timezone
# Create your views here.

def index(request):
    q_list = Question.objects.order_by('-create_date')
    context = {'q_list':q_list}
    return render(request,'notice/index.html',context)

def detail(request,q_id):
    q_data = get_object_or_404(Question,pk=q_id)
    #q_data = Question.objects.get(id=q_id)
    context = {'q_data':q_data}
    return render(request,'notice/detail.html',context)


@login_required(login_url='common:login')
def a_register(request,q_id):
    #q.author = request.user
    q_data = get_object_or_404(Question,pk=q_id)
    q_data.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
    return redirect('notice:detail',q_id=q_data.id)


@login_required(login_url='common:login')
def q_register(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.author = request.user
            q.create_date=timezone.now()
            q.save()
            return redirect('notice:index')
    else :
        form = QuestionForm()
    return render(request,'notice/q_register.html',{'form':form})

def up(request,q_id):
    return render(request,'notice/up.html')

def delete(request,q_id):
    q = get_object_or_404(Question,pk=q_id)
    if request.user != q.author:
        messages.error(request,'삭제권한이 없습니다')
        return redirect('notice:detail',q_id=q_id)
    q.delete()
    return redirect('notice:index')
    '''
