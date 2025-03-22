
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home_view,name="home"),
    path("services/",views.Service_view,name="service"),
    path("contact/",views.Condact_view,name="contact"),
    path("about/",views.About_us_view,name="about"),
    path("gallery/",views.gallery,name="gallery"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
