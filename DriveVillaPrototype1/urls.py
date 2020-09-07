"""DriveVillaPrototype1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from users.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path("accounts/register/", RegistrationView.as_view(form_class=CustomUserForm,
                                                        success_url="/accounts/login/"), name="django_registration_register"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('DriveVilla.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
