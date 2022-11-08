from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('add/', views.UserCreateView.as_view(), name='user_add'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
]
