# Generated by Django 4.2 on 2023-05-16 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_regis', '0002_remove_deliveryaddres_customer_remove_rate_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.IntegerField()),
                ('conten', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_regis.customer')),
            ],
        ),
    ]
