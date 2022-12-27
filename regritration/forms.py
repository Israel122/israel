from django import forms
from .models import Reg

class RegCustom(forms.ModelForm):
    class Meta:
        model=Reg
        fields=('Sur_name',"First_name","Middle_name","Date_of_birth","Age","Photo","Postal_Address","Residential_Address",
        "Latest_School_Address","Latest_class_Attended","Home_Telephone_Number","Name_of_Father","Occpation_of_Father",
        "Contact_Address_of_Father","Tel_No_of_Father","Tel_No_of_Father","Occpation_of_Mother","Contact_Address_of_Mother","Tel_No_of_Mother",
        "In_case_of_any_emergency_contact","Any_allery_or_physical_defect")


        widgets = {
            'Sur_name' : forms.TextInput(attrs={'class':'form-control'}),
            "First_name":forms.TextInput(attrs={'class':'form-control'}),
            "Middle_name":forms.TextInput(attrs={'class':'form-control'}),
            "Postal_Address":forms.Textarea(attrs={'class':'form-control'}),
            "Residential_Address":forms.Textarea(attrs={'class':'form-control'}),
            "Latest_School_Address":forms.Textarea(attrs={'class':'form-control'}),
            "Home_Telephone_Number":forms.TextInput(attrs={'class':'form-control'}),
            "Name_of_Father":forms.TextInput(attrs={'class':'form-control'}),
            "Occupation_of_Father":forms.TextInput(attrs={'class':'form-control'}),        
            "Contact_Address_of_Father":forms.Textarea(attrs={'class':'form-control'}),
            "Tel_No_of_Father":forms.TextInput(attrs={'class':'form-control'}),
            "Name_of_mother":forms.TextInput(attrs={'class':'form-control'}),
            "Occupation_of_mother":forms.Textarea(attrs={'class':'form-control'}),
            "Contact_Address_of_mother":forms.Textarea(attrs={'class':'form-control'}),
            "Tel_No_of_mother":forms.TextInput(attrs={'class':'form-control'}),
            "Occupation_of_mother":forms.TextInput(attrs={'class':'form-control'}),
            "Contact_Address_of_Mother":forms.Textarea(attrs={'class':'form-control'}),
            "Tel_No_of_mother":forms.TextInput(attrs={'class':'form-control'}),
            "In_case_of_any_emergency_contact":forms.Textarea(attrs={'class':'form-control'}),
            "Any_allery_or_physical_defect":forms.Textarea(attrs={'class':'form-control'}),
}