# Generated by Django 5.1.2 on 2024-10-21 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("certifications", "0002_remove_certificate_course_ar_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CertificateTemplate",
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
                ("name", models.CharField(max_length=100)),
                ("template_file", models.FileField(upload_to="certificate_templates")),
            ],
        ),
        migrations.CreateModel(
            name="QRCodeCustomization",
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
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="qr_logos"),
                ),
                ("foreground_color", models.CharField(default="#000000", max_length=7)),
                ("background_color", models.CharField(default="#FFFFFF", max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name="certificate",
            name="template",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="certifications.certificatetemplate",
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="qr_customization",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="certifications.qrcodecustomization",
            ),
        ),
    ]
