# Generated by Django 3.1.5 on 2021-02-24 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('pic', models.ImageField(upload_to='uploads/')),
                ('details', models.CharField(max_length=1000)),
                ('fb', models.CharField(max_length=100)),
                ('insta', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mark', models.IntegerField(default=0)),
                ('pic', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=100)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_details', to='ttnapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_details', to='ttnapp.person')),
                ('subjects', models.ManyToManyField(blank=True, related_name='taken_subjects', to='ttnapp.Subject')),
            ],
        ),
    ]