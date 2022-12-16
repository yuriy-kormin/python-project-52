# Generated by Django 4.1.3 on 2022-12-12 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_initial'),
        ('tasks', '0007_rename_mark_task_label_remove_task_performer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.taskuser'),
        ),
    ]