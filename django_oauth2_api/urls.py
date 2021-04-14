"""django_oauth2_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from dj_rest_auth.views import PasswordResetConfirmView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # django-rest-framework
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')), # django-rest-auth
    path('api/dj-rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        # api/dj-rest-auth/login/
        # api/dj-rest-auth/logout/
        # api/dj-rest-auth/password/reset/
        # api/dj-rest-auth/password/reset/confirm/
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # dj-rest_auth.registration
    

    path('', include('core.urls', namespace='core')),
    path('todo/', include('todo.urls', namespace='todo')),
    path('api/', include('api.urls', namespace='api')),
    path('blog/', include('blogapi.urls', namespace='blog')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""

https://jamshid98.pythonanywhere.com/blog/          get
https://jamshid98.pythonanywhere.com/blog/<id>/     get

https://jamshid98.pythonanywhere.com/api/dj-rest-auth/login/
https://jamshid98.pythonanywhere.com/api/dj-rest-auth/logout/
https://jamshid98.pythonanywhere.com/api/dj-rest-auth/password/reset/
https://jamshid98.pythonanywhere.com/api/dj-rest-auth/password/reset/confirm/
https://jamshid98.pythonanywhere.com/api/dj-rest-auth/registration/

"""