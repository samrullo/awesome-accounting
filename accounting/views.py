from rest_framework import viewsets
from accounting.models import User
from .models import Business, Course, CourseTeacher, Parent, Child, CourseEnrollment, CoursePayment, Teacher, Salary, \
    Expense, Account
from .serializers import BusinessSerializer, CourseSerializer, CourseTeacherSerializer, ParentSerializer, \
    ChildSerializer, \
    CourseEnrollmentSerializer, PaymentSerializer, TeacherSerializer, SalarySerializer, ExpenseSerializer, \
    AccountSerializer, UserSerializer

from .permissions import IsBusinessAdmin,TeacherAccessPermission
from rest_framework import permissions

from .models import BusinessUser
from .serializers import BusinessUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsBusinessAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ModifiedByMixin:
    def perform_create(self, serializer):
        serializer.save(modified_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class BusinessViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class BusinessUserViewSet(ModifiedByMixin, viewsets.ModelViewSet):
    queryset = BusinessUser.objects.all()
    serializer_class = BusinessUserSerializer


class ParentViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,TeacherAccessPermission,IsBusinessAdmin)
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    
class ChildViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,TeacherAccessPermission,IsBusinessAdmin)
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    
class TeacherViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,TeacherAccessPermission)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    
class CourseViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsBusinessAdmin,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    
class CourseTeacherViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsBusinessAdmin,)
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer

    
class CourseEnrollmentViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer

    

class CoursePaymentViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    queryset = CoursePayment.objects.all()
    serializer_class = PaymentSerializer

    

class SalaryViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

    

class ExpenseViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    

class AccountViewSet(ModifiedByMixin,viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    
from rest_framework.generics import RetrieveAPIView
class UserDetails(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_object(self):
        return self.request.user
