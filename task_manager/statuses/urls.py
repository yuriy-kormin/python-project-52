from django.urls import path
from .views import StatusCreateView, StatusListView, \
    StatusUpdateView, StatusDeleteView

urlpatterns = [
    path('', StatusListView.as_view(), name='status_list'),
    path('create/', StatusCreateView.as_view(), name='status_add'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]
