# Generated by Django 3.2.3 on 2021-06-09 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COUNTRIES',
            fields=[
                ('IDCOUNTRY', models.AutoField(primary_key=True, serialize=False)),
                ('COUNTRYNAME', models.CharField(blank=True, max_length=350)),
                ('NATIVECOUNTRY', models.CharField(blank=True, max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='DRUGNAMES',
            fields=[
                ('IDDDRUGNAME', models.AutoField(primary_key=True, serialize=False)),
                ('DRUGNAME', models.CharField(max_length=350)),
                ('FORM', models.CharField(blank=True, max_length=350)),
                ('CONTAIN', models.CharField(blank=True, max_length=350)),
                ('NUMBER', models.IntegerField(blank=True)),
                ('ISDEAD', models.IntegerField(blank=True)),
                ('GRPJOUR', models.IntegerField(blank=True)),
                ('NUMLIKETHISALL', models.IntegerField(blank=True)),
                ('KEYWORDSTRING', models.CharField(blank=True, max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='FILES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(blank=True, max_length=350)),
                ('fileData', models.BinaryField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='KEYWORDS',
            fields=[
                ('IDKWKEYWORD', models.AutoField(primary_key=True, serialize=False)),
                ('KEYWORDNAME', models.CharField(blank=True, max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='PARAMETERS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PARAMETER', models.CharField(blank=True, max_length=350)),
                ('PARAMETERVALUE', models.CharField(blank=True, max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCERS',
            fields=[
                ('IDPRODUCER', models.AutoField(primary_key=True, serialize=False)),
                ('PRODUCERNAME', models.CharField(blank=True, max_length=350)),
                ('NATIVEPRODUCER', models.CharField(blank=True, max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='SELLERS',
            fields=[
                ('IDSSELLER', models.AutoField(primary_key=True, serialize=False)),
                ('SELLERNAME', models.CharField(max_length=350)),
                ('ADDR', models.CharField(blank=True, max_length=350)),
                ('PHONE', models.CharField(blank=True, max_length=350)),
                ('REGION', models.IntegerField(blank=True)),
                ('PAYCOND', models.IntegerField(blank=True)),
                ('COMMENT', models.IntegerField(blank=True)),
                ('EMAIL', models.EmailField(blank=True, max_length=254)),
                ('LICENSE', models.IntegerField(blank=True)),
                ('FORMOPL', models.IntegerField(blank=True)),
                ('NATIVESELLER', models.IntegerField(blank=True)),
                ('POSINPRICE', models.CharField(blank=True, max_length=350)),
                ('POSINPRICEALL', models.CharField(max_length=350)),
                ('CDATE', models.DateTimeField(blank=True)),
                ('NATBANK', models.CharField(blank=True, max_length=350)),
                ('ESHOP_SITE', models.IntegerField(blank=True)),
                ('ESHOP_INFO', models.IntegerField(blank=True)),
                ('USDCOURSE', models.IntegerField(blank=True)),
                ('RURCOURSE', models.IntegerField(blank=True)),
                ('hasDelivery', models.IntegerField(blank=True)),
                ('baseContactId', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='USERS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('idfirm', models.IntegerField(blank=True)),
                ('mac', models.CharField(max_length=100)),
                ('ipCame', models.CharField(max_length=100)),
                ('dtCameLats', models.DateTimeField(blank=True)),
                ('ipCheck', models.CharField(max_length=100)),
                ('dtCheck', models.DateTimeField(blank=True)),
                ('date_from', models.DateTimeField(blank=True)),
                ('date_to', models.DateTimeField(blank=True)),
                ('srcfile', models.CharField(max_length=100)),
                ('typebd', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VIDAL',
            fields=[
                ('IDVCLASS', models.AutoField(primary_key=True, serialize=False)),
                ('INTNAME', models.CharField(blank=True, max_length=350)),
                ('CLINGROUP', models.CharField(blank=True, max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='MAIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDCOLOR', models.IntegerField(blank=True)),
                ('IDMONEYTYPE', models.IntegerField(blank=True)),
                ('IDPRICEMASK', models.IntegerField(blank=True)),
                ('PRICE', models.IntegerField(blank=True)),
                ('VPRICE', models.IntegerField(blank=True)),
                ('BPRICE', models.IntegerField(blank=True)),
                ('IDEXPDATE', models.IntegerField(blank=True)),
                ('NDS', models.IntegerField(blank=True)),
                ('CDATE', models.DateTimeField(blank=True)),
                ('IDDRUGNAME', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.drugnames')),
                ('IDSELLER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sellers')),
            ],
        ),
        migrations.AddField(
            model_name='drugnames',
            name='IDCLASS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vidal'),
        ),
        migrations.AddField(
            model_name='drugnames',
            name='IDCOUNTRY',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.countries'),
        ),
        migrations.AddField(
            model_name='drugnames',
            name='IDPRODUCER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producers'),
        ),
    ]
