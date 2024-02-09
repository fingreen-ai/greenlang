""" Implementations of the investments category calculations methods."""
from fingreen_web.models import GhgEmissionFactorValue

from ..base.base import BaseCalculationMethod
from .forms.investments import (ProjectSpecificMethodForm,
                                AverageSpecificMethodForm,
                                LongTermFinancedProjectSpecificMethodForm)

class ProjectSpecificMethod(BaseCalculationMethod):
    """ The specific method for calculating the equity investments category."""

    @property
    def form_class(self):
        """Return form class."""
        return ProjectSpecificMethodForm

    def compute(self, collection_item):
        return super().compute(collection_item) / 100 # The amount is a percentage

    def explain(self, collection_item):
        """Return formula html."""

        factor_value = GhgEmissionFactorValue.objects.get(
            factor=collection_item.ghg_factor,
            unit=collection_item.ghg_unit
        )

        text = f"""
Share of equity = {self.amount(collection_item)} %<br>
Project Scope 1 emissions = {collection_item.widget_data['scope1_emissions']} kg CO2<br>
Project Scope 2 emissions = {collection_item.widget_data['scope2_emissions']} kg CO2<br>
<br>

Calculus :<br>     
Total emissions = Share of equity * (Scope 1 emissions + Scope 2 emissions) = {self.amount(collection_item)} * ({collection_item.widget_data['scope1_emissions']} + {collection_item.widget_data['scope2_emissions']}) = {self.compute(collection_item)} kg CO2
<br><br>
Source : Custom<br>
Source year : {factor_value.data_source_year}
        
        """

        return text

class AverageDataMethod(BaseCalculationMethod):
    """ The average data method for calculating the equity investments category."""

    @property
    def form_class(self):
        """Return form class."""
        return AverageSpecificMethodForm

    def compute(self, collection_item):
        return super().compute(collection_item) * collection_item.widget_data['equity_share'] / 100 # The amount is a percentage

    def explain(self, collection_item):
        """Return formula html."""

        factor_value = GhgEmissionFactorValue.objects.get(
            factor=collection_item.ghg_factor,
            unit=collection_item.ghg_unit
        )

        text =  f"""
Amount declared by company = {self.amount(collection_item)} {factor_value.get_unit_display()}<br>\
GHG emission factor value = {factor_value.tot_co2_kg} kg CO2/{factor_value.get_unit_display()}<br>\
Share of equity = {collection_item.widget_data['equity_share']} %<br>
        """

        if factor_value.factor.factor_type in ['goods', 'services']:
            text += f"""
<br>
For GHG factor which are goods or services, we apply an inflaction rate of 7% per year to the GHG emission factor value.<br>
Updated GHG emission factor value = {round(self.total_co2(collection_item), 5)} kg CO2/{factor_value.get_unit_display()}<br>
<br><br>
            """

        text += f"""
Calculus : {collection_item.widget_data['equity_share']} * {self.amount(collection_item)} {factor_value.get_unit_display()} x {self.total_co2(collection_item)} kg CO2/{factor_value.get_unit_display()} / 1000 = {round(self.compute(collection_item), 5)} tonnes CO2\
<br><br>
Source : {factor_value.data_source}<br>
Source year : {factor_value.data_source_year}
        """

        return text


class LongTermFinancedProjectSpecificMethod(BaseCalculationMethod):
    """ The specific method for calculating the long-term financed projects category."""

    @property
    def form_class(self):
        """Return form class."""
        return LongTermFinancedProjectSpecificMethodForm

    def compute(self, collection_item):
        return super().compute(collection_item) * collection_item.widget_data['equity_share'] / 100

    def explain(self, collection_item):
        """Return formula html."""

        factor_value = GhgEmissionFactorValue.objects.get(
            factor=collection_item.ghg_factor,
            unit=collection_item.ghg_unit
        )

        text =  f"""
Expected lifetime of project = {self.amount(collection_item)} {factor_value.get_unit_display()}<br>\
Expected annual emissions = {factor_value.tot_co2_kg} kg CO2/{factor_value.get_unit_display()}<br>\
Share of equity = {collection_item.widget_data['equity_share']} %<br><br>
        """

        text += f"""
Calculus : {collection_item.widget_data['equity_share']}/100 * {self.amount(collection_item)} {factor_value.get_unit_display()} x {self.total_co2(collection_item)} kg CO2/{factor_value.get_unit_display()} / 1000 = {round(self.compute(collection_item), 5)} tonnes CO2\
<br><br>
Source : Custom<br>
Source year : {factor_value.data_source_year}
        """

        return text
    