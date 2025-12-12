from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"



class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "image", "cost"]

    def clean_cost(self):
        cost = self.cleaned_data.get("cost")

        if cost < 0:
            raise ValidationError("Цена не может быть отрицательной!")

        return cost

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "")
        description = cleaned_data.get("description", "")
        taboo_list = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        for world in taboo_list:
            world = world.lower()
            if world in name:
                raise ValidationError("Некорректное слово было использованы в названии продукта!")
            if world in description:
                raise ValidationError("Некорректное слово было использованы в описании продукта!")
            continue

        return cleaned_data
