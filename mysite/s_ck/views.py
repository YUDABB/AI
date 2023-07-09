from django.shortcuts import render
from iot.models import student_tables
from iot.models import check_times
from iot.models import subject_tables

# Create your views here.
def index(request):
    t_check = check_times.objects.all()
    subj = subject_tables.objects.all()

    count = {'t_check': t_check, 'subj':subj }
    return render(request, 's_ck/index.html',count )
