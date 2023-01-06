from django.forms import ModelForm
from .models import Filme


class PostForm(ModelForm):
    class Meta:
        model = Filme
        fields = ['filme', 'resenha', 'categoria']
