from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Business, BusinessUser, Course, CourseTeacher, Parent, Child, CourseEnrollment, CoursePayment, \
    Teacher, Salary, Expense, \
    Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'


class BusinessUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUser
        fields = ['id', 'business', 'user', 'role']


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTeacher
        fields = '__all__'


class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePayment
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    user_id = serializers.IntegerField(source='user.id')



class BusinessUserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUser
        exclude = ['modified_by']


class ParentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        exclude = ['modified_by']


class ChildWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        exclude = ['modified_by']


class TeacherWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ['modified_by']


class CourseWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['modified_by']


class CourseTeacherWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTeacher
        exclude = ['modified_by']


class CourseEnrollmentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        exclude = ['modified_by']


class CoursePaymentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePayment
        exclude = ['modified_by']


class SalaryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        exclude = ['modified_by']


class ExpenseWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ['modified_by']


class AccountWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['modified_by']