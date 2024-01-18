from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('account.urls')),
    path('dashboard/lead/', include('lead.urls')),
    path('dashboard/', include('dashboard.urls')),
]
