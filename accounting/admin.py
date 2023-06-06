from django.contrib import admin
from .models import Business, BusinessUser, Course, Parent, Child, CourseEnrollment, CoursePayment, Teacher, Salary, Expense, Account

admin.site.register(Business)
admin.site.register(BusinessUser)
admin.site.register(Course)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(CourseEnrollment)
admin.site.register(CoursePayment)
admin.site.register(Teacher)
admin.site.register(Salary)
admin.site.register(Expense)
admin.site.register(Account)
