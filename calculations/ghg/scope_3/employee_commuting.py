""" Employee commuting emissions calculation module. """

from ..base.base import BaseCalculationMethod
from ..base.forms import CustomFactorCalculationMethodForm


class DistanceBasedMethod(BaseCalculationMethod):
    """Distance based method"""


class EquipmentBasedMethod(BaseCalculationMethod):
    """Equipment based method"""

class FuelAmountMethod(BaseCalculationMethod):
    """Fuel amount method"""