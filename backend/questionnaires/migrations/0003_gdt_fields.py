from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0002_patient_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnairesession',
            name='gdt_patient_id',
            field=models.CharField(
                blank=True,
                max_length=100,
                help_text='GDT Feld 3000 – interne SAMAS Patienten-ID',
            ),
        ),
        migrations.AddField(
            model_name='questionnairesession',
            name='gdt_request_id',
            field=models.CharField(
                blank=True,
                max_length=100,
                help_text='GDT Feld 8315 – Anforderungskennung für Rückantwort',
            ),
        ),
    ]
