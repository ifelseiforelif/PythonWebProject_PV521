from django import forms

from .models import QuestionnaireResponse


class QuestionnaireForm(forms.Form):
    # Поля форм перевіряють обов'язковість, формат і допустимі межі даних.
    full_name = forms.CharField(
        label="Ім'я та прізвище",
        max_length=100,
        error_messages={'required':'Треба заповнити це поле'},
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    age = forms.IntegerField(
        label="Вік",
        min_value=1,
        max_value=120,
        error_messages={'min_value':'Вік не може бути меньший за 1'},
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    topic = forms.ChoiceField(
        label="Тема питання",
        choices=QuestionnaireResponse.TOPIC_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    visit_date = forms.DateField(
        label="Бажана дата відповіді",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    rating = forms.IntegerField(
        label="Оцініть сайт від 1 до 10",
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 10}),
    )
    comment = forms.CharField(
        label="Ваше питання або коментар",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
    )
    accepted_terms = forms.BooleanField(
        label="Погоджуюся на обробку наданих даних",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
