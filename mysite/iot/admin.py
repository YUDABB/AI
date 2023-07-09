from django.contrib import admin

from .models import professor_tables
from .models import student_tables
from .models import subject_tables
from .models import check_times


admin.site.register(professor_tables)
admin.site.register(student_tables)
admin.site.register(subject_tables)
admin.site.register(check_times)