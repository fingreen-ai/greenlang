""" Calculation method for scope 3, capital goods  """
from ..base.forms import CustomAverageDataMethodForm, SupplierSpecificMethodForm
from .purchased_goods_and_services import (
    SpendBasedMethod as PurchasedGoodsAndServicesSpendBasedMethod,
    SupplierSpecificMethod as PurchasedGoodsAndServicesSupplierSpecificMethod,
    AverageDataMethod as PurchasedGoodsAndServicesAverageDataMethod)


class SpendBasedMethod(PurchasedGoodsAndServicesSpendBasedMethod):
    """Spend-based method"""


class SupplierSpecificMethod(PurchasedGoodsAndServicesSupplierSpecificMethod):
    """Supplier specific method"""

    @property
    def form_class(self):
        """Return form class"""
        return SupplierSpecificMethodForm


class AverageDataMethod(PurchasedGoodsAndServicesAverageDataMethod):
    """Average data method"""

    @property
    def form_class(self):
        """Return form class"""
        return CustomAverageDataMethodForm
