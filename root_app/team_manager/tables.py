from django_tables2 import tables, TemplateColumn
from my_app.models import Training

class TrainingTable(tables.Table):
    class Meta:
         model = Training
         attrs = {'class': 'table table-sm'}
         fields = ['date', 'description', 'tags', 'points', 'edit']

     edit = TemplateColumn(template_name='pages/tables/training_update_column.html')