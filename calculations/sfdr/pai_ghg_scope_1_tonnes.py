""" ghg_scope_1_tonnes """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class Scope1GhgEmissions(): #pylint: disable=[invalid-name, too-few-public-methods]
    """ ghg_scope_1_tonnes """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute ghg_scope_1_tonnes 
        
        Formula ???

        Args:
        - assets
        Returns:
        - share_t
        """
        collection_items = CollectionItem.objects.filter(collection__in=collections,
            template__name='ghg_scope_1_tonnes')

        value_t = 0
        for collection_item in collection_items:
            value_i = 0

            # Find related Asset
            current_asset = assets.filter(company=collection_item.collection.company)[0]
            if (current_asset.shares_pct
                and collection_item.value_pint):
                value_i = (current_asset.shares_pct
                           * collection_item.value_pint / 100)
            value_t =  value_t + value_i

        return f'{value_t:g}'
