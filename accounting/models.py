from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Business(models.Model):
    name = models.CharField(max_length=100)
    # Add other business-related fields as needed

    def __str__(self):
        return self.name

class BusinessUser(models.Model):
    BUSINESS_ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('contributor', 'Contributor'),
        ('regular', 'Regular'),
    ]

    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=BUSINESS_ROLE_CHOICES)

    class Meta:
        unique_together = ['business', 'user']

class Course(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Add other course-related fields as needed

    def __str__(self):
        return self.name


class Parent(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other parent-related fields as needed

    def __str__(self):
        return self.user.username


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    # Add other child-related fields as needed

    def __str__(self):
        return self.name


class CourseEnrollment(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Add other enrollment-related fields as needed

    def __str__(self):
        return f"{self.child.name} - {self.course.name}"


class Payment(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Add other payment-related fields as needed

    def __str__(self):
        return f"{self.child.name} - {self.amount}"


class Teacher(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other teacher-related fields as needed

    def __str__(self):
        return self.user.username


class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Add other salary-related fields as needed

    def __str__(self):
        return f"{self.teacher.user.username} - {self.amount}"


class Expense(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Add other expense-related fields as needed

    def __str__(self):
        return self.description


class Account(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Add other account-related fields as needed

    def __str__(self):
        return self.name
