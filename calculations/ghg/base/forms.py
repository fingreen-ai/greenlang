""" GHG base forms."""

from django import forms
from django.urls import reverse
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Hidden, Row, Column, Field
from crispy_forms.bootstrap import AppendedText

from fingreen_web.models import (
    CollectionItem,
    GhgEmissionFactor,
    GhgEmissionFactorValue,
    GhgEmissionSourceComputationMethod,
)


class PredefinedFactorCalculationMethodForm(forms.ModelForm):
    """
    This form provides the inputs for category using a predefined factor.
    It exposes the following fields:

    - description_user: a description of the item
    - ghg_factor: the GHG emission factor to use, prefilled with the factors related to selected calculation method
    - value_float: the amount value
    - ghg_unit: the GHG emission unit to use, prefilled with the units related to selected GHG emission factor
    
    As hidden fields, the form exposes:

    - method: the selected GHG emission source computation method
    - collection: the selected collection
    - item_type: the selected item type, must be 'ghg'
    - ghg_scope: the selected GHG scope

    """ # pylint: disable=line-too-long

    method = forms.ModelChoiceField(
        queryset=GhgEmissionSourceComputationMethod.objects.all(), required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields.keys():
            self.fields[field_name].required = True

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.form_show_labels = False

        self.fields["ghg_factor"].choices = [
        (
            factor.pk,
            f"{factor.factor_subtype_repr}{' > ' if factor.factor_subtype else ''}{factor.name}",
        )  # pylint: disable=line-too-long
        for factor in self.initial["method"]
        .factors.annotate(value_count=Count("values"))
        .filter(value_count__gt=0)  # pylint: disable=line-too-long
        ]

        self.helper.layout = Layout(
            Hidden(
                "method", self.initial["method"].id
            ),  # field used in the view to preset form
            Hidden("collection", self.initial["collection"].id),
            Hidden("item_type", self.initial["item_type"]),
            Hidden("ghg_scope", self.initial["ghg_scope"]),
            Row(
                Column(
                    Field(
                        "description_user",
                        placeholder=_("Description"),
                        type="text",
                        autocomplete="off",
                        css_class="form-control form-control-lg form-control-solid mb-3 mb-lg-0",
                    ),
                    css_class="col-md-6",
                ),
            ),
            Row(
                Column(
                    Field(
                        "ghg_factor",
                        data_control="select2",
                        data_placeholder=_("Choose a GHG emission factor"),
                        hx_post=reverse("ghg_factor_units"),
                        hx_swap="innerHTML",
                        hx_target="#custom_units",
                        hx_trigger="load, change",
                        hx_include="[name='ghg_factor']",
                        style="display: none;",
                        css_class="form-control",
                    ),
                    css_class="col-5",
                ),
                Column(
                    Field(
                        "value_float",
                        placeholder=_("Enter amount"),
                        min=0,
                        type="number",
                        autocomplete="off",
                        css_class="form-control form-control-lg form-control-solid mb-3 mb-lg-0",
                    ),
                    css_class="col-2",
                ),
                Column(
                    Field(
                        "ghg_unit",
                        data_placeholder=_("Select an emission source 1st"),
                        data_control="select2",
                        style="display: none;",
                        css_class="form-control",
                    ),
                    id="custom_units",
                    css_class="col",
                ),
                *self.get_extra_fields(),
                Column(
                    Submit("submit", _("Add"), css_class="btn btn-light-primary"),
                    css_class="col",
                ),
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


class CustomFactorCalculationMethodForm(forms.ModelForm):
    """CustomFactorCalculationMethodForm"""

    method = forms.ModelChoiceField(
        queryset=GhgEmissionSourceComputationMethod.objects.all(), required=True
    )

    custom_factor_name = forms.CharField(required=True)
    custom_factor_value = forms.FloatField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.factor_type = "custom"

        for field_name in self.fields.keys():
            self.fields[field_name].required = True

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.form_show_labels = False

        self.fields["custom_factor_value"].widget.attrs["placeholder"] = _(
            "Emission factor value"
        )
        self.fields["custom_factor_value"].widget.attrs["min"] = 0
        self.fields["custom_factor_value"].widget.attrs["step"] = 0.01

        self.helper.layout = Layout(
            Hidden(
                "method", self.initial["method"].id
            ),  # field used in the view to preset form
            Hidden("collection", self.initial["collection"].id),
            Hidden("item_type", self.initial["item_type"]),
            Hidden("ghg_scope", self.initial["ghg_scope"]),
            Row(
                Column(
                    Field(
                        "description_user",
                        placeholder=_("Description"),
                        type="text",
                        autocomplete="off",
                        css_class="form-control form-control-lg form-control-solid mb-3 mb-lg-0",
                    ),
                    css_class="col-md-6",
                ),
            ),
            Row(
                Column(
                    Field(
                        "custom_factor_name",
                        placeholder=_("Emission factor name"),
                        type="text",
                        autocomplete="off",
                        css_class="form-control form-control-lg form-control-solid mb-3 mb-lg-0",
                    ),
                    css_class="col-3",
                ),
                Column(
                    Field(
                        "value_float",
                        placeholder=_("Enter amount"),
                        min=0,
                        type="number",
                        autocomplete="off",
                        css_class="form-control form-control-lg form-control-solid mb-3 mb-lg-0",
                    ),
                    css_class="col-2",
                ),
                Column(
                    Field(
                        "ghg_unit",
                        data_placeholder=_("Select an emission source 1st"),
                        data_control="select2",
                        style="display: none;",
                        css_class="form-control",
                    ),
                    id="custom_units",
                    css_class="col-2",
                ),
                Column(
                    AppendedText("custom_factor_value", "kg CO2e/ unit"),
                    css_class="col-4",
                ),
                Column(
                    Submit("submit", _("Add"), css_class="btn btn-light-primary w-100"),
                    css_class="col-1",
                ),
            ),
        )

    def save(self, commit=True):
        """Save"""

        instance = super().save(commit=False)

        custom_factor_name = self.cleaned_data["custom_factor_name"]
        custom_factor_value = self.cleaned_data["custom_factor_value"]
        method = self.cleaned_data["method"]

        instance.widget_data = {
            "custom_factor_name": custom_factor_name,
            "custom_factor_value": custom_factor_value,
        }

        if instance.item_type == "ghg":
            instance.ghg_factor = GhgEmissionFactor.objects.create(
                name=custom_factor_name, factor_type=self.factor_type, method=method
            )
            GhgEmissionFactorValue.objects.create(
                factor=instance.ghg_factor,
                unit=instance.ghg_unit,
                tot_co2_kg=custom_factor_value,
            )

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
            "value_float",
            "ghg_unit",
        ]


class SupplierSpecificMethodForm(CustomFactorCalculationMethodForm):
    """Supplier specific method"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["custom_factor_name"].label = _("Supplier name")
        self.factor_type = "supplier"

    class Meta(CustomFactorCalculationMethodForm.Meta):
        pass


class CustomAverageDataMethodForm(CustomFactorCalculationMethodForm):
    """Custom Average data method form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["custom_factor_name"].label = _("Name")
        self.factor_type = "goods"

    class Meta(CustomFactorCalculationMethodForm.Meta):
        pass
