# Generated by Django 3.0.5 on 2020-04-13 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_agreement_details_customer_details_site_details_user_authentication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='AGR_AUTO_UUPDATE',
            new_name='AGR_AUTO_UPDATE',
        ),
    ]
