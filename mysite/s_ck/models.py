from django.db import models
from django.contrib.auth.models import User

class CheckList(models.Model):
    prf = models.CharField(max_length=5)
    ctime = models.IntegerField(max_length=2)
    cdate = models.DateTimeField()
    s_id = models.ForeignKey(User, on_delete=models.CASCADE, null=0)

    def str(self):
        return self.prf