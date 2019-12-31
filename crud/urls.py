"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
import crudApp.views
import accounts.views
import portfolio.views

from django.conf import settings
from django.conf.urls.static import static
# media 사용시 필수적으로 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudApp.views.index, name="index"),
    path('crudApp/', include('crudApp.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# media 사용시 필수적으로 추가