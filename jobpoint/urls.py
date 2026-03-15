
from django.contrib import admin
from django.urls import path, include   # ✅ include add karo
from jobs.views import home
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('accounts/', include('accounts.urls')),

    # Jobs app
    path('jobs/', include('jobs.urls')),  
    
    
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
