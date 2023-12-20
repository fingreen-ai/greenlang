# [Upstream Transportation and Distribution](#upstream-transportation-and-distribution)

### name_fr

Transport et Distribution Amont

### scope

3

### description 

category 4 includes emissions from: 

- Transportation and distribution of products purchased in the reporting year, between a company’s tier 1 suppliers and its own operations in vehicles not owned or operated by the reporting company (including multi-modal shipping where multiple carriers are involved in the delivery of a product, but excluding fuel and energy products) 
- Third-party transportation and distribution services purchased by the reporting company in the reporting year (either directly or through an intermediary), including inbound logistics, outbound logistics (e.g., of sold products), and third-party transportation and distribution between a company’s own facilities. Emissions may arise from the following transportation and distribution activities throughout the value chain: 
- Air transport, Rail transport, Road transport, Marine transport, Storage of purchased products in warehouses, distribution centers, and retail facilities. 

Outbound logistics services purchased by the reporting company are categorized as upstream because they are a purchased service. Emissions from transportation and distribution of purchased products upstream of the reporting company’s tier 1 suppliers (e.g., transportation between a company’s tier 2 and tier 1 suppliers) are accounted for in scope 3, category 1 (Purchased goods and services).


### description_fr

La catégorie 4 inclut les émissions provenant de :

- Le transport et la distribution des produits achetés au cours de l'année de déclaration, entre les fournisseurs de premier niveau de l'entreprise et ses propres opérations dans des véhicules non détenus ni exploités par l'entreprise déclarante (y compris l'expédition multimodale où plusieurs transporteurs sont impliqués dans la livraison d'un produit, à l'exception des produits de carburant et d'énergie).
- Les services de transport et de distribution tiers achetés par l'entreprise déclarante au cours de l'année de déclaration (directement ou par l'intermédiaire d'un intermédiaire), y compris la logistique entrante, la logistique sortante (par exemple, des produits vendus) et le transport et la distribution tiers entre les propres installations de l'entreprise. Les émissions peuvent provenir des activités de transport et de distribution suivantes tout au long de la chaîne de valeur :
- Le transport aérien, le transport ferroviaire, le transport routier, le transport maritime, le stockage des produits achetés dans les entrepôts, les centres de distribution et les points de vente au détail.

Les services de logistique sortante achetés par l'entreprise déclarante sont catégorisés comme amont car il s'agit d'un service acheté. Les émissions provenant du transport et de la distribution des produits achetés en amont des fournisseurs de premier niveau de l'entreprise déclarante (par exemple, le transport entre les fournisseurs de deuxième niveau et de premier niveau de l'entreprise) sont comptabilisées dans la portée 3, catégorie 1 (Biens et services achetés).


## [Distance based method](#distance-based-method)

### name_fr

Méthode basée sur la distance

### description

In the distance-based method for upstream transportation, the key data needed are the distances vehicles travel and the weight of the goods transported. This method is precise and ideal for companies with detailed transport data, allowing for accurate emission calculations. It is most effective when reliable distance and weight information is available

### description_fr

Dans la méthode basée sur la distance pour le transport amont, les données clés nécessaires sont les distances parcourues par les véhicules et le poids des marchandises transportées. Cette méthode est précise et idéale pour les entreprises disposant de données de transport détaillées, permettant des calculs d'émissions précis. Elle est plus efficace lorsque des informations fiables sur la distance et le poids sont disponibles.

### implem_path

greenlang.calculations.ghg.scope_3.upstream_transportation_and_distribution.DistanceBasedMethod

## [Spend-based method](#spend-based-method)

### name_fr

Méthode basée sur les dépenses

### description

The spend-based method relies on financial expenditure data for transportation services, not physical transport metrics. This approach is suitable for companies lacking detailed transport data, providing a simpler, albeit less precise, emissions estimate based on transportation spending.It's a practical alternative when detailed distance and weight information is unavailable.

### description_fr

La méthode basée sur les dépenses repose sur les données de dépenses financières pour les services de transport, et non sur les mesures de transport physique. Cette approche convient aux entreprises qui ne disposent pas de données de transport détaillées, fournissant une estimation des émissions plus simple, mais moins précise, basée sur les dépenses de transport. C'est une alternative pratique lorsque des informations détaillées sur la distance et le poids ne sont pas disponibles.

### implem_path

greenlang.calculations.ghg.scope_3.upstream_transportation_and_distribution.SpendBasedMethod

## [Fuel Amount Method](#fuel-amount-method)

### name_fr

Méthode basée sur la consommation de carburant

### description

The "fuel amount" method for calculating emissions is a direct approach that relies on actual fuel consumption data. This method involves calculating emissions, such as CO2, based on the quantity of fuel used by vehicles. To implement this approach effectively, access to detailed records is essential, including fuel consumption logs, gas station data, or vehicle mileage. The precision of this method is particularly high when accurate and specific fuel usage data is available. The "fuel amount" method provides a granular understanding of emissions by directly tying them to real-world fuel consumption.

### description_fr

La méthode basée sur la quantité de carburant pour le calcul des émissions est une approche directe qui repose sur des données réelles de consommation de carburant. Cette méthode consiste à calculer les émissions, telles que le CO2, en fonction de la quantité de carburant utilisée par les véhicules. Pour mettre en œuvre cette approche de manière efficace, l'accès à des dossiers détaillés est essentiel, notamment des journaux de consommation de carburant, des données de stations-service ou des kilométrages des véhicules. La précision de cette méthode est particulièrement élevée lorsque des données de consommation de carburant précises et spécifiques sont disponibles. Celle-ci offre une compréhension granulaire des émissions en les reliant directement à la consommation de carburant du monde réel.

### implem_path

greenlang.calculations.ghg.scope_3.upstream_transportation_and_distribution.FuelAmountMethod