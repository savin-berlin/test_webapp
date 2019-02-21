# team_manager/urls.py
from django.conf.urls import url
from team_manager import views
from django.urls import path, include
from .views import (
	contact_edit_view,deleted_contact_view,contact_datails_view,unsecure_delete_contact_view,
	RESTAPI_ListCreateContactView,RESTAPI_ContactDetailView)



urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), 
    url(r'^contacts/$', views.ContactsView.as_view(), name="contacts_overview"),
	url(r'^create/$', views.contact_create_view,name="create_contact"), 
	path(r"contact/<int:contact_id>/", contact_datails_view, name="contact_datails"),
	path(r"contact/edit-contact/<int:contact_id>/", contact_edit_view, name="edit_contact"),
	path(r'contact/delete-contact/<int:contact_id>/', deleted_contact_view, name='deleted_view'),
	path(r'contact/unsecure_delete-contact/<int:contact_id>/', unsecure_delete_contact_view, name='unsecure_deleted_view'),
	url(r'^contact/(?P<contact_id>\d+)/$', contact_datails_view, name="contact_datails_2"),
	path('rest_api/contacts/', RESTAPI_ListCreateContactView.as_view(), name="restapi_contacts_list_and_create"),
	path(r'rest_api/contacts/<int:pk>/', RESTAPI_ContactDetailView.as_view(), name="restapi_contact_details"),
	
	#url(r'user/edit/(?P<UserID>\d+)$', 'VMS.views.update_or_edit_user_profile', name='user-edit'),
    
    
]