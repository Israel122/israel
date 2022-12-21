# Generated by Django 4.1.3 on 2022-12-19 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Sur_name", models.CharField(max_length=20, null=True)),
                ("First_name", models.CharField(max_length=20, null=True)),
                ("Middle_name", models.CharField(max_length=20, null=True)),
                (
                    "Date_of_birth",
                    models.DateField(
                        default=datetime.datetime(2022, 12, 19, 12, 43, 32, 226012),
                        verbose_name="Date",
                    ),
                ),
                ("Age", models.PositiveIntegerField(null=True)),
                ("Photo", models.ImageField(blank=True, null=True, upload_to="photo/")),
                ("Postal_Address", models.TextField(max_length=1100, null=True)),
                ("Residential_Address", models.TextField(max_length=1100, null=True)),
                ("Latest_School_Address", models.TextField(max_length=2000, null=True)),
                (
                    "Latest_class_Attended",
                    models.CharField(
                        choices=[
                            ("PRY_1", "Primary 1"),
                            ("PRY_2", "Primary 2"),
                            ("PRY_3", "Primary 3"),
                            ("PRY_4", "Primary 4"),
                            ("PRY_5", "Primary 5"),
                            ("PRY_6", "Primary 6"),
                        ],
                        default="PRY_1",
                        max_length=30,
                    ),
                ),
                ("Home_Telephone_Number", models.CharField(max_length=11, null=True)),
                ("Name_of_Father", models.CharField(max_length=200, null=True)),
                ("Occpation_of_Father", models.CharField(max_length=200, null=True)),
                (
                    "Contact_Address_of_Father",
                    models.TextField(max_length=1100, null=True),
                ),
                ("Tel_No_of_Father", models.CharField(max_length=11, null=True)),
                ("Name_of_Mother", models.CharField(max_length=200, null=True)),
                ("Occpation_of_Mother", models.CharField(max_length=200, null=True)),
                (
                    "Contact_Address_of_Mother",
                    models.TextField(max_length=1100, null=True),
                ),
                ("Tel_No_of_Mother", models.CharField(max_length=11, null=True)),
                (
                    "In_case_of_any_emergency_contact",
                    models.TextField(max_length=1100, null=True),
                ),
                (
                    "Any_allery_or_physical_defect",
                    models.TextField(max_length=1100, null=True),
                ),
            ],
        ),
    ]