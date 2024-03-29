# Generated by Django 4.1.7 on 2023-09-19 20:52

import disease.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "disease",
            "0004_alter_book_table_author_alter_book_table_image_link_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="book_table",
            name="buy_link",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="age",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        1, "age should be greater than or equal to 1"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="allergies_link",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="country",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="email_address",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                validators=[disease.models.validate_small_letters],
            ),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="first_name",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                validators=[disease.models.validate_small_letters],
            ),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="history_link",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="last_name",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                validators=[disease.models.validate_small_letters],
            ),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="occupation",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="phone_number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="reports_link",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="state",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="street_address",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="case_table",
            name="zip_code",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="historicalbook_table",
            name="buy_link",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="age",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        1, "age should be greater than or equal to 1"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="allergies_link",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="country",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="email_address",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                validators=[disease.models.validate_small_letters],
            ),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="first_name",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                validators=[disease.models.validate_small_letters],
            ),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="history_link",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="last_name",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                validators=[disease.models.validate_small_letters],
            ),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="occupation",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="phone_number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="reports_link",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="state",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="street_address",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcase_table",
            name="zip_code",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
