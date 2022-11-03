from django.urls import path
from .views import user_list

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', user_list),
]