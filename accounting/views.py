from rest_framework import viewsets
from accounting.models import User
from .models import Business, Course, Parent, Child, CourseEnrollment, Payment, Teacher, Salary, Expense, Account
from .serializers import BusinessSerializer, CourseSerializer, ParentSerializer, ChildSerializer, \
    CourseEnrollmentSerializer, PaymentSerializer, TeacherSerializer, SalarySerializer, ExpenseSerializer, AccountSerializer,UserSerializer

from .permissions import IsBusinessAdmin
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=(permissions.IsAuthenticated,IsBusinessAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes=(permissions.IsAuthenticated,IsBusinessAdmin,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class CourseEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
