from django import forms

class OrderCreateForm(forms.Form):
    city = forms.CharField(label="Город", max_length=255)
    warehouse = forms.CharField(label="Отделение", max_length=255)
