from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnairesession',
            name='patient_last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='questionnairesession',
            name='patient_first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='questionnairesession',
            name='patient_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='questionnairesession',
            name='patient_birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questionnairesession',
            name='invitation_sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
