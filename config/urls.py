from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import landing_page,allreview_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing_page,name='landing_page'),
    path('allreview/',allreview_page,name='allreview'),
    path('users/',include('users.urls')),
    path('api/',include('api.urls')),
    path('books/',include('books.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
