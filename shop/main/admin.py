from django.contrib import admin

from main.models import Card, QuestionnaireResponse

# Register your models here.
admin.site.register(Card)
admin.site.register(QuestionnaireResponse)