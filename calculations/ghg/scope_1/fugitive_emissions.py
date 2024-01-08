"""
Category 2 : Fugitive Emission calculation implementations
"""
from django.utils.translation import gettext_lazy as _

from fingreen_web.models import (
    GhgEmissionFactor,
    GhgEmissionFactorValue,
)
from ..base.base import BaseCalculationMethod
from .forms import MassBalanceMethodForm, ScreeningMethodApproachForm


class MassBalanceMethod(BaseCalculationMethod):
    """Spend-based method"""

    @property
    def form_class(self):
        """Return form class."""
        return MassBalanceMethodForm

    def explain(self, collection_item):
        """Return formula html."""
        factor_value = GhgEmissionFactorValue.objects.get(
            factor=collection_item.ghg_factor, unit=collection_item.ghg_unit
        )

        begin = collection_item.widget_data.get("begin_year_storage")
        end = collection_item.widget_data.get("end_year_storage")
        decrease = begin - end

        purchased = collection_item.widget_data.get("purchased")
        acquired = collection_item.widget_data.get("acquired")
        available = purchased + acquired

        text = f"\
        GHG emission factor value ({factor_value.factor.name}) = {factor_value.tot_co2_kg} kg CO2/{factor_value.get_unit_display()}<br>\
        <br>\
        Inventory at the beginning of the year (A) = {begin} kg<br>\
        Inventory at the end of the year (B) = {end} kg<br>\
        Decrease during the year (C = A - B) = {decrease} kg<br>\
        <br>\
        Purchased from producers/distributors in bulk (D) = {purchased} kg<br>\
        Added to equipment by contractors (E) = {acquired} kg<br>\
        Total Purchases/ Acquisitions (F = D + E) = {available} kg<br>\
        <br>\
        Total Emissions (C + F) = {collection_item.value_float} kg<br>\
        <br>\
        "

        text += f"\
        Calculus : {collection_item.value_float} {factor_value.get_unit_display()} x {self.total_co2(collection_item)} kg CO2/{factor_value.get_unit_display()} / 1000 = {round(self.compute(collection_item), 5)} tonnes CO2\
        <br>\
        <br>\
        Data source : {factor_value.data_source}<br>\
        Data source year : {factor_value.data_source_year}<br>\
        "

        return text


class ScreeningMethodApproach(BaseCalculationMethod):
    """Screening method approach"""

    @property
    def form_class(self):
        """Return form class."""
        return ScreeningMethodApproachForm

    def amount(self, collection_item):
        """Return amount."""
        quantity = collection_item.widget_data.get("quantity")
        capacity = collection_item.value_float

        return quantity * capacity

    def compute(self, collection_item):
        """Return total co2."""

        emission_source = collection_item.ghg_factor
        emission_source_gwp = emission_source.values.get(unit="kg").tot_co2_kg

        gas_id = collection_item.widget_data.get("gas")
        gas = GhgEmissionFactor.objects.get(id=gas_id)
        gas_gwp = gas.values.get(unit="kg").tot_co2_kg

        return emission_source_gwp * gas_gwp * self.amount(collection_item) / 1000

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

        text = f"\
        GHG emission factor value ({factor_value.factor.name}) = {emission_source_gwp} kg CO2/kg<br>\
        Gas emission factor value ({gas.name}) = {gas_gwp} kg CO2/kg<br>\
        <br>\
        Quantity = {quantity} units<br>\
        Operating Units Refrigerant or Gas Capacity = {capacity} kg<br>\
        <br>\
        Total Emissions = {quantity} * {capacity} = {self.amount(collection_item)} kg<br>\
        <br>\
        "

        text += f"\
        Calculus : {emission_source_gwp} kg CO2/kg x {gas_gwp} kg CO2/kg x {quantity} kg x {capacity} units / 1000 = {round(self.compute(collection_item), 5)} tonnes CO2\
        <br>\
        <br>\
        Data source : {factor_value.data_source}<br>\
        Data source year : {factor_value.data_source_year}<br>\
        "

        return text
