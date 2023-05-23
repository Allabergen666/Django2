from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    # list_display принисает tuple or list, Показывает по столбцам
    list_display = ['full_name','course','group','faculty']
    # list_filter сортировать по курс, группа, факултатив
    list_filter = ['course', 'group', 'faculty']
    #  search_fields Поиск 
    search_fields = ['firstname', 'lastname','course','group','faculty']
    #  list_editable изменить
    list_editable = ['course','group']
    # # ordering для сортировки
    # ordering = ['firstname', 'lastname']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name','subjectname','lengthofservice']
    # list_filter сортировать по курс, группа, факултатив
    list_filter = ['subjectname','lengthofservice']
    #  search_fields Поиск 
    search_fields = ['firstname', 'lastname','subjectname','lengthofservice']
    #  list_editable изменить
    list_editable = ['subjectname','lengthofservice']
    # # ordering для сортировки
    # ordering = ['firstname', 'lastname']


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)

