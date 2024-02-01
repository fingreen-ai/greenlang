""" Upstream Leased Assets calculation methods """

from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Hidden, Field
from crispy_forms.bootstrap import AppendedText

from fingreen_web.models import (
    GhgEmissionSourceComputationMethod,
    CollectionItem,
    GhgEmissionFactor,
)
from ...base.forms import PredefinedFactorCalculationMethodForm


class LeasedBuildingsAssetSpecificMethodForm(forms.ModelForm):
    """Automatic method form"""

    method = forms.ModelChoiceField(
        queryset=GhgEmissionSourceComputationMethod.objects.all(), required=True
    )

    total_floor_space = forms.FloatField(required=True)
    leased_floor_space = forms.FloatField(required=True)

    scope1_emissions = forms.FloatField(required=True)
    scope2_emissions = forms.FloatField(required=True)

    leased_month_count = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        """Init form"""
        super().__init__(*args, **kwargs)

        has_instance = 'instance' in kwargs and kwargs['instance']
        if has_instance:
            instance = kwargs['instance']
            if instance.widget_data:
                for key, value in instance.widget_data.items():
                    setattr(self.fields[key], 'initial', value)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False

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
                    AppendedText(
                        "total_floor_space", "m2", placeholder=_("Total floor space")
                    ),
                    css_class="col-6",
                ),
                Column(
                    AppendedText(
                        "leased_floor_space", "m2", placeholder=_("Leased floor space")
                    ),
                    css_class="col-6",
                ),
                Column(
                    AppendedText(
                        "scope1_emissions",
                        "kg CO2e",
                        placeholder=_("Total Building Scope 1 Emissions"),
                    ),
                    css_class="col-6",
                ),
                Column(
                    AppendedText(
                        "scope2_emissions",
                        "kg CO2e",
                        placeholder=_("Total Building Scope 2 Emissions"),
                    ),
                    css_class="col-6",
                ),
                Column(
                    Field("leased_month_count", placeholder=_("Leased month count")),
                    css_class="col-6",
                ),
                Column(
                    Submit(
                        "submit",
                        _("Add") if not has_instance else _("Update"),
                        css_class="btn btn-light-primary w-100 mb-3",
                    ),
                    css_class="d-flex align-items-end col-2",
                ),
            ),
        )

    def save(self, commit=True):
        """Save form"""

        instance = super().save(commit=False)

        leased_ratio = (
            self.cleaned_data["leased_floor_space"]
            / self.cleaned_data["total_floor_space"]
        )
        leased_ratio_per_year = (
            leased_ratio * self.cleaned_data["leased_month_count"] / 12
        )

        instance.value_float = leased_ratio_per_year
        instance.ghg_unit = "m2_year"

        instance.ghg_factor = GhgEmissionFactor.objects.create(
            name=instance.description_user,
            factor_type="custom_leased_nuildings",
            method=self.cleaned_data["method"],
        )

        instance.widget_data = {
            "total_floor_space": self.cleaned_data["total_floor_space"],
            "leased_floor_space": self.cleaned_data["leased_floor_space"],
            "scope1_emissions": self.cleaned_data["scope1_emissions"],
            "scope2_emissions": self.cleaned_data["scope2_emissions"],
            "leased_month_count": self.cleaned_data["leased_month_count"],
        }

        if commit:
            instance.save()

        return instance

    class Meta:
        model = CollectionItem
        fields = [
            "method",
            "collection",
            "ghg_scope",
            "item_type",
            "description_user",
        ]


class LeasedBuildingsAverageDataMethodForm(PredefinedFactorCalculationMethodForm):
    """LeasedBuildingsAverageDataMethodForm"""

    leased_month_count = forms.IntegerField(required=True)

    def get_extra_fields(self):
        """Return fields."""
        return [
            Column(
                Field("leased_month_count", placeholder=_("Leased month count")),
                css_class="col-2",
            ),
        ]

    def save(self, commit=True):
        """Save form"""

        instance = super().save(commit=False)

        instance.widget_data = {
            "leased_month_count": self.cleaned_data["leased_month_count"],
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
