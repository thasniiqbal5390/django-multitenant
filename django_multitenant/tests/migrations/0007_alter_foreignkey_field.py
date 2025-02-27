# Generated by Django 2.1.1 on 2019-03-01 08:45

from django.db import migrations
import django.db.models.deletion
import django_multitenant.fields


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0006_subtask_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="project",
            field=django_multitenant.fields.TenantForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tests.Project"
            ),
        ),
    ]
