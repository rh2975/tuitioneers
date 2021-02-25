# Generated by Django 3.1.5 on 2021-02-25 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttnapp', '0003_auto_20210225_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='pic',
        ),
        migrations.AddField(
            model_name='exam',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='student_exam', to='ttnapp.student'),
            preserve_default=False,
        ),
    ]
