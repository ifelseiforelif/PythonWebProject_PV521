# Змінюємо колірування текстових полів, щоб коректно зберігати кирилицю.
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_questionnaireresponse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(db_collation="utf8mb4_unicode_ci", max_length=50),
        ),
        migrations.AlterField(
            model_name="card",
            name="title",
            field=models.CharField(db_collation="utf8mb4_unicode_ci", max_length=200),
        ),
        migrations.AlterField(
            model_name="card",
            name="description",
            field=models.CharField(db_collation="utf8mb4_unicode_ci", max_length=200),
        ),
        migrations.AlterField(
            model_name="questionnaireresponse",
            name="full_name",
            field=models.CharField(db_collation="utf8mb4_unicode_ci", max_length=100),
        ),
        migrations.AlterField(
            model_name="questionnaireresponse",
            name="email",
            field=models.EmailField(db_collation="utf8mb4_unicode_ci", max_length=254),
        ),
        migrations.AlterField(
            model_name="questionnaireresponse",
            name="topic",
            field=models.CharField(
                choices=[
                    ("orders", "Замовлення"),
                    ("delivery", "Доставка"),
                    ("other", "Інше"),
                ],
                db_collation="utf8mb4_unicode_ci",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="questionnaireresponse",
            name="comment",
            field=models.TextField(db_collation="utf8mb4_unicode_ci", blank=True),
        ),
    ]
