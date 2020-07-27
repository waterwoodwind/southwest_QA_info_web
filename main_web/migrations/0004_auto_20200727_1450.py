# Generated by Django 2.2.7 on 2020-07-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0003_remove_qa_info_grade_human'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='event_class',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='information_classification',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='information_source',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='sub_department',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='sub_information_classification',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='time_bucket',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='department',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='event_class',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='information_classification',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='information_source',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='location',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='state',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='sub_department',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='sub_information_classification',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='team',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
        migrations.AddField(
            model_name='time_bucket',
            name='order',
            field=models.DecimalField(decimal_places=3, default=1000, max_digits=8),
        ),
    ]
