""" GHG - Scope 3 - Use of sold products calculations. """

from ..base.base import BaseCalculationMethod
from ..scope_1.fugitive_emissions import ScreeningMethodApproach
from .forms.use_of_sold_products import (
    DirectElectricityOrFuelUseForm,
    EmissionOfGreenhouseGasesForm,
)

from fingreen_web.models import (
    GhgEmissionFactor,
    GhgEmissionFactorValue,
)


class DirectElectricityOrFuelUse(BaseCalculationMethod):
    """ DirectElectricityUse """

    @property
    def form_class(self):
        """Return form class."""
        return DirectElectricityOrFuelUseForm

    def compute(self, collection_item):
        """Compute."""
        sold_quantity = collection_item.widget_data["sold_quantity"]
        product_lifetime = collection_item.widget_data["product_lifetime"]

        print(f"{sold_quantity} * {product_lifetime} * {self.total_co2(collection_item)} * {self.amount(collection_item) }/ 1000")

        return sold_quantity * product_lifetime * self.total_co2(collection_item) * self.amount(collection_item) / 1000


    # def explain(self, collection_item):
    #     """Return formula html."""

class FuelsAndFeedstocks(BaseCalculationMethod):
    """ FuelsAndFeedstocks """


class EmissionOfGreenhouseGases(ScreeningMethodApproach):
    """ EmissionOfGreenhouseGases """

    @property
    def form_class(self):
        """Return form class."""
        return EmissionOfGreenhouseGasesForm

    def amount(self, collection_item):
        """Return amount."""
        amount = super().amount(collection_item)
        return amount * collection_item.widget_data["product_lifetime"]
    
    def explain(self, collection_item):
        factor_value = GhgEmissionFactorValue.objects.get(
            factor=collection_item.ghg_factor, unit=collection_item.ghg_unit
        )

        emission_source_gwp = factor_value.tot_co2_kg

        gas_id = collection_item.widget_data.get("gas")
        gas = GhgEmissionFactor.objects.get(id=gas_id)
        gas_gwp = gas.values.get(unit="kg").tot_co2_kg

        quantity = collection_item.widget_data.get("quantity")
        capacity = collection_item.value_float

        product_lifetime = collection_item.widget_data["product_lifetime"]

        text = f"\
        GHG emission factor value ({factor_value.factor.name}) = {emission_source_gwp} kg CO2/kg<br>\
        Gas emission factor value ({gas.name}) = {gas_gwp} kg CO2/kg<br>\
        <br>\
        Quantity = {quantity} units<br>\
        Refrigerant or Gas Capacity = {capacity} kg<br>\
        Product Lifetime = {product_lifetime} years<br>\
        <br>\
        Total Emissions = {quantity} * {capacity} * {product_lifetime} = {self.amount(collection_item)} kg<br>\
        <br>\
        "

        text += f"\
        Calculus : {emission_source_gwp} kg CO2/kg x {gas_gwp} kg CO2/kg x {quantity} kg x {capacity} units x  {product_lifetime} years / 1000 = {round(self.compute(collection_item), 5)} tonnes CO2\
        <br>\
        <br>\
        Data source : {factor_value.data_source}<br>\
        Data source year : {factor_value.data_source_year}<br>\
        "

        return text
