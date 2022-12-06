# Generated by Django 4.1.3 on 2022-12-06 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_initial'),
        ('tasks', '0004_alter_task_author_alter_task_performer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='performer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='performer', to='users.taskuser'),
        ),
    ]
