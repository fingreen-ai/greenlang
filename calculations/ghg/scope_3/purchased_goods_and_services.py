"""Calculation methods for Purchased Goods and Services emission sources """
from ..base.base import BaseCalculationMethod
from ..base.forms import SupplierSpecificMethodForm


class SpendBasedMethod(BaseCalculationMethod):
    """Spend-based method"""


class SupplierSpecificMethod(BaseCalculationMethod):
    """Supplier specific method"""

    @property
    def form_class(self):
        """Return form class"""
        return SupplierSpecificMethodForm


class AverageDataMethod(BaseCalculationMethod):
    """Average data method"""
