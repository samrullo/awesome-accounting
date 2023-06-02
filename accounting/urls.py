from django.urls import path, include
from rest_framework import routers
from .views import BusinessViewSet, CourseViewSet, ParentViewSet, ChildViewSet, CourseEnrollmentViewSet, \
    PaymentViewSet, TeacherViewSet, SalaryViewSet, ExpenseViewSet, AccountViewSet,UserViewSet

router = routers.DefaultRouter()
router.register('businesses', BusinessViewSet)
router.register('courses', CourseViewSet)
router.register('parents', ParentViewSet)
router.register('children', ChildViewSet)
router.register('enrollments', CourseEnrollmentViewSet)
router.register('payments', PaymentViewSet)
router.register('teachers', TeacherViewSet)
router.register('salaries', SalaryViewSet)
router.register('expenses', ExpenseViewSet)
router.register('accounts', AccountViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    # Your other URL patterns
    path('v1/', include(router.urls)),
]
