"""root_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include,re_path
from team_manager.admin import user_admin_site
#from team_manager.admin import user_admin_site
#from team_manager.views import RESTAPI_ListContactsView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('team_manager.urls')),
    url('useradmin',user_admin_site.urls),
    #re_path('contacts_api/(?P<version>(v1|v2))/', RESTAPI_ListContactsView.as_view())

]
