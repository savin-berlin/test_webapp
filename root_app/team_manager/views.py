 # team_manager/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from team_manager.db.db_handler import connect,default_db_name,default_table_name,db_handler,getTable
from team_manager.helpers.debugger import p
from django_tables2 import RequestConfig




# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)



# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"




class ContactsView(TemplateView):
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