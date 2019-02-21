 # team_manager/views.py
from django.http import Http404
from django.shortcuts import render, get_object_or_404 
from django.views.generic import TemplateView
from django.utils import timezone
from team_manager.db.db_handler import connect,default_db_name,default_table_name,db_handler,getTable
from team_manager.helpers.debugger import p
from django_tables2 import RequestConfig
from django.contrib import messages
from django.core import serializers
from rest_framework.views import status
from .forms import ContactForm,RawContactForm
from .serializers import ContactsSerializer
from .models import Contact
from .tables import ContactTable
import django 
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from .decorators import validate_request_contact_data

######### REST API VIEWS ############

#class RESTAPI_ListContactsView(generics.ListAPIView):
#    """
#    Provides a get method handler.
#    """
#    queryset = Contact.objects.all()
#    serializer_class = ContactsSerializer


class RESTAPI_ListCreateContactView(generics.ListCreateAPIView):
    """
    GET rest_api/contacts/
    POST rest_api/contacts/
    """
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
    #permission_classes = (permissions.IsAuthenticated,)

    @validate_request_contact_data
    def post(self, request, *args, **kwargs):
        #print(request.data, "!!!!")
        #print(request.data["id"], "!!!!")
        try:
            contact_id = request.data["id"]

        except:
            contact_id = None

        a_contact = Contact.objects.create(
            id=contact_id,
            first_name=request.data["first_name"],
            second_name=request.data["second_name"],
            email=request.data["email"],
        )
        return Response(
            data=ContactsSerializer(a_contact).data,
            status=status.HTTP_201_CREATED
        )



# class RESTAPI_ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     GET rest_api/contacts/:id/
#     PUT rest_api/contacts/:id/
#     DELETE rest_api/contacts/:id/
#     """
#     queryset = Contact.objects.all()
#     serializer_class = ContactsSerializer


#     def get(self, request, *args, **kwargs):
#         #
#         try:
#             a_contact = self.queryset.get(pk=kwargs["pk"])
#             #obj = get_object_or_404(Contact, id=a_contact.id)
#             #p(a_contact.id)

#             return Response(ContactsSerializer(a_contact).data)
#         except Contact.DoesNotExist:
#             return Response(
#                 data={
#                     "message": "Contact with id: {} does not exist".format(kwargs["pk"])
#                 },
#                 status=status.HTTP_404_NOT_FOUND
#             )




class RESTAPI_ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET rest_api/contacts/:id/
    PUT rest_api/contacts/:id/
    DELETE rest_api/contacts/:id/
    """
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer

    def get(self, request, *args, **kwargs):
        #
        try:
            a_contact = self.queryset.get(pk=kwargs["pk"])
            #obj = get_object_or_404(Contact, id=a_contact.id)
            #p(a_contact.id)

            return Response(ContactsSerializer(a_contact).data)
        except Contact.DoesNotExist:
            return Response(
                data={
                    "message": "Contact with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


    @validate_request_contact_data
    def put(self, request, *args, **kwargs):
        try:
            a_contact = self.queryset.get(pk=kwargs["pk"])
            serializer = ContactsSerializer()
            updated_contact = serializer.update(a_contact, request.data)
            return Response(ContactsSerializer(updated_contact).data)
        except Contact.DoesNotExist:
            return Response(
                data={
                    "message": "Contact with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_contact = self.queryset.get(pk=kwargs["pk"])
            a_contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contact.DoesNotExist:
            return Response(
                data={
                    "message": "Contact with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )





########## Web Platform VIEWS ###########

def contact_create_view(request):
    form = ContactForm(request.POST or None)
    success = False
    #p(request.GET)
    #p(request.POST)
    #p(request.POST.get("first_name"))

    if form.is_valid():
        form.save()
        form = ContactForm()
        #success = True
        #form.errors['success'] = 'Saved'
        messages.success(request, 'Your form was saved') 
        #messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'contact_create.html', {"form":form,"success":success}, )




class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)




class AboutPageView(TemplateView):
    template_name = "about.html"



class ContactsView(TemplateView):
    #template_name = "about.html"
    def get(self, request, **kwargs):
            now = timezone.now()
            #obj = Contact.objects.get(id=1)
            #print(request)
            csrf_token = django.middleware.csrf.get_token(request)
            table_data = Contact.objects.all()
            #p(table_data )
            #p(csrf_token,"ContactsView")
            table = ContactTable(csrf_token= csrf_token, data=table_data, )
            #p(dir(table))
            #p(table.__dict__)
            RequestConfig(request).configure(table)

            return render(request, 'contacts_overview.html', {"table_data":table,}, )


def contact_edit_view(request, contact_id):
    success = False
    #obj = Contact.objects.get(id=contact_id)
    obj = get_object_or_404(Contact, id=contact_id)
    form = ContactForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        obj = get_object_or_404(Contact, id=contact_id)
        form = ContactForm(request.POST or None, instance=obj)
        #form = ContactForm()
        #success = True
        #form.errors['success'] = 'Saved'
        messages.success(request, 'Your changes was saved!') 
        success = True

        #messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'contact_edit.html', {"form":form,"success":success, "contact_id":contact_id}, )



def contact_datails_view(request, contact_id):
    success = False
    #obj = Contact.objects.get(id=contact_id)
    obj = get_object_or_404(Contact, id=contact_id)
    #p(dir(obj))
    obj = Contact.objects.filter(id=contact_id).values()
    #p(obj)
    # form = ContactForm(request.POST or None, instance=obj)
    # if form.is_valid():
    #     form.save()
    #     obj = get_object_or_404(Contact, id=contact_id)
    #     form = ContactForm(request.POST or None, instance=obj)
    #     #form = ContactForm()
    #     #success = True
    #     #form.errors['success'] = 'Saved'
    #     messages.success(request, 'Your changes was saved!') 
    #     success = True

        #messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'contact_details.html', { "contact_id":contact_id, "obj":obj }, )



def contact_delete_view_with_submit(request, contact_id):
    success = False
    #obj = Contact.objects.get(id=contact_id)
    obj = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        obj.delete()
        success = True

    return render(request, 'contact_edit.html', {"form":form,"success":success}, )

def deleted_contact_view(request, contact_id):
    success = False
    #obj = Contact.objects.get(id=contact_id)
    obj = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        obj.delete()
        success = True
        #form = ContactForm(request.POST or None, instance=obj)
        messages.success(request, 'Contact  with id "{}" was deleted!'.format(contact_id))

        return render(request, 'contact_was_deleted.html', {"success":success}, )
    else:
        #success = False
        #form = ContactForm(request.POST or None, instance=obj)
        messages.error(request, "ERROR! Contact with id '{}'' wasn't deleted!".format(contact_id))
        return render(request, 'contact_was_deleted.html', {"success":success}, )



def unsecure_delete_contact_view(request, contact_id):
    success = False
    #obj = Contact.objects.get(id=contact_id)
    obj = get_object_or_404(Contact, id=contact_id)
    if request.method == "GET":
        obj.delete()
        success = True
        #form = ContactForm(request.POST or None, instance=obj)
        messages.success(request, 'Contact  with id "{}" was deleted!'.format(contact_id))

        return render(request, 'contact_was_deleted.html', {"success":success}, )
    else:
        #success = False
        #form = ContactForm(request.POST or None, instance=obj)
        messages.error(request, "ERROR! Contact with id '{}'' wasn't deleted!".format(contact_id))
        return render(request, 'contact_was_deleted.html', {"success":success}, )








############################################################################
############# Functions for learn goal ####################
############################################################################



#### handle item not found exeption





class _ContactsView(TemplateView):
    #template_name = "about.html"
    def get(self, request, **kwargs):
            now = timezone.now()
            #obj = Contact.objects.get(id=1)
            #print(request)
            table_data = Contact.objects.all()
            #RequestConfig(request).configure(table_data)
            return render(request, 'contacts_overview.html', {"table_data":table_data,}, )
           



def contact_edit_view_with_404_exception(request, contact_id):
    success = False 
    try:
        obj = Contact.objects.get(id=contact_id)
    except Contact.DoesNotExist:
        raise Http404
    #obj = get_object_or_404(Contact, id=contact_id)
    form = ContactForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        obj = get_object_or_404(Contact, id=contact_id)
        form = ContactForm(request.POST or None, instance=obj)
        #form = ContactForm()
        #success = True
        #form.errors['success'] = 'Saved'
        messages.success(request, 'Your changes was saved!') 
        success = True
        #messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'contact_edit.html', {"form":form,"success":success}, )





def raw_contact_create_view(request):
    success = False
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        
        #p(request.GET)
        if form.is_valid():
            #p(request.POST)
            #p(request.POST.get("first_name"))
            success = True
            Contact.objects.create(
                        first_name=request.POST.get("first_name"),
                        second_name=request.POST.get("second_name"),
                        email=request.POST.get("email"),)
            messages.success(request, 'Your form was saved')

    return render(request, 'contact_create.html', {"form":form,"success":success}, )

def raw_raw_contact_create_view(request):
    form = RawContactForm(request.POST or None)
    success = False
    #p(request.GET)
    if form.is_valid():
        #p(request.POST)
        #p(request.POST.get("first_name"))
        Contact.objects.create(**form.cleaned_data)
        messages.success(request, 'Your form was saved')

    return render(request, 'contact_create.html', {"form":form,"success":success}, )










class ExternContactsView(TemplateView):
    #template_name = "about.html"
    def get(self, request, **kwargs):
            now = timezone.now()
            conn = connect(default_db_name)
            col_names = db_handler.cols(default_table_name)
            contacts = list(db_handler.rows(default_table_name))
            contacts_as_dict = [dict(zip(col_names, c)) for c in contacts]
            #print(contacts_as_dict)
            #table_data = NameTable(contacts_as_dict)
            table_data = getTable(default_table_name)
            RequestConfig(request).configure(table_data)
            #p(table_data)
            #contacts_as_arrays = contacts
            #print(list(rows))
            #users = User.objects.all()
            #return render(request, 'contacts_overview.html', {'contacts': contacts_as_dict, "col_names":col_names}, )
            #p(list(contacts))
            #p(contacts_as_arrays)
            return render(request, 'contacts_overview.html', {"table_data":table_data,}, )



#def contacts(request):
#    return render(request, 'tutorial/people.html', {'people': Person.objects.all()})