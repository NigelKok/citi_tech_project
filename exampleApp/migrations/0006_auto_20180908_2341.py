# Generated by Django 2.1 on 2018-09-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleApp', '0005_auto_20180908_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='locations',
            field=models.CharField(choices=[('Ang-Mo-Kio', 'Ang Mo Kio'), ('Bedok', 'Bedok'), ('Bishan', 'Bishan'), ('Bukit-Batok', 'Bukit Batok'), ('Bukit-Merah', 'Bukit Merah'), ('Bukit-Panjang', 'Bukit Panjang'), ('Bukit-Timah', 'Bukit Timah'), ('Central', 'Central'), ('Choa', 'Choa'), ('Clementi', 'Clementi'), ('Geylang', 'Geylang'), ('Hougang', 'Hougang'), ('Jurong-East', 'Jurong East'), ('Jurong-West', 'Jurong West'), ('Kallang', 'Kallang'), ('Marine-Parade', 'Marine Parade'), ('Pasir-Ris', 'Pasir Ris'), ('Punggol', 'Punggol'), ('Queenstown', 'Queenstown'), ('Sembawang', 'Sembawang'), ('Sengkang', 'Sengkang'), ('Serangoon', 'Serangoon'), ('Tampines', 'Tampines'), ('Toa-Payoh', 'Toa Payoh'), ('WLDS', 'Woodlands'), ('Yishun', 'Yishun')], max_length=100),
        ),
    ]
