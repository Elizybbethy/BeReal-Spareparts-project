from django.forms import ModelForm
from .models import *

class AddForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "Category_name", "part_name", "arrival_date", "total_quantity", 
            "country_of_origin", "branch_name","received_quantity","unit_price"
        ]
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = [
            "quantity","amount_received", "issued_to","phone", "branch", "part"
        ]