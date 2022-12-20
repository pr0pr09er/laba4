from django import forms


class FilmForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Дата выпуска в формате YYYY-MM-DD'}))
    actors = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Актеры'}))
    show_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Дата показа в формате YYYY-MM-DD'}))
