# [Downstream Transportation and Distribution](#downstream-transportation-and-distribution)

### name_fr

Transport et distribution en aval

### scope

3

### description 

This category includes emissions that occur in the reporting year from transportation and distribution of sold products in vehicles and facilities not owned or controlled by the reporting company. This category also includes emissions from retail and storage. Outbound transportation and distribution services that are purchased by the reporting company are excluded from category 9 and included in category 4 (Upstream transportation and distribution) because the reporting company purchases the service. Category 9 includes only emissions from transportation and distribution of products after the point of sale. Emissions from downstream transportation and distribution can arise from transportation/storage of sold products in vehicles/facilities not owned by the reporting company. 

For example:

- Warehouses and distribution centers
- Retail facilities
- Air transport
- Rail transport
- Road transport
- Marine transport.  

If the reporting company sells an intermediate product, the company should report emissions from transportation and distribution of this intermediate product between the point of sale by the reporting company and either (1) the end consumer (if the eventual end use of the intermediate product is known) or (2) business customers (if the eventual end use of the intermediate product is unknown).


### description_fr

Cette catégorie comprend les émissions qui se produisent au cours de l'année de déclaration du transport et de la distribution des produits vendus dans des véhicules et des installations non détenus ou contrôlés par l'entreprise déclarante. Cette catégorie comprend également les émissions du commerce de détail et du stockage. Les services de transport et de distribution sortants achetés par l'entreprise déclarante sont exclus de la catégorie 9 et inclus dans la catégorie 4 (Transport et distribution en amont) car l'entreprise déclarante achète le service. La catégorie 9 comprend uniquement les émissions du transport et de la distribution de produits après le point de vente. Les émissions du transport et de la distribution en aval peuvent provenir du transport/stockage de produits vendus dans des véhicules/installations non détenus par l'entreprise déclarante.

Par exemple:

- Entrepôts et centres de distribution
- Installations de vente au détail
- Transport aérien
- Transport ferroviaire
- Transport routier
- Transport maritime.

Si l'entreprise déclarante vend un produit intermédiaire, elle doit déclarer les émissions du transport et de la distribution de ce produit intermédiaire entre le point de vente par l'entreprise déclarante et soit (1) le consommateur final (si l'utilisation finale éventuelle du produit intermédiaire est connue) ou (2) les clients professionnels (si l'utilisation finale éventuelle du produit intermédiaire est inconnue).




## [Distance based method](#distance-based-method)

### name_fr

Méthode basée sur la distance

### description

In the distance-based method for downstream transportation, the key data needed are the distances vehicles travel and the weight of the goods transported. This method is precise and ideal for companies with detailed transport data, allowing for accurate emission calculations. It is most effective when reliable distance and weight information is available.

### description_fr

Dans la méthode basée sur la distance pour le transport en aval, les données clés nécessaires sont les distances parcourues par les véhicules et le poids des marchandises transportées. Cette méthode est précise et idéale pour les entreprises disposant de données de transport détaillées, permettant des calculs d'émissions précis. Elle est plus efficace lorsque des informations fiables sur la distance et le poids sont disponibles.

### implem_path

greenlang.calculations.ghg.scope_3.downstream_transportation_and_distribution.DistanceBasedMethod

## [Spend-based method](#spend-based-method)

### name_fr

Méthode basée sur les dépenses

### description

The spend-based method relies on financial expenditure data for transportation services, not physical transport metrics. This approach is suitable for companies lacking detailed transport data, providing a simpler, albeit less precise, emissions estimate based on transportation spending.It's a practical alternative when detailed distance and weight information is unavailable.

### description_fr

La méthode basée sur les dépenses repose sur les données de dépenses financières pour les services de transport, et non sur les mesures physiques de transport. Cette approche convient aux entreprises qui ne disposent pas de données de transport détaillées, fournissant une estimation des émissions plus simple, mais moins précise, basée sur les dépenses de transport. C'est une alternative pratique lorsque des informations détaillées sur la distance et le poids ne sont pas disponibles.

### implem_path

greenlang.calculations.ghg.scope_3.downstream_transportation_and_distribution.SpendBasedMethod

