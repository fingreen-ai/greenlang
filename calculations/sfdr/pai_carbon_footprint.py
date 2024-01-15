""" carbon_footprint """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class CarbonFootprint(): #pylint: disable=[invalid-name, too-few-public-methods]
    """ carbon_footprint """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute carbon_footprint 
        
        Formula ???

        Args:
        - assets
        Returns:
        - share_t
        """
        value_t = 0
        for asset in assets:
            # Get spcope 1, 2, 3 ghg emissions
            #collection = Collection.objects.get(company=asset.company)
            collection = collections.filter(company=asset.company, collection_type='metrics')[0]
            collection_items_ghg_1 = CollectionItem.objects.get(collection=collection,
                                                    template__name='ghg_scope_1_tonnes')
            collection_items_ghg_2 = CollectionItem.objects.get(collection=collection,
                                                    template__name='ghg_scope_2_tonnes')
            collection_items_ghg_3 = CollectionItem.objects.get(collection=collection,
                                                    template__name='ghg_scope_3_tonnes')
            if collection_items_ghg_1.value_pint is None:
                collection_items_ghg_1.value_pint = 0
            if collection_items_ghg_2.value_pint is None:
                collection_items_ghg_2.value_pint = 0
            if collection_items_ghg_3.value_pint is None:
                collection_items_ghg_3.value_pint = 0

            ghg_tot = (collection_items_ghg_1.value_pint
                    + collection_items_ghg_2.value_pint
                    + collection_items_ghg_3.value_pint)
            value_i = asset.shares_pct * ghg_tot / 100
            value_t =  value_t + value_i

        value_t = value_t / invest_value_tot * 1000000
        value_t = round(value_t, 2)

        return f'{value_t:g}'
