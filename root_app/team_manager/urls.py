# team_manager/urls.py
from django.conf.urls import url
from team_manager import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^contacts_overview/$', views.ContactsView.as_view()), # Add this /about/ route
]