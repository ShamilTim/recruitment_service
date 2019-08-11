from django.forms import ModelForm

from rservice.models import Recruit, Sith


class RecruitForm(ModelForm):
    class Meta:
        model = Recruit
        fields = ('name', 'planet_habitat', 'age', 'email')


class TestForm(ModelForm):
    class Meta:
        model = Recruit
        fields = ('answer_1', 'answer_2', 'answer_3')


class ShadowHandForm(ModelForm):
    class Meta:
        model = Sith
        fields = ('shadow_hand',)
