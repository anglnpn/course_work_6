from django import forms

from main.models import Questionnaire


class QuestionnaireForm(forms.ModelForm):
    """
    Форма для валидации и стилизации анкеты
    """

    class Meta:
        model = Questionnaire
        fields = ['name', 'surname', 'age', 'sex', 'city', 'description', 'image']

    def clean_description(self):
        """
        Проверка на недопустимые слова в описании анкеты
        """
        cleaned_descriptions = self.cleaned_data.get('description')
        words_unused = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
                        'ставки', 'продам']
        if cleaned_descriptions in words_unused:
            raise forms.ValidationError("Данная информация недопустима")

        return cleaned_descriptions
