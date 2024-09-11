# [Purchased Heat or Steam](#purchased-heat-or-steam)

### scope

2

### name_fr

Chaleur achetée

### description

Scope 2 is an indirect emission category that includes GHG emissions from the generation of purchased or acquired steam, heat, or cooling consumed by the reporting company. GHGs are emitted when fossil fuels are combusted to generate electricity. Companies account for their responsibility for these emissions by reporting them as scope 2 indirect emissions. If the organization purchases heat or steam, the emissions are accounted for as scope 2 indirect emissions. Also similar to electricity, both the location-based method and the market-based method should be calculated and reported. Typically supplier-specific emission factors for steam will apply to both location-based and market-based emissions.

### description_fr

La portée 2 est une catégorie d'émissions indirectes qui comprend les émissions de gaz à effet de serre (GES) provenant de la production de vapeur, de chaleur ou de refroidissement achetés ou acquis et consommés par l'entreprise déclarante. Les GES sont émis lorsque des combustibles fossiles sont brûlés pour produire de l'électricité. Les entreprises rendent compte de leur responsabilité pour ces émissions en les signalant en tant qu'émissions indirectes de portée 2. Si l'organisation achète de la chaleur ou de la vapeur, les émissions sont comptabilisées en tant qu'émissions indirectes de portée 2. Tout comme pour l'électricité, tant la méthode basée sur la localisation que la méthode basée sur le marché doivent être calculées et signalées. En général, les facteurs d'émission spécifiques au fournisseur s'appliqueront aux émissions basées sur la localisation et sur le marché pour la vapeur.

## [Location Based Method](#location-based-method)

### name_fr

Méthode basée sur la localisation

### description

A location-based emission factor for such systems should characterize the average GHG intensity of the fuels used to generate the heat/steam/cooling, as well as the efficiency of that generation.

### description_fr

Un facteur d'émission basé sur la localisation pour de tels systèmes devrait caractériser l'intensité moyenne des GES des combustibles utilisés pour produire la chaleur, la vapeur ou le refroidissement, ainsi que l'efficacité de cette production.

### implem_path

greenlang.calculations.ghg.scope_2.purchased_heat_or_steam.LocationBasedMethod

## [Marked Based Method](#marked-based-method)

### name_fr

Méthode basée sur le marché

### description

Market based methods reflects heat/steam supplier, such as a regulated utility or a deregulated supplier, may provide information to its customers on the emission factor associated with its energy product.

### description_fr

Les méthodes basées sur le marché reflètent le fournisseur de chaleur/vapeur, tel qu'un service public réglementé ou un fournisseur déréglementé, peuvent fournir des informations à ses clients sur le facteur d'émission associé à son produit énergétique.

### implem_path

greenlang.calculations.ghg.scope_2.purchased_heat_or_steam.MarketBasedMethod