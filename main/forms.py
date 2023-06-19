from django import forms
from .models import *


class SertForm(forms.Form):
    phone = forms.CharField(max_length = 11, label = "телефон")
    name = forms.CharField(max_length = 50, min_length = 4, label = "ФИО", widget = forms.TextInput())
    email = forms.EmailField(widget = forms.EmailInput())
    view = forms.ModelChoiceField(queryset=Sertificats.objects.all(), label = "вид сертификата")

    num_carta = forms.CharField(max_length = 16, label = "номер карты")
    m_y = forms.CharField(max_length=4, label = 'срок действия')
    bank = forms.ModelChoiceField(queryset=Banks.objects.all(), label = "выберете банк")
    boolfield = forms.TypedChoiceField(
                   label = "выберете способ получения",
                   coerce=lambda x: x == 'True',
                   choices=((False, 'заберу сам'), (True, 'отправить на почту')),
                   widget=forms.RadioSelect
                )

    is_person = forms.BooleanField(label = "Согласиться на обработку персональных данных")
 

class TalonForm(forms.Form):
    phone = forms.CharField(max_length = 11,
                            label = "телефон",
                            widget = forms.TextInput(attrs={'placeholder': '8**********', 'class': 'form_input'}))
    name = forms.CharField(max_length = 50,
                           min_length = 4,
                           label = "ФИО",
                           widget = forms.TextInput(attrs={'placeholder': 'Кошкин Кот Котович', 'class': 'form_input'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'placeholder': 'koshka@email.com', 'class': 'form_input'}))
    view = forms.ModelChoiceField(queryset=Massage.objects.all(),
                                  label = "вид массажа")
    service = forms.ModelChoiceField(queryset=Service.objects.all(),
                                     label = "доп. услуга")
    num_carta = forms.CharField(max_length = 16,
                                label = "номер карты",
                                widget = forms.TextInput(attrs={'placeholder': '**** **** **** ****'}))
    m_y = forms.CharField(max_length=4,
                          label = 'срок действия',
                          widget = forms.TextInput(attrs={'placeholder': '**/**'}))
    bank = forms.ModelChoiceField(queryset=Banks.objects.all(),
                                  label = "выберете банк",
                                  widget = forms.Select(attrs={'class': 'form_input'}))

    text = forms.CharField(max_length=200, 
                           required=False,
                           label = "комментарий (необязательно)", 
                           widget = forms.Textarea(attrs={'cols':50, 'rows': 5, 'placeholder': 'Здесь могу буть ваши пожелания'}))
    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'text')
   
    name = forms.CharField(max_length = 50,
                           min_length = 3,
                           label = "Ваше имя",
                           widget = forms.TextInput(attrs={'placeholder': 'Кошкин Кот Котович', 'class': 'form_input'}))
    text = forms.CharField(max_length=600, 
                           label = "Комментарий", 
                           widget = forms.Textarea(attrs={'cols':50, 'rows': 5, 'placeholder': 'Напишите пару слов...', 'class': 'form_input'}))
    