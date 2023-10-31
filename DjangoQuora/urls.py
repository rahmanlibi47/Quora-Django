from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('homepage.urls')),
    path('qna/', include('qna.urls', namespace='qna')),
]
