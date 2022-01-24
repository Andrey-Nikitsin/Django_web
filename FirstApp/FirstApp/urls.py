from re import I
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from FirstApp.settings import BASE_DIR
from user.views import index
from django.conf import settings
# if settings.DEBUG:
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('user.urls')),
    path('andrey/', index ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
