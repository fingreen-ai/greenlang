"""Investments forms"""

from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Hidden, Field
from crispy_forms.bootstrap import AppendedText

from fingreen_web.models import (
    GhgEmissionSourceComputationMethod,
    CollectionItem,
    GhgEmissionFactor,
    GhgEmissionFactorValue,
)
from ...base.forms import (
    PredefinedFactorCalculationMethodForm,
    TaggedFormMixin,
    CustomFactorCalculationMethodForm,
)


class ProjectSpecificMethodForm(TaggedFormMixin, forms.ModelForm):
    """Equity Investments Specific method form"""

    method = forms.ModelChoiceField(
        queryset=GhgEmissionSourceComputationMethod.objects.all(), required=True
    )

    scope1_emissions = forms.FloatField(required=True)
    scope2_emissions = forms.FloatField(required=True)

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
                Column(
                    Field(
                        "tags",
                        css_class="form-control tags-input",
                    ),
                    css_class="col-md-6",
                ),
            ),
            Row(
                Column(
                    AppendedText(
                        "value_float",
                        "%",
                        min=0,
                        max=100,
                        placeholder=_("Equity"),
                        type="number",
                        css_class="form-control form-control-lg form-control-solid",
                    ),
                    css_class="col-md-3",
                ),
                Column(
                    AppendedText(
                        "scope1_emissions",
                        _("kg CO2e/project financed"),
                        placeholder=_(
                            "Scope 1 Emissions of relevant project in the reporting year"
                        ),
                        type="number",
                        autocomplete="off",
                        css_class="form-control form-control-lg form-control-solid",
                    ),
                    css_class="col-md-4",
                ),
                Column(
                    AppendedText(
                        "scope2_emissions",
                        _("kg CO2e/project financed"),
                        placeholder=_(
                            "Scope 2 Emissions of relevant project in the reporting year"
                        ),
                        type="number",
                        autocomplete="off",
                        css_class="form-control form-control-lg form-control-solid",
                    ),
                    css_class="col-md-4",
                ),
                Column(
                    Submit(
                        "submit",
                        _("Add") if not has_instance else _("Update"),
                        css_class="btn btn-light-primary w-100 mb-3",
                    ),
                    css_class="d-flex align-items-end col",
                ),
            ),
        )

    def save(self, commit=True):
        """Save form"""

        instance = super().save(commit=False)

        instance.ghg_unit = "pct"

        scope_1_emissions = self.cleaned_data["scope1_emissions"]
        scope_2_emissions = self.cleaned_data["scope2_emissions"]

        instance.ghg_factor = GhgEmissionFactor.objects.get_or_create(
            name=instance.description_user,
            factor_type="investments",
            method=self.cleaned_data["method"],
            organization=self.user.org_active,
        )[0]

        GhgEmissionFactorValue.objects.update_or_create(
            factor=instance.ghg_factor,
            unit="pct",
            defaults={
                "tot_co2_kg": scope_1_emissions + scope_2_emissions,
            },
        )

        instance.widget_data = {
            'scope1_emissions': scope_1_emissions,
            'scope2_emissions': scope_2_emissions,
        }

        if commit:
            instance.save()

            self.save_tags(instance)

        return instance

    class Meta:
        model = CollectionItem
        fields = [
            "method",
            "collection",
            "ghg_scope",
            "item_type",
            "description_user",
            "tags",
            "value_float",
        ]


class AverageSpecificMethodForm(PredefinedFactorCalculationMethodForm):
    """Equity Average Specific method form"""

    equity_share = forms.FloatField(required=True)

    def get_extra_fields(self):
        return {
            Column(
                AppendedText(
                    "equity_share",
                    "%",
                    min=0,
                    max=100,
                    placeholder=_("Equity"),
                    type="number",
                    css_class="form-control form-control-lg form-control-solid",
                ),
                css_class="col-2",
            ),
        }

    def save(self, commit=True):
        """Save form"""

        instance = super().save(commit=False)

        instance.widget_data = {
            'equity_share': self.cleaned_data["equity_share"],
        }

        if commit:
            instance.save()

        return instance


class LongTermFinancedProjectSpecificMethodForm(CustomFactorCalculationMethodForm):
    """Supplier specific method"""

    equity_share = forms.FloatField(required=True)

    def __init__(self, *args, **kwargs):
        """Init form"""
        super().__init__(*args, **kwargs)
        self.fields["custom_factor_name"].label = _("Emission Source Description")
        self.fields["custom_factor_name"].widget.attrs["placeholder"] = _(
            "Emission Source Description"
        )
        self.factor_type = "investments"
    
    def get_value_float_columns(self):
        """ Get value float columns """
        return [
            Column(
                AppendedText(
                    "value_float",
                    _("years"),
                    placeholder=self.get_placeholder('value_float'),
                    min=0,
                    type="number",
                    autocomplete="off",
                    css_class="form-control form-control-lg form-control-solid mb-3 mb-lg-0",
                ),
                css_class="col-2",
            ),
            Hidden("ghg_unit", "year"),
        ]

    def get_extra_fields(self):
        return {
            Column(
                AppendedText(
                    "equity_share",
                    "%",
                    min=0,
                    max=100,
                    placeholder=_("Equity"),
                    type="number",
                    css_class="form-control form-control-lg form-control-solid",
                ),
                css_class="col-2",
            ),
        }

    def get_placeholder(self, field_name):
        if field_name == 'value_float':
            return _("Expected lifetime of project")
        return super().get_placeholder(field_name)
    
    def save(self, commit=True):
        """Save form"""

        instance = super().save(commit=False)

        instance.widget_data = {
            'equity_share': self.cleaned_data["equity_share"],
        }

        if commit:
            instance.save()

        return instance

    class Meta(CustomFactorCalculationMethodForm.Meta):
        pass
