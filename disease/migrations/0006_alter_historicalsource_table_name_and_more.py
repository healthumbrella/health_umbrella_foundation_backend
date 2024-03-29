# Generated by Django 4.1.7 on 2024-01-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("disease", "0005_alter_book_table_buy_link_alter_case_table_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsource_table",
            name="name",
            field=models.CharField(
                choices=[
                    ("books", "books"),
                    ("socialMedia", "socialMedia"),
                    ("youtube", "youtube"),
                    ("website", "website"),
                    ("article", "article"),
                    ("quora", "quora"),
                    ("directCase", "directCase"),
                ],
                max_length=1000,
            ),
        ),
        migrations.AlterField(
            model_name="source_table",
            name="name",
            field=models.CharField(
                choices=[
                    ("books", "books"),
                    ("socialMedia", "socialMedia"),
                    ("youtube", "youtube"),
                    ("website", "website"),
                    ("article", "article"),
                    ("quora", "quora"),
                    ("directCase", "directCase"),
                ],
                max_length=1000,
            ),
        ),
    ]
