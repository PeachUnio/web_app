from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from catalog.models import Product



FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]



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


        if cost is not None and cost < 0:
            raise ValidationError("Цена не может быть отрицательной!")


        return cost


    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        if name:
            name_lower = name.lower()
            for word in FORBIDDEN_WORDS:
                if word.lower() in name_lower:
                    raise ValidationError("Некорректное слово было использовано в названии продукта!")
        return name


    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        if description:
            description_lower = description.lower()
            for word in FORBIDDEN_WORDS:
                if word.lower() in description_lower:
                    raise ValidationError("Некорректное слово было использовано в описании продукта!")
        return description
