from django.urls import path, include
from rest_framework import routers
from .views import BusinessViewSet, CourseViewSet, CourseTeacherViewSet, ParentViewSet, ChildViewSet, \
    CourseEnrollmentViewSet, \
    CoursePaymentViewSet, TeacherViewSet, SalaryViewSet, ExpenseViewSet, AccountViewSet, UserViewSet, \
    BusinessUserViewSet
from .views import UserDetails

router = routers.DefaultRouter()
router.register('businesses', BusinessViewSet)
router.register('business-users', BusinessUserViewSet)
router.register('parents', ParentViewSet)
router.register('children', ChildViewSet)
router.register('teachers', TeacherViewSet)
router.register('courses', CourseViewSet)
router.register('course-teachers', CourseTeacherViewSet)
router.register('enrollments', CourseEnrollmentViewSet)
router.register('course-payments', CoursePaymentViewSet)
router.register('salaries', SalaryViewSet)
router.register('expenses', ExpenseViewSet)
router.register('accounts', AccountViewSet)
router.register('users', UserViewSet)

from .views import BusinessUserViewSet

router.register(r'<int:business_id>/users',BusinessUserViewSet,basename='user')
urlpatterns = [
    # Your other URL patterns
    path('v1/', include(router.urls)),
    path('v1/user-detail/',UserDetails.as_view())

]
