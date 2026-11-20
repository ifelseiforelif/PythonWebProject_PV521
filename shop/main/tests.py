from django.test import TestCase

from .models import QuestionnaireResponse


# Перевіряємо збереження валідних відповідей і показ помилок для некоректних.
class QuestionnaireViewTests(TestCase):
    def test_valid_submission_is_saved(self):
        response = self.client.post(
            "/questions/",
            {
                "full_name": "Олена Приклад",
                "email": "olena@example.com",
                "age": 25,
                "topic": "delivery",
                "visit_date": "2026-12-01",
                "rating": 8,
                "comment": "Підкажіть час доставки",
                "accepted_terms": "on",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Дякуємо! Ваші відповіді збережено.")
        self.assertEqual(QuestionnaireResponse.objects.count(), 1)
        self.assertEqual(
            QuestionnaireResponse.objects.get().full_name,
            "Олена Приклад",
        )

    def test_invalid_submission_displays_errors_without_saving(self):
        response = self.client.post(
            "/questions/",
            {
                "full_name": "",
                "email": "непошта",
                "age": 0,
                "topic": "invalid",
                "visit_date": "не дата",
                "rating": 11,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertContains(response, "Enter a valid email address.")
        self.assertEqual(QuestionnaireResponse.objects.count(), 0)
