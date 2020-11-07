from django.contrib import admin
from django.urls import path, include

from .views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('core/', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
