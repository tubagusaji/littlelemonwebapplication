from django.urls import re_path, path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter(trailing_slash=False)
router.register(r'tables', views.BookingViewSet, basename='BookingViewSet')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('booking/', include(router.urls)),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]