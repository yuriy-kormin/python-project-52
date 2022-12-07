from django.urls import path
from .views import MarkCreateView, MarkListView, \
    MarkUpdateView, MarkDeleteView

urlpatterns = [
    path('', MarkListView.as_view(), name='mark_list'),
    path('create/', MarkCreateView.as_view(), name='mark_add'),
    path('<int:pk>/update/', MarkUpdateView.as_view(), name='mark_update'),
    path('<int:pk>/delete/', MarkDeleteView.as_view(), name='mark_delete'),
]
