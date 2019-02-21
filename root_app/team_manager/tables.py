import django_tables2
from django_tables2 import tables, TemplateColumn
#from my_app.models import Training
from .models import Contact
from django_tables2.utils import A  # alias for Accessor
from django.utils.safestring import mark_safe
from django.utils.html import escape
from team_manager.helpers.debugger import p
from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponseRedirect
from django.urls import reverse
import django
import session_csrf
from session_csrf import anonymous_csrf
#import django_csrf

edit_icon = static("/icons/edit.png")
delete_icon = static("/icons/delete.png")
info_icon = static("/icons/info2.png")

class ImageColumn(django_tables2.LinkColumn):
    #def __init__(self, csrf_token=None, **kwargs):
    #    super(ImageColumn, self).__init__(**kwargs)
    #    self.csrf_token = csrf_token
        #p(csrf_token, "ContactTable")
    #def __init__(self, text=None *args, **kwargs):
    #    super(ImageColumn, self).__init__(*args, **kwargs)

    #    self.text = text
    #    #print(self.text)
    #@anonymous_csrf
    def render(self, record, value, ):
        #p( (record.id, value), "RV")
        #from crequest.middleware import CrequestMiddleware
        #current_request = CrequestMiddleware.get_request()
        #if not current_request:
        #    return None
        #csrf_token = session_csrf.monkeypatch()
        #p(csrf_token)
        #csrf_token = django.middleware.csrf.get_token(current_request)
        #p(csrf_token)
        #p(dir(self))
        #p(self.__dict__)
        #p(dir(self.link))
        #p(self.link.__dict__, "self.link.__dict__")
        return format_html(

            """<a href="{}" title="Details"><img src="{}"  height="28px", width="28px" alt="info"></a>
               <a href="{}" title="Edit"><img src="{}"  height="28px", width="28px" alt="edit"></a>
               <a href="{}" title="Unsecure_Delete"><img src="{}" onclick="return confirm('Are you sure you want to delete this?')"  height="28px", width="28px" alt="delete"></a>
               

            """.format(
                    reverse('contact_datails', args=(record.id,)), info_icon,
                    reverse('edit_contact', args=(record.id,)), edit_icon,
                    reverse('unsecure_deleted_view', args=(record.id,)), delete_icon,
                    #csrf_token, reverse('deleted_view', args=(record.id,))
                    #reverse('deleted_view', args=(record.id,)), delete_icon,
                    #reverse('deleted_view', args=(record.id,)), delete_icon,
                )
        )


#<form method='POST'> <input value="{}" class="btn btn-default btn-danger" type="submit" value="Delete" formaction="{}" /> </form>

class ContactTable(tables.Table):

    def __init__(self, csrf_token=None, **kwargs):
        super(ContactTable, self).__init__(**kwargs)
        self.csrf_token = csrf_token
        #p(self.columns.columns)
        #p(csrf_token, "ContactTable")


    #Actions = django_tables2.LinkColumn("contact_datails_2", kwargs={"contact_id": A("pk")},  text='Details', orderable=False)
    #Action = ImageColumn("Actions",  orderable=False) #contact_id=A("pk"),
    Actions = ImageColumn( "contact_datails", kwargs={"contact_id": A("pk")},  text='Details', orderable=False)

    class Meta:
        #csrf_token = self.csrf_token
        model = Contact
        fields = [f.name for f in Contact._meta.get_fields()]
        template_name = 'django_tables2/bootstrap-responsive.html'
        #attrs = {"class": "paleblue"}
        #attrs = {'class': 'table table-sm'}


