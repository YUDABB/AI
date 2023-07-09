from django.db import models
from django.contrib.auth.models import User

class subject_tables(models.Model):
    subject_id = models.IntegerField()
    subject_name = models.CharField(max_length=200)
    professor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_time = models.IntegerField()

    def __str__(self):
        return self.subject_name


class professor_tables(models.Model):
    professor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    professor_name = models.CharField(max_length=200)
    subject_id = models.ForeignKey(subject_tables,on_delete=models.CASCADE)

    def __str__(self):
        return self.professor_name

class student_tables(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    subject_id = models.ForeignKey(subject_tables,on_delete=models.CASCADE)
    student_count = models.IntegerField()
    p_c = models.IntegerField(default=0)
    f_c = models.IntegerField(default=0)
    r_c = models.IntegerField(default=0)


    def __str__(self):
        return self.student_name

class check_times(models.Model):
    subject_id = models.IntegerField()
    face_id = models.IntegerField()
    pfr =  models.IntegerField()
    c_date = models.DateTimeField()
    out_times = models.IntegerField()
