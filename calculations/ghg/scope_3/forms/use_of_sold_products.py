""" Forms for the use of sold products calculation method. """
from django import forms
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from crispy_forms.layout import Layout, Submit, Hidden, Row, Column, Field
from crispy_forms.bootstrap import AppendedText

from fingreen_web.models import CollectionItem

from ...base.forms import PredefinedFactorCalculationMethodForm
from ...scope_1.forms import ScreeningMethodApproachForm


class DirectElectricityOrFuelUseForm(PredefinedFactorCalculationMethodForm):
    """ DirectElectricityUseForm """
    sold_quantity = forms.IntegerField(required=True)
    product_lifetime = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Hidden(
                "method", self.initial["method"].id
            ),  # field used in the view to preset form
            Hidden("collection", self.initial["collection"].id),
            Hidden("item_type", self.initial["item_type"]),
            Hidden("ghg_scope", self.initial["ghg_scope"]),
            # Hidden("ghg_unit", "kwh"),
            Row(
                Column(
                    Field(
                        "description_user",
                        placeholder=_("Product name"),
                        type="text",
                        autocomplete="off",
                        css_class="form-control form-control-lg form-control-solid mb-3 mb-lg-0",
                    ),
                    css_class="col-md-5",
                ),
            ),
            Row(
                Column(
                    Field(
                        "sold_quantity",
                        placeholder=_("Sold quantity"),
                        min=0,
                        type="number",
                        autocomplete="off",
                    ),
                    css_class="col-2",
                ),
                Column(
                    Field(
                        "ghg_factor",
                        data_control="select2",
                        data_placeholder=_("Sold product country"),
                        hx_post=reverse("ghg_factor_units"),
                        hx_swap="innerHTML",
                        hx_target="#custom_units",
                        hx_trigger="load, change",
                        hx_include="[name='ghg_factor']",
                        style="display: none;",
                        css_class="form-control",
                    ),
                    css_class="col-3",
                ),
                Column(
                    AppendedText(
                        "product_lifetime", _('year'), 
                        placeholder=_("Product lifetime"),
                        css_class="form-control form-control-lg mb-3 mb-lg-0",
                    ),
                    css_class="col-3",
                ),
                Column(
                    Field(
                        "value_float",
                        placeholder=_("energy quantity"),
                        min=0,
                        type="number",
                        autocomplete="off",
                        css_class="form-control form-control-lg mb-3 mb-lg-0",
                    ),
                    css_class="col-3",
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
                    css_class="col-1",
                ),
                Column(
                    Submit("submit", _("Add"), css_class="btn btn-light-primary"),
                    css_class="col",
                ),
            ),
        )
    
    def save(self, commit=True):
        """Save form"""

        instance = super().save(commit=False)

        instance.widget_data = {
            "sold_quantity": self.cleaned_data["sold_quantity"],
            "product_lifetime": self.cleaned_data["product_lifetime"],
        }

        if commit:
            instance.save()

        return instance

    class Meta:
        model = CollectionItem
        fields = [
            "method",
            "collection",
            "item_type",
            "ghg_scope",
            "ghg_unit",
            "ghg_factor",
            "description_user",
            "sold_quantity",
            "product_lifetime",
            "value_float",
        ]

class DirectFuelUseForm(PredefinedFactorCalculationMethodForm):
    """ DirectFuelUseForm """

class FuelsAndFeedstocksForm(PredefinedFactorCalculationMethodForm):
    """ FuelsAndFeedstocksForm """

class EmissionOfGreenhouseGasesForm(ScreeningMethodApproachForm):
    """ EmissionOfGreenhouseGasesForm """

    product_lifetime = forms.IntegerField(required=True)

    def get_extra_fields(self):
        return [
            Column(
                Column(
                    AppendedText(
                        "product_lifetime", _('year'), 
                        placeholder=_("Product lifetime"),
                        css_class="form-control form-control-lg mb-3 mb-lg-0",
                    ),
                    css_class="col",
                ),
            ),
        ]

    def save_extra_fields(self, instance):
        
        return {
            "product_lifetime": self.cleaned_data["product_lifetime"],
        }
