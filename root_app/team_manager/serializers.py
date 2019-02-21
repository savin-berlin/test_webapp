from rest_framework import serializers
from .models import Contact


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [f.name for f in Contact._meta.get_fields()]