from django.shortcuts import render
from .models import check_times
from .models import subject_tables
from .models import student_tables
from .models import professor_tables
from p_ck.views import detail
import datetime
from django.utils import timezone
def index(request):
    t_check = check_times.objects.all()
    s_check = student_tables.objects.all()
    subj = subject_tables.objects.all()
    p_check = professor_tables.objects.all()

    d_c = 0
    a = 0

    times = datetime.datetime.now()
    ct1 = datetime.datetime.strftime(times, '%Y-%m-%d %H')

    a=[]

    # 오늘의 출석 현황
    '''
    for i in t_check:
        for s in s_check:
            if i.face_id == s.student_id_id:
                ct2 = datetime.datetime.strftime(i.c_date, '%Y-%m-%d %H')
                ct2_m = datetime.datetime.strftime(i.c_date, '%M')
                if ct1 == ct2 and int(ct2_m) <= 10:
                    a.append(i.face_id)
        if a:
            for j in range(len(a)):
                ct2 = datetime.datetime.strftime(i.c_date, '%Y-%m-%d %H')
                ct2_m = datetime.datetime.strftime(i.c_date, '%M')
                if ct1 == ct2 and int(ct2_m) > 10:
                    d_c = 1
'''


    count = {'t_check': t_check, 'subj': subj, 's_check':s_check, 'p_check':p_check}
    return render(request,'iot/index.html',count)

