
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from post.views import custom404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('post.urls')),
]
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404  = custom404