
from django import forms
from . models import RateSearch
class RateSearchForm(forms.ModelForm):
    class Meta:
        model = RateSearch
        fields = ('IlluvialTier','IlluvialStage','ShardTier','Captured')
