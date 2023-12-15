""" ghg_total_tonnes """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)

class TotalGhgEmissions(): #pylint: disable=[invalid-name, too-few-public-methods]
    """ ghg_total_tonnes """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute ghg_intensity_investees 
        
        """

        # ghg_scope_1_tonnes
        collection_items = CollectionItem.objects.filter(collection__in=collections,
            template__name='ghg_scope_1_tonnes')

        ghg_scope_1_t = 0
        for collection_item in collection_items:
            value_i = 0

            # Find related Asset
            current_asset = assets.filter(company=collection_item.collection.company)[0]

            if (current_asset.shares_pct
                and collection_item.value_pint):
                value_i = (current_asset.shares_pct
                           * collection_item.value_pint / 100)
            ghg_scope_1_t =  ghg_scope_1_t + value_i

        # ghg_scope_2_tonnes
        collection_items = CollectionItem.objects.filter(collection__in=collections,
            template__name='ghg_scope_2_tonnes')

        ghg_scope_2_t = 0
        for collection_item in collection_items:
            value_i = 0

            # Find related Asset
            current_asset = assets.filter(company=collection_item.collection.company)[0]

            if (current_asset.shares_pct
                and collection_item.value_pint):
                value_i = (current_asset.shares_pct
                           * collection_item.value_pint / 100)
            ghg_scope_2_t =  ghg_scope_2_t + value_i

        # ghg_scope_3_tonnes
        collection_items = CollectionItem.objects.filter(collection__in=collections,
            template__name='ghg_scope_3_tonnes')

        ghg_scope_3_t = 0
        for collection_item in collection_items:
            value_i = 0

            # Find related Asset
            current_asset = assets.filter(company=collection_item.collection.company)[0]

            if (current_asset.shares_pct
                and collection_item.value_pint):
                value_i = (current_asset.shares_pct
                           * collection_item.value_pint / 100)
            ghg_scope_3_t =  ghg_scope_3_t + value_i

        value_t = (
            float(ghg_scope_1_t)
            + float(ghg_scope_2_t)
            + float(ghg_scope_3_t)
        )
        return f'{value_t:g}'
