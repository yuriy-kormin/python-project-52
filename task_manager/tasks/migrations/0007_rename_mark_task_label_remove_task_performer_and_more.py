# Generated by Django 4.1.3 on 2022-12-12 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_initial'),
        ('tasks', '0006_bond_task_mark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='mark',
            new_name='label',
        ),
        migrations.RemoveField(
            model_name='task',
            name='performer',
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.taskuser', verbose_name='executor'),
        ),
    ]
