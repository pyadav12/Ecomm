# Generated by Django 4.0.4 on 2023-04-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0002_registration_email_registration_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('cat_image', models.ImageField(upload_to='Category/')),
            ],
        ),
    ]
