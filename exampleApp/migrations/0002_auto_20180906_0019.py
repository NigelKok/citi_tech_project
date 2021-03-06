# Generated by Django 2.1 on 2018-09-05 16:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exampleApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='snippet',
            name='essentialExpenses',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='snippet',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='snippet',
            name='locations',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AMK', 'Ang Mo Kio'), ('SRG', 'Serangoon'), ('WLDS', 'Woodlands')], default='AMK', max_length=20),
        ),
        migrations.AddField(
            model_name='snippet',
            name='monthlyIncome',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='snippet',
            name='personalSavings',
            field=models.FloatField(null=True),
        ),
    ]
