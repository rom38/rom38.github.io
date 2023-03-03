"""chat_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

from chat.views import (register_request, ShowProfilePageView,
                        start_page, UpdateProfilePageView,
                        CreateProfilePageView, RoomList, whoami_view,
                        UserList, RoomDetail)

# from

urlpatterns = [
    # path('', RedirectView.as_view(url='/chat/')),
    path('', start_page, name='start_page'),
    path('accounts/logout/', LogoutView.as_view(next_page='start_page'), name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', register_request, name="register"),
    path('accounts/whoami/', whoami_view),
    path('accounts/profile/<int:pk>/', ShowProfilePageView.as_view(), name="user_profile"),
    path('accounts/profile/<int:pk>/update/', UpdateProfilePageView.as_view(), name="user_profile_update"),
    path('accounts/profile/<int:pk>/create/', CreateProfilePageView.as_view(), name="user_profile_create"),
    path('room/<int:pk>/', RoomDetail.as_view(), name="room_detail"),
    path('room/list/', RoomList.as_view(), name="room_list"),
    path('user/list/', UserList.as_view(), name="user_list"),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
