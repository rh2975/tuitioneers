# Generated by Django 3.1.5 on 2021-02-25 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttnapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='mark',
            new_name='marks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher', to='ttnapp.teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='taken_subjects', to='ttnapp.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='details',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='fb',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='insta',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='pic',
            field=models.ImageField(blank=True, default='uploads/368-kakashi.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='pic',
            field=models.ImageField(blank=True, default='uploads/emc.png', upload_to='uploads/'),
        ),
    ]