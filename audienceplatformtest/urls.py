"""audienceplatformtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from rest_framework_simplejwt import views as jwt_views

from audienceplatformtest import settings
from audienceplatformtest.views.registration import Registration
from audienceplatformtest.views.video import VideoListView, AdminVideoView, VideoView, CreateVideoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^register/?$', Registration.as_view()),
    url(r'^videos/?$', VideoListView.as_view()),
    url(r'^video/(?P<id>[0-9]+)/?$', VideoView.as_view()),
    url(r'^video/?$', CreateVideoView.as_view()),
    url(r'^video/admin/?$', AdminVideoView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
