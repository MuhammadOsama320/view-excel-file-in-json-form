import datetime
import pandas as pd
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Customer
from uploadfile.models import Customer


# Create your views here.


class UploadFileView(TemplateView):
    template_name = 'upload.html'

    def get_context_data(self, **kwargs):
        return kwargs

    def post(self, request, *args, **kwargs):
        file1 = request.FILES['upload']
        print(file1)
        read_file = pd.read_csv(file1)
        json_data = read_file.to_json()
        Customer.objects.all().delete()
        for row in read_file.to_dict(orient='records'):
            Customer.objects.update_or_create(consignee_name=row.get("Consignee Name"),
                                              pickup_address_id=row.get("Pickup Address ID"),
                                              show_information_on_air_waybill=row.get("Show Information on Air Waybill"),
                                              consignee_city_name=row.get("Consignee City Name"),
                                              consignee_address=row.get("Consignee Address"),
                                              consignee_phone_number_1=row.get("Consignee Phone Number 1 (03000000000)"),
                                              consignee_phone_number_2=row.get("Consignee Phone Number 2 (03000000000)"),
                                              consignee_email_address=row.get("Consignee Email Address"),
                                              self_collection=row.get("Self Collection"),
                                              order_id=row.get("Order ID"),
                                              order_date=datetime.datetime.strptime(row.get("Order Date (YYYY-MM-DD)"), '%d/%m/%Y'),
                                              item_product_type_id=row.get("Item Product Type ID"),
                                              item_description=row.get("Item Description"),
                                              item_quantity=str(row.get("Item Quantity")),
                                              item_insurance=row.get("Item Insurance"),
                                              product_value=row.get("Product Value"),
                                              special_instructions=row.get("Special Instructions"),
                                              estimated_weight=row.get("Estimated Weight (kg)"),
                                              mode_of_shipment_id=row.get("Mode of Shipment ID"),
                                              same_day_timing_id=row.get("Same Day Timing ID"),
                                              collection_amount=row.get("Collection Amount"),
                                              mode_of_payment_id=row.get("Mode of Payment ID"),
                                              charges_mode_id=row.get("Charges Mode ID"),
                                              pieces=row.get("Pieces"),
                                              shipper_reference_number_1=row.get("Shipper Reference Number 1"),
                                              shipper_reference_number_2=row.get("Shipper Reference Number 2"),
                                              shipper_reference_number_3=row.get("Shipper Reference Number 3"),
                                              shipper_reference_number_4=row.get("Shipper Reference Number 4"),
                                              shipper_reference_number_5=row.get("Shipper Reference Number 5"))
        return redirect(reverse('data'))


class DataView(TemplateView):
    template_name = 'data.html'

    def get_context_data(self, **kwargs):
        kwargs['customers'] = Customer.objects.all()
        return kwargs
