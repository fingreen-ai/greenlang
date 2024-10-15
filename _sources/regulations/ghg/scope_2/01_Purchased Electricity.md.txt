# [Purchased Electricity](#purchased-electricity)

### scope

2

### name_fr

Électricité achetée

### description

Scope 2 is an indirect emission category that includes GHG emissions from the generation of purchased or acquired electricity. GHGs are emitted when fossil fuels are combusted to generate electricity. Companies account for their responsibility for these emissions by reporting them as scope 2 indirect emissions. Emissions from both the location-based method and the market-based method, and both totals should be reported

### description_fr

La portée 2 est une catégorie d'émissions indirectes qui comprend les émissions de gaz à effet de serre (GES) provenant de la production d'électricité achetée ou acquise. Les GES sont émis lorsque des combustibles fossiles sont brûlés pour générer de l'électricité. Les entreprises rendent compte de leur responsabilité pour ces émissions en les signalant comme émissions indirectes de portée 2. Les émissions provenant à la fois de la méthode basée sur la localisation et de la méthode basée sur le marché doivent être signalées, ainsi que leurs totaux.

## [Location Based Method](#location-based-method)

### name_fr

Méthode basée sur la localisation

### description

The Location-Based method uses average emission factors for the electricity grids that are providing electricity to the facility. That is, the Location-Based approach considers average emissions intensities in the locations of electricity use, while the Market-Based approach considers the emissions intensities of electricity products that the processor has specifically chosen.

### description_fr

La méthode basée sur la localisation utilise des facteurs d'émission moyens pour les réseaux électriques qui fournissent de l'électricité à l'installation. Autrement dit, l'approche basée sur la localisation prend en compte les intensités moyennes d'émissions dans les endroits où l'électricité est utilisée, tandis que l'approche basée sur le marché prend en compte les intensités d'émissions des produits électriques spécifiquement choisis par l'entreprise.

### implem_path

greenlang.calculations.ghg.scope_2.purchased_electricity.LocationBasedMethod

## [Marked Based Method](#marked-based-method)

### name_fr

Méthode basée sur le marché

### description

The Market-Based method reflects the GHG emissions associated with the specific choices a consumer (a dairy processor) makes regarding its electricity supplier or product, as conveyed through contractual agreements between the processor and the provider. The emission factors are supplier-specific emission factors, or the emissions profiles associated with renewable energy credits (RECs) and power purchase agreements (PPAs).

### description_fr

La méthode basée sur le marché reflète les émissions de gaz à effet de serre associées aux choix spécifiques qu'un consommateur (un transformateur de produits laitiers) fait en ce qui concerne son fournisseur d'électricité ou son produit, tels qu'ils sont stipulés dans les accords contractuels entre le transformateur et le fournisseur. Les facteurs d'émission sont des facteurs d'émission spécifiques au fournisseur ou les profils d'émissions associés aux crédits d'énergie renouvelable (REC) et aux accords d'achat d'électricité (PPA).

### implem_path

greenlang.calculations.ghg.scope_2.purchased_electricity.MarketBasedMethod