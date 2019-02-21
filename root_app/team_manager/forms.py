from django import forms
from team_manager.helpers.debugger import p
from .models import Contact


class ContactForm(forms.ModelForm):
     class Meta: 
        model = Contact
        fields = [f.name for f in Contact._meta.get_fields()]
        #p(fields,"fields")
 

class ContactForm_overwerited(forms.ModelForm):
    ### overwriting and doing extra validations

    ### overwrite first_name from the model
    first_name =  forms.CharField(
                                max_length=100,
                                required=True, 
                                widget=forms.TextInput(
                                                        attrs={"placeholder":"First Name"}
                                                        )

                                )
    class Meta: 
        model = Contact
        fields = [f.name for f in Contact._meta.get_fields()]
        #p(fields,"fields")

    def clean_first_name(self, *args,**kwargs):
        title = self.clened_data.get("titel")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not valud title")

    def clean_email(self, *args,**kwargs):
        email = self.clened_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not valid email")
        return email

 







class RawContactForm(forms.Form):
    first_name =  forms.CharField(
                                    max_length=100,
                                    required=True, 
                                    widget=forms.TextInput(
                                                            attrs={"placeholder":"First Name"}
                                                            )

                                    )
    
    second_name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(max_length=70,  required=True, initial="11@22.de")
    #p(fields,"fields")