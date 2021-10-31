from django import forms

PLACES = (
    (1, 'パントリー'),
    (2, 'キッチン・冷蔵庫'),
    (3, '洗面台下'),
    (4, 'トイレ'),
    (5, 'リビング・たんす'),
    (6, '下駄箱'),
    (7, 'その他'),
)

class ItemForm(forms.Form):
    item = forms.CharField(max_length=30, label='品目名')
    place = forms.fields.ChoiceField(
        label='保管場所',
        choices = PLACES,
        required=True,
        widget=forms.widgets.Select
    )
    memo = forms.CharField(label='備考', widget=forms.Textarea(), required=False)
