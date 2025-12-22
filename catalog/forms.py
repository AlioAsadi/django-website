from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(required=False, label="جستجو")
    stock = forms.ChoiceField(
        required=False,
        choices=[
            ("", "همه"),
            ("in_stock", "موجود"),
            ("limited", "محدود"),
            ("out_of_stock", "ناموجود"),
        ],
    )
    sort = forms.ChoiceField(
        required=False,
        choices=[
            ("new", "جدیدترین"),
            ("name", "نام"),
        ],
        initial="new",
    )
