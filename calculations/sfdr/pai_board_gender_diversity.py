""" board_gender_diversity """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class BoardGenderDiversity(): #pylint: disable=[invalid-name, too-few-public-methods]
    """ board_gender_diversity """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute carbon_footprint 
        
        Formula ???

        Args:
        - assets
        Returns:
        - share_t
        """
        diversity_tot = 0
        for asset in assets:
            #collection = Collection.objects.get(company=asset.company)
            collection = collections.filter(company=asset.company, collection_type='metrics')[0]
            collection_item_gender_board_diversity_pct = CollectionItem.objects.get(
                collection=collection, template__name='gender_board_diversity_pct')

            diversity_i = 0
            if collection_item_gender_board_diversity_pct.value_float:
                diversity_i = collection_item_gender_board_diversity_pct.value_float
            diversity_tot = diversity_tot + diversity_i

        diversity_avrg = diversity_tot / len(assets)
        diversity_avrg = round(diversity_avrg, 2)

        return f'{diversity_avrg:g}'
