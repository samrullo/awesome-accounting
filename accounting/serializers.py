from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Business, BusinessUser, Course, CourseTeacher, Parent, Child, CourseEnrollment, CoursePayment, \
    Teacher, Salary, Expense, \
    Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']

class BaseSerializer(serializers.ModelSerializer):
    def get_fields(self):
        fields = super().get_fields()
        if self.context['request'].method in ('POST', 'PUT', 'PATCH'):
            fields.pop('modified_by', None)
        return fields

class BusinessSerializer(BaseSerializer):
    class Meta:
        model = Business
        fields = '__all__'


class BusinessUserSerializer(BaseSerializer):
    class Meta:
        model = BusinessUser
        fields = ['id', 'business', 'user', 'role']


class ParentSerializer(BaseSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class ChildSerializer(BaseSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseTeacherSerializer(BaseSerializer):
    class Meta:
        model = CourseTeacher
        fields = '__all__'


class CourseEnrollmentSerializer(BaseSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'


class PaymentSerializer(BaseSerializer):
    class Meta:
        model = CoursePayment
        fields = '__all__'


class TeacherSerializer(BaseSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class SalarySerializer(BaseSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class ExpenseSerializer(BaseSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class AccountSerializer(BaseSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    user_id = serializers.IntegerField(source='user.id')


