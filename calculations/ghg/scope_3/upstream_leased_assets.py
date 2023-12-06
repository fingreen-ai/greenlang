""" Upstream Leased Assets calculation methods """

from ..base.base import BaseCalculationMethod
from .forms.upstream_leased_assets import (
    LeasedBuildingsAssetSpecificMethodForm,
    LeasedBuildingsAverageDataMethodForm,
)


class LeasedBuildingsAssetSpecificMethod(BaseCalculationMethod):
    """Leased Buildings - Asset Specific method"""

    @property
    def form_class(self):
        """Return form class."""
        return LeasedBuildingsAssetSpecificMethodForm

    def total_co2(self, factor_value):
        """Return total co2.
        Can not be used because there are 2 total_co2, one for scope 1 and one for scope 2.
        """
        return 1

    def compute(self, collection_item):
        """Compute."""
        scope1_emissions = collection_item.widget_data["scope1_emissions"]
        scope2_emissions = collection_item.widget_data["scope2_emissions"]

        return self.amount(collection_item) * (scope1_emissions + scope2_emissions)

    def explain(self, collection_item):
        """Return formula html."""
        leased_ratio = (
            collection_item.widget_data["total_floor_space"]
            / collection_item.widget_data["total_floor_space"]
        )
        leased_ratio_per_year = (
            leased_ratio * collection_item.widget_data["leased_month_count"] / 12
        )

        text = f"\
        Total floor space = {collection_item.widget_data['total_floor_space']} m2<br>\
        Leased floor space = {collection_item.widget_data['leased_floor_space']} m2<br>\
        Leased month count = {collection_item.widget_data['leased_month_count']} months<br>\
        Scope 1 emissions = {collection_item.widget_data['scope1_emissions']} kg CO2<br>\
        Scope 2 emissions = {collection_item.widget_data['scope2_emissions']} kg CO<br>\
        <br>\
        "
        text += f"""
Calculus : 
Leased ratio = Leased floor space / Total floor space = {collection_item.widget_data['leased_floor_space']} / {collection_item.widget_data['total_floor_space']} = {leased_ratio} m2<br>
Leased ratio per year = Leased ratio * Leased month count / 12 = {leased_ratio} * collection_item.widget_data['leased_month_count'] / 12 = {leased_ratio_per_year} m2/year<br>
Total Emissions = Leased ratio per year * (Scope 1 emissions + Scope 2 emissions) = {leased_ratio_per_year} * ({collection_item.widget_data['scope1_emissions']} + {collection_item.widget_data['scope2_emissions']}) = {self.compute(collection_item)} kg CO2
<br>
        """

        return text



class LeasedBuildingsAverageDataMethod(BaseCalculationMethod):
    """Leased Buildings - Average-data method"""

    @property
    def form_class(self):
        """Return form class."""
        return LeasedBuildingsAverageDataMethodForm

    def compute(self, collection_item):
        """Compute."""
        leased_month_count = collection_item.widget_data["leased_month_count"]

        return super().compute(collection_item) * leased_month_count / 12


class LeasedVehiclesFuelAmountMethod(BaseCalculationMethod):
    """Leased Vehicles - Fuel Amount method"""


class LeasedVehiclesVehicleTypeMethod(BaseCalculationMethod):
    """Leased Vehicles - Vehicle Type method"""
