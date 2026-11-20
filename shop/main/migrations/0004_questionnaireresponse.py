# Створено вручну для збереження відповідей анкети.
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_tag_card_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionnaireResponse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("age", models.PositiveSmallIntegerField()),
                (
                    "topic",
                    models.CharField(
                        choices=[
                            ("orders", "Замовлення"),
                            ("delivery", "Доставка"),
                            ("other", "Інше"),
                        ],
                        max_length=20,
                    ),
                ),
                ("visit_date", models.DateField()),
                ("rating", models.PositiveSmallIntegerField()),
                ("comment", models.TextField(blank=True)),
                ("accepted_terms", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
