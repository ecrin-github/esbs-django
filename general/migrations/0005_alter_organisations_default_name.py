# Generated by Django 4.1.6 on 2023-04-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_alter_organisations_ror_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisations',
            name='default_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]