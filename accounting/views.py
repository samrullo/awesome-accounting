from rest_framework import viewsets
from accounting.models import User
from .models import Business, Course, CourseTeacher, Parent, Child, CourseEnrollment, CoursePayment, Teacher, Salary, \
    Expense, Account
from .serializers import BusinessSerializer, CourseSerializer, CourseTeacherSerializer, ParentSerializer, \
    ChildSerializer, \
    CourseEnrollmentSerializer, PaymentSerializer, TeacherSerializer, SalarySerializer, ExpenseSerializer, \
    AccountSerializer, UserSerializer

from .serializers import  (BusinessUserWriteSerializer,
    ParentWriteSerializer,
    ChildWriteSerializer,
    TeacherWriteSerializer,
    CourseWriteSerializer,
    CourseTeacherWriteSerializer,
    CourseEnrollmentWriteSerializer,
    CoursePaymentWriteSerializer,
    SalaryWriteSerializer,
    ExpenseWriteSerializer,
    AccountWriteSerializer)

from .permissions import IsBusinessAdmin,TeacherAccessPermission
from rest_framework import permissions

from .models import BusinessUser
from .serializers import BusinessUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsBusinessAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class BusinessUserViewSet(viewsets.ModelViewSet):
    queryset = BusinessUser.objects.all()
    serializer_class = BusinessUserSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BusinessUserWriteSerializer
        return BusinessUserSerializer

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class ParentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,TeacherAccessPermission,IsBusinessAdmin)
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ParentWriteSerializer
        return ParentSerializer
    
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class ChildViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,TeacherAccessPermission,IsBusinessAdmin)
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ChildWriteSerializer
        return ChildSerializer
    
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,TeacherAccessPermission)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TeacherWriteSerializer
        return TeacherSerializer

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsBusinessAdmin,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CourseWriteSerializer
        return CourseSerializer

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(modified_by=self.request.user)

class CourseTeacherViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsBusinessAdmin,)
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CourseTeacherWriteSerializer
        return CourseTeacherSerializer
    
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class CourseEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CourseEnrollmentWriteSerializer
        return CourseEnrollmentSerializer
    
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class CoursePaymentViewSet(viewsets.ModelViewSet):
    queryset = CoursePayment.objects.all()
    serializer_class = PaymentSerializer

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CoursePaymentWriteSerializer
        return CoursePaymentWriteSerializer
    
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return SalaryWriteSerializer
        return SalarySerializer
    
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return ExpenseWriteSerializer
        return ExpenseSerializer
    
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return AccountWriteSerializer
        return AccountSerializer
    
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

from rest_framework.generics import RetrieveAPIView
class UserDetails(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_object(self):
        return self.request.user
