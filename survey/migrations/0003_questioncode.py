# Generated by Django 3.1.7 on 2021-05-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_stepcountdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=10)),
                ('code', models.TextField()),
                ('description', models.CharField(max_length=30)),
            ],
        ),
    ]