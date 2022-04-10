from django.forms import IntegerField, ModelForm
from nft.models import Image, Collection

class AvatarForm(ModelForm):
    quantity = IntegerField(max_value=10)
    class Meta:
            model = Collection
            fields = ["name"]