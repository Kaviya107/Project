# Generated by Django 3.0.8 on 2020-08-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basic_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, null=True)),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('DOB', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Others', 'Others'), ('Female', 'Female'), ('Male', 'Male')], default='Female', max_length=20)),
                ('mobile_number', models.CharField(max_length=100, null=True)),
                ('email_address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='designation_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('date_of_join', models.CharField(max_length=100, null=True)),
                ('salary', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='other_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('mother_name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=100, null=True)),
                ('aadhar_number', models.CharField(max_length=100, null=True)),
                ('driving_license', models.CharField(max_length=100, null=True)),
                ('emergency_contact_name', models.CharField(max_length=100, null=True)),
                ('emergency_contact_number', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='salary_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, null=True)),
                ('account_number', models.CharField(max_length=100, null=True)),
                ('IFSC_code', models.CharField(max_length=100, null=True)),
                ('bank_name', models.CharField(max_length=100, null=True)),
                ('bank_address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
