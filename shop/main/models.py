from django.db import models

# Create your models here.

CYRILLIC_COLLATION = "utf8mb4_unicode_ci"

class Tag(models.Model):
    name = models.CharField(max_length=50, )

    def __str__(self):
        return self.name

class Card(models.Model):
    title = models.CharField(max_length=200, )
    description = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='cards/')
    created_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name='cards', blank=True)


class QuestionnaireResponse(models.Model):
    # Спільні варіанти тем для вибору у формі та збереження у базі даних.
    TOPIC_CHOICES = [
        ("orders", "Замовлення"),
        ("delivery", "Доставка"),
        ("other", "Інше"),
    ]

    full_name = models.CharField(max_length=100, )
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    topic = models.CharField(
        max_length=20,
        choices=TOPIC_CHOICES,
    )
    visit_date = models.DateField()
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, )
    accepted_terms = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} — {self.get_topic_display()}"