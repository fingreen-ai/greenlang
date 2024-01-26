"""
Category 2 : Fugitive Emission custom forms
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from django.db.models import Count

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Hidden, Row, Column, Field
from crispy_forms.bootstrap import AppendedText

from fingreen_web.models import (
    CollectionItem,
    GhgEmissionSourceComputationMethod,
    GhgEmissionFactor,
)


class MassBalanceMethodForm(forms.ModelForm):
    """Mass balance method form"""

    method = forms.ModelChoiceField(
        queryset=GhgEmissionSourceComputationMethod.objects.all(), required=True
    )

    begin_year_storage = forms.FloatField(
        required=True, label=_("Inventory at the beginning of the year")
    )
    end_year_storage = forms.FloatField(
        required=True, label=_("Inventory at the end of the year")
    )
    year_decrease = forms.FloatField(
        required=True, label=_("Decrease during the year"),
    )

    purchased = forms.FloatField(
        required=True, label=_("Purchased from producers/distributors in bulk")
    )

    acquired = forms.FloatField(
        required=True, label=_("Added to equipment by contractors")
    )

    available = forms.FloatField(
        required=True, label=_("Total Purchases/ Acquisitions"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields.keys():
            self.fields[field_name].required = True

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.show_labels = True
        self.fields["description_user"].label = _("Emission source")
        self.fields["ghg_factor"].label = _("Gas or refrigerant")
        self.fields["value_float"].label = _(
            "Refrigerant or Gas Total Emissions"
        )

        self.fields["year_decrease"].widget.attrs['readonly'] = True
        self.fields["available"].widget.attrs['readonly'] = True
        self.fields["value_float"].widget.attrs['readonly'] = True
        
        self.fields["description_user"].widget = forms.Select(
            choices=[
                (
                    "Refrigeration and air conditioning equipments in use",
                    _("Refrigeration and air conditioning equipments in use"),
                ),
                ("Fire suppression equipments", _("Fire suppression equipments")),
                (
                    "Direct emissions from purchased industrial gases",
                    _("Direct emissions from purchased industrial gases"),
                ),
            ]
        )

        self.fields["ghg_factor"].choices = [
            (
                factor.pk,
                f"{factor.factor_subtype_repr}\
                    {' > ' if factor.factor_subtype else ''}{factor.name}",
            )
            for factor in self.initial["method"]
            .factors.annotate(value_count=Count("values"))
            .filter(value_count__gt=0)
        ]

        self.helper.layout = Layout(
            Hidden(
                "method", self.initial["method"].id
            ),  # extra field used in the view to preset form
            Hidden("collection", self.initial["collection"].id),
            Hidden("item_type", self.initial["item_type"]),
            Hidden("ghg_scope", self.initial["ghg_scope"]),
            Hidden("ghg_unit", "kg"),
            Row(
                Column(
                    Field(
                        "description_user",
                        data_control="select2",
                        data_placeholder=self.fields["description_user"].label,
                        style="display: none;",
                        css_class="form-select",
                    ),
                    css_class="col-md-6",
                ),
                Column(
                    Field(
                        "ghg_factor",
                        data_control="select2",
                        data_placeholder=_("Emission factor"),
                        style="display: none;",
                        css_class="form-control",
                    ),
                    css_class="col-6",
                ),
            ),
            Row(
                Column(AppendedText("begin_year_storage", "kg"), css_class="col-4"),
                Column(AppendedText("end_year_storage", "kg"), css_class="col-4"),
                Column(AppendedText("year_decrease", "kg", css_class="disabled"), css_class="col-4"),
                css_class="d-flex align-items-end my-3",
            ),
            Row(
                Column(AppendedText("purchased", "kg"), css_class="col-4"),
                Column(AppendedText("acquired", "kg"), css_class="col-4"),
                Column(AppendedText("available", "kg", css_class="disabled"), css_class="col-4"),
                css_class="d-flex align-items-end my-3",
            ),
            Row(
                Column(AppendedText("value_float", "kg", css_class="disabled"), css_class="col-6"),
                Column(
                    Submit(
                        "submit", _("Add"), css_class="btn btn-light-primary w-100 mb-3"
                    ),
                    css_class="col-2",
                ),
                css_class="d-flex align-items-end my-3",
            ),
        )

    def save(self, commit=True):
        """Save"""

        instance = super().save(commit=False)

        instance.widget_data = {
            "begin_year_storage": self.cleaned_data["begin_year_storage"],
            "end_year_storage": self.cleaned_data["end_year_storage"],
            "purchased": self.cleaned_data["purchased"],
            "acquired": self.cleaned_data["acquired"],
        }

        if commit:
            instance.save()

        return instance

    class Meta:
        model = CollectionItem
        fields = [
            "collection",
            "ghg_scope",
            "item_type",
            "description_user",
            "ghg_factor",
            "value_float",
            "ghg_unit",
        ]


class ScreeningMethodApproachForm(forms.ModelForm):
    """ScreeningMethodApproachForm."""

    method = forms.ModelChoiceField(
        queryset=GhgEmissionSourceComputationMethod.objects.all(), required=True
    )
    gas = forms.ModelChoiceField(
        queryset=GhgEmissionFactor.objects.all(), required=True
    )
    quantity = forms.FloatField(required=True, label=_("Quantity"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields.keys():
            self.fields[field_name].required = True

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.fields["ghg_factor"].label = _("Emission source")
        self.fields["value_float"].label = _("Refrigerant or Gas Capacity")

        gases = GhgEmissionFactor.objects.filter(
            # method__source=self.initial["method"].source, factor_type="gas"
            method__source__slug="fugitive-emissions", factor_type="gas"
        )

        self.fields["ghg_factor"].choices = [
            (
                factor.pk,
                f"{factor.factor_subtype_repr}\
                    {' > ' if factor.factor_subtype else ''}{factor.name}",
            )
            for factor in self.initial["method"]
            .factors.annotate(value_count=Count("values"))
            .filter(value_count__gt=0)
        ]

        self.fields["gas"].choices = [
            (
                factor.pk,
                f"{factor.factor_subtype_repr}\
                    {' > ' if factor.factor_subtype else ''}{factor.name}",
            )
            for factor in gases.annotate(value_count=Count("values")).filter(
                value_count__gt=0
            )
        ]

        self.helper.layout = Layout(
            Hidden(
                "method", self.initial["method"].id
            ),  # extra field used in the view to preset form
            Hidden("collection", self.initial["collection"].id),
            Hidden("item_type", self.initial["item_type"]),
            Hidden("ghg_scope", self.initial["ghg_scope"]),
            Hidden("ghg_unit", "kg"),
            Row(
                Column(
                    Field(
                        "ghg_factor",
                        data_control="select2",
                        data_placeholder=_("Choose a GHG emission factor"),
                        style="display: none;",
                        css_class="form-control",
                    ),
                    css_class="col-3",
                ),
                Column(
                    Field(
                        "gas",
                        data_control="select2",
                        data_placeholder=self.fields["gas"].label,
                        style="display: none;",
                        css_class="form-select",
                    ),
                    css_class="col-2",
                ),
                Column("quantity", css_class="col"),
                Column(AppendedText("value_float", "kg"), css_class="col"),
                *self.get_extra_fields(),
                Column(
                    Submit("submit", _("Add"), css_class="btn btn-light-primary"),
                    css_class="mb-3",
                ),
                css_class="col d-flex align-items-end",
            ),
        )

    def get_extra_fields(self):
        """
        Return extra fields to add to the form.
        This method is meant to be overriden by subclasses.
        Return:
            A list of extra fields to add to the form. Empty list by default.
        """
        return []
    
    def save_extra_fields(self, instance):
        """
        Save extra fields.
        This method is meant to be overriden by subclasses.
        Args:
            instance: The collection item instance.
        """
        return {}


    def save(self, commit=True):
        """Save"""

        instance = super().save(commit=False)

        instance.description_user = instance.ghg_factor.name

        instance.widget_data = {
            "gas": self.cleaned_data["gas"].id,
            "quantity": self.cleaned_data["quantity"],
        }

        instance.widget_data.update(self.save_extra_fields(instance))

        if commit:
            instance.save()

        return instance

    class Meta:
        model = CollectionItem
        fields = [
            "collection",
            "ghg_scope",
            "item_type",
            "ghg_unit",
            "ghg_factor",
            "value_float",
        ]
