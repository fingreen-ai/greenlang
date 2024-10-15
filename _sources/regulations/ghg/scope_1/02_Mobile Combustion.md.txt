# [Mobile Combustion](#mobile-combustion)

### scope

1

### name_fr

Combustion mobile

### description 
Mobile sources, like owned or leased cars and heavy duty vehicles generate emissions by burning fuel. The fuel usage for any vehicle that is under the organization's operational control should be reported here as scope 1 emissions.

### description_fr

Les sources mobiles, telles que les voitures possédées ou louées et les véhicules lourds, génèrent des émissions en brûlant du carburant. L'utilisation de carburant pour tout véhicule qui est sous le contrôle opérationnel de l'organisation devrait être signalée ici en tant qu'émissions de portée 1.


## [Fuel Amount Method](#fuel-amount-method)

### name_fr

Méthode basée sur la consommation de carburant

### description

The "fuel amount" method for calculating emissions is a direct approach that relies on actual fuel consumption data. This method involves calculating emissions, such as CO2, based on the quantity of fuel used by vehicles. To implement this approach effectively, access to detailed records is essential, including fuel consumption logs, gas station data, or vehicle mileage. The precision of this method is particularly high when accurate and specific fuel usage data is available. The "fuel amount" method provides a granular understanding of emissions by directly tying them to real-world fuel consumption.

### description_fr

La méthode basée sur la quantité de carburant pour le calcul des émissions est une approche directe qui repose sur des données réelles de consommation de carburant. Cette méthode consiste à calculer les émissions, telles que le CO2, en fonction de la quantité de carburant utilisée par les véhicules. Pour mettre en œuvre cette approche de manière efficace, l'accès à des dossiers détaillés est essentiel, notamment des journaux de consommation de carburant, des données de stations-service ou des kilométrages des véhicules. La précision de cette méthode est particulièrement élevée lorsque des données de consommation de carburant précises et spécifiques sont disponibles. Celle-ci offre une compréhension granulaire des émissions en les reliant directement à la consommation de carburant du monde réel.

### implem_path

greenlang.calculations.ghg.scope_1.mobile_combustion.FuelAmountMethod

## [Vehicle Type Method](#vehicle-type-method)

### name_fr

Méthode basée sur le type de véhicule

### description

The "vehicle type" method takes a different approach to estimate emissions. This method relies on categorizing vehicles, such as cars, trucks, and buses, and utilizing average emission factors assigned to each vehicle type. These emission factors are predefined estimates representing the typical emissions produced by each kind of vehicle. The "vehicle type" method is especially useful in situations where specific fuel consumption data is not readily accessible or when estimating emissions for a large and varied fleet of vehicles. Although less precise than the "fuel amount" method, the "vehicle type" method provides a more general overview of emissions by relying on average estimates based on vehicle categories.

### description_fr

La méthode basée sur le type de véhicule adopte une approche différente pour estimer les émissions. Cette méthode repose sur la catégorisation des véhicules, tels que les voitures, les camions et les bus, et utilise des facteurs d'émission moyens attribués à chaque type de véhicule. Ces facteurs d'émission sont des estimations prédéfinies représentant les émissions typiques produites par chaque type de véhicule. Cette méthode est particulièrement utile dans les situations où des données spécifiques de consommation de carburant ne sont pas facilement accessibles ou lors de l'estimation des émissions pour une flotte de véhicules importante et variée. Bien que moins précise que la méthode basée sur la quantité de carburant, la méthode basée sur le type de véhicule offre une vue d'ensemble plus générale des émissions en se basant sur des estimations moyennes basées sur les catégories de véhicules.

### implem_path

greenlang.calculations.ghg.scope_1.mobile_combustion.VehicleTypeMethod