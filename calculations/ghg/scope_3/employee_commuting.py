""" Employee commuting emissions calculation module. """

from ..base.base import BaseCalculationMethod


class TransportationDistanceBasedMethod(BaseCalculationMethod):
    """Transportation by distance"""

class TransportationFuelAmountMethod(BaseCalculationMethod):
    """Transportation by fuel amount"""

class HomeOfficeElectricityUseMethod(BaseCalculationMethod):
    """ Home Office Electricity Use """

class HomeOfficeHeatingNeedsMethod(BaseCalculationMethod):
    """ Home Office Heating Needs """

class HomeOfficeCoolingNeedsMethod(BaseCalculationMethod):
    """ Home Office Cooling Needs """