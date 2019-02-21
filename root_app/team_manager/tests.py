from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Contact
from .serializers import ContactsSerializer
from django_fake_model import models as f
from rest_framework import serializers
from django.db import models

from team_manager.helpers.debugger import p

from .serializers import ContactsSerializer


# create fake Model for tests


#@FakeContacts.fake_me
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_contact(first_name="", second_name="", email=""):
        if first_name != "" and second_name != "":
            #FakeContacts.objects.create(first_name=first_name, second_name=second_name, email=email)
            Contact.objects.create(first_name=first_name, second_name=second_name, email=email)

    def setUp(self):
        # add test data
        self.create_contact("Jack", "Jonnsons", "jack@jonh.de")
        self.create_contact("alice", "key", "alice@key.com")
        self.create_contact("Mikle", "Jackson", "mikle@jackson.net")
        self.create_contact("alexa", "Amazone", "alexa@amazon.com")

    #@classmethod 
    #def tearDown(self):
        #super(type(self), self).tearDown()


    #def



#@FakeContacts.fake_me
class GetAllContactsTest(BaseViewTest):

    def test_get_all_contacts(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("restapi_contacts_list_and_create")
        )
        # fetch the data from db
        #expected = FakeContacts.objects.all()
        #serialized = FakeContactsSerializer(expected, many=True)
        expected = Contact.objects.all()
        serialized = ContactsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




class ContactModelTest(TestCase):

    #@classmethod
    def create_contact(self,first_name="", second_name="", email=""):
        if first_name != "" and second_name != "":
            #FakeContacts.objects.create(first_name=first_name, second_name=second_name, email=email)
            Contact.objects.create(first_name=first_name, second_name=second_name, email=email)

    #@classmethod
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.create_contact("Jack", "Jonnsons", "jack@jonh.de")

    def test_first_name_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        contact=Contact.objects.get(id=1)
        field_label = contact._meta.get_field('second_name').verbose_name
        self.assertEquals(field_label, 'second name')

    def test_first_name_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        contact = Contact.objects.get(id=1)
        expected_object_name = f'{contact.id} - {contact.first_name} - {contact.second_name}'
        self.assertEquals(expected_object_name, str(contact))

    def test_get_absolute_url(self):
        contact = Contact.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(contact.get_absolute_url(), '/contact/1/')




class ContactListViewTest(TestCase):
    #@classmethod
    def create_contact(self,first_name="", second_name="", email="", num=0):
        if first_name != "" and second_name != "":
            #FakeContacts.objects.create(first_name=first_name, second_name=second_name, email=email)
            Contact.objects.create(first_name=first_name+str(num), second_name=second_name+str(num), email=email+str(num))

    #@classmethod
    def setUp(self):
        # Set up non-modified objects used by all test methods
        
        self.number_of_contacts = 13
        for author_id in range(self.number_of_contacts):
            self.create_contact("Jack", "Jonnsons", "jack@jonh.de",num=0)


           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('contacts_overview'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('contacts_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts_overview.html')
        
    def test_number_of_contacts(self):
        response = self.client.get(reverse('contacts_overview'))
        #print(type(response.context[0]), list(response.context[0]) , "!!!")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('table_data' in response.context)
        #print(response.context['table_data'].data, "????")
        self.assertTrue(len(response.context['table_data'].rows) == self.number_of_contacts)

