""" Employee commuting emissions calculation module. """

from ..base.base import BaseCalculationMethod
from ..base.forms import CustomFactorCalculationMethodForm


class DistanceBasedMethod(BaseCalculationMethod):
    """Distance based method"""


class EquipmentBasedMethod(BaseCalculationMethod):
    """Equipment based method"""


class AverageDataMethod(BaseCalculationMethod):
    """Average data method"""

    @property
    def form_class(self):
        """Return form class."""
        return CustomFactorCalculationMethodForm
