"""
Base classes for calculation methods
"""
import logging
from datetime import datetime

from django.utils.translation import gettext_lazy as _

from fingreen_web.models import GhgEmissionFactorValue

from .forms import PredefinedFactorCalculationMethodForm

logger = logging.getLogger(__name__)

class BaseCalculationMethod:
    """ 
    This is the base class for all calculation methods.
    All lot of categories are using this class because they are using a predefined factor.
    In term of form, the user has to select a GHG emission factor, a GHG emission unit and a amount.
    """

    @property
    def form_class(self):
        """ 
        Return form class to use for this calculation method.
        The form is responsible both of the displayed inputs both of the validation and the saving, if so.

        Returns:
            The form class to use for this calculation method.
        """
        return PredefinedFactorCalculationMethodForm

    def amount(self, collection_item):
        """ 
        Return the amount value of the related ghg emission factor. 

        Args:
            collection_item: the collection item where the amount value is stored.

        Returns:
            The amount value, as float number, of the related ghg emission factor.
        """
        return collection_item.value_float

    def total_co2(self, factor_value):
        """ 
        The total co2 value for the given GHG emission factor value.

        Args:
            factor_value: GHG emission factor value

        Returns:
            The total co2 value, as float number, for the given GHG emission factor value.
            If the GHG emission factor value is a goods or services, the total co2 value is updated
            with an inflaction rate. For the moment, the inflaction rate is hard-coded :
            7% per year.
        """

        current_year = datetime.now().year

        if factor_value.factor.factor_type in ['goods', 'services']:
            # If the data source year is not the current year, the tot_co2_kg value could be outdated. #pylint: disable=line-too-long
            # According Simge, a kind of inflaction rate should be applied to the tot_co2_kg value.
            # In her example, the inflaction rate is 0.7 per year.

            year_diff = current_year - factor_value.data_source_year
            rate = 1+(0.07 * year_diff)
            return factor_value.tot_co2_kg / rate

        return factor_value.tot_co2_kg


    def compute(self, collection_item):
        """ Compute.
        """
        factor_value = GhgEmissionFactorValue.objects.get(factor=collection_item.ghg_factor,
                    unit=collection_item.ghg_unit)

        return self.amount(collection_item) * self.total_co2(factor_value) / 1000

    def explain(self, collection_item):
        """ Return calculation explanation in human readable format.
        Basically, it's displaying the amount, the GHG emission factor value and the total co2 value.
        It's also mentionning the data source and the data source year.
        args:
            collection_item: the collection item where informations are stored.
        returns:
            Calculation explanation in human readable format.

        """
        factor_value = GhgEmissionFactorValue.objects.get(
            factor=collection_item.ghg_factor,
            unit=collection_item.ghg_unit
        )

        text =  f"\
        Amount declared by company = {self.amount(collection_item)} {factor_value.get_unit_display()}<br>\
        GHG emission factor value = {factor_value.tot_co2_kg} kg CO2/{factor_value.get_unit_display()}<br>\
        "

        if factor_value.factor.factor_type in ['goods', 'services']:
            text += f"\
            <br>\
            For GHG factor which are goods or services, we apply an inflaction rate of 7% per year to the GHG emission factor value.<br>\
            Updated GHG emission factor value = {round(self.total_co2(factor_value), 5)} kg CO2/{factor_value.get_unit_display()}<br>\
            <br>\
            "

        text += f"\
        Calculus : {self.amount(collection_item)} {factor_value.get_unit_display()} x {self.total_co2(factor_value)} kg CO2/{factor_value.get_unit_display()} / 1000 = {round(self.compute(collection_item), 5)} tonnes CO2\
        <br>\
        <br>\
        Data source : {factor_value.data_source}<br>\
        Data source year : {factor_value.data_source_year}<br>\
        "

        return text
