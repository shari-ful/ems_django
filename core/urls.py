
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', include('hrms.urls.home')),
    path('admin/', admin.site.urls),
]
