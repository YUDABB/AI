from django.shortcuts import render
from iot.models import professor_tables
from iot.models import student_tables
from iot.models import check_times
from iot.models import subject_tables
import time
import datetime


#from .forms import StudentsForm
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

def index(request, u_id):
    s_check = subject_tables.objects.all()
    s_count = 0
    for s in s_check:
        if u_id == s.professor_id_id:
            s_count += 1
    return render(request, 'p_ck/index.html', {'s_check':s_check, 's_count':s_count})


def detail(request, q_id):
    q_data = get_object_or_404(subject_tables, pk=q_id)
    p_check = professor_tables.objects.all()
    t_check = check_times.objects.all()
    s_check = student_tables.objects.all()

    times = datetime.datetime.now()
    ct1 = datetime.datetime.strftime(times, '%Y-%m-%d %H')

    d_c = ''
    # 총 출석 현황
    for i in t_check:
        for s in s_check:
            if i.face_id == s.student_id_id and i.subject_id == q_data.subject_id:

                    if i.pfr == 2:
                        s.p_c += 1
                    elif i.pfr == 1:
                        s.r_c += 1
                    else:
                        s.f_c += 1

    # 오늘의 출석 현황
    for i in t_check:
        for s in s_check:
            if i.face_id == s.student_id_id and i.subject_id == q_data.subject_id :
                ct2 = datetime.datetime.strftime(i.c_date, '%Y-%m-%d %H')
                ct2_m = datetime.datetime.strftime(i.c_date, '%M')
                if ct1 == ct2 and int(ct2_m)<= 15:
                        d_c = '출석'
                else:
                        d_c = '결석'



    context = {'t_check': t_check, 's_check': s_check,'q_data': q_data, 'p_check':p_check,'d_c': d_c}
    return render(request, 'p_ck/detail.html', context)

def up(request,q_id):
    q_data = get_object_or_404(student_tables,pk=q_id)
    subj = subject_tables.objects.all()

    context = {'subj':subj, 'u_id':q_id}
    return render(request,'p_ck/up.html',context)