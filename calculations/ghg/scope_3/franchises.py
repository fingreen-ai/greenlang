""" Franchises implementation  """

from .leased_assets import LeasedBuildingsAssetSpecificMethod, LeasedBuildingsAverageDataMethod

class FranchiseSpecificMethod(LeasedBuildingsAssetSpecificMethod):
    """Franchises - Specific method"""

class AverageDataMethod(LeasedBuildingsAverageDataMethod):
    """Franchises - Average data method"""
