# Generated by Django 2.0.4 on 2018-04-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change', '0002_auto_20180407_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='c_category',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]