"""Upstream transportation and distribution"""

from ..base.base import BaseCalculationMethod
from .purchased_goods_and_services import (
    SpendBasedMethod as PurchasedGoodsAndServicesSpendBasedMethod,
)


class SpendBasedMethod(PurchasedGoodsAndServicesSpendBasedMethod):
    """Spend-based method"""


class DistanceBasedMethod(BaseCalculationMethod):
    """Distance based method"""

class FuelAmountMethod(BaseCalculationMethod):
    """Fuel amount method"""