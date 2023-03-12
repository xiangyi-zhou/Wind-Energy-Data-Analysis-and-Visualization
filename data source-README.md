
DATAPACKAGE: RENEWABLE POWER PLANTS
===========================================================================

https://doi.org/10.25832/renewable_power_plants/2020-08-25

by Open Power System Data: http://www.open-power-system-data.org/

Package Version: 2020-08-25

List of renewable energy power stations

This Data Package contains a list of renewable energy power plants in lists
of  renewable energy-based power plants of Czechia, Denmark, France,
Germany, Poland, Sweden, Switzerland and United Kingdom.  Czechia:
Renewable-energy power plants in Czech Republic. Denmark: Wind and
phovoltaic power plants with a high level of detail. France:
Renewable-energy power plants of various types (solar, hydro, wind,
bioenergy marine, geothermal) in France. Germany: Individual power plants,
all renewable energy plants supported by the German Renewable Energy Law
(EEG). Poland: Summed capacity and number of installations per energy
source per municipality (Powiat). Sweden: Wind power plants in Sweden.
Switzerland: All renewable-energy power plants supported by the
feed-in-tariff KEV (Kostendeckende Einspeisevergütung). United Kingdom:
Renewable-energy power plants in the United Kingdom.
Due to different data availability, the power plant lists are of different 
accurancy and partly provide different power plant parameter. Due to that,
the  lists are provided as seperate csv-files per country and as separate
sheets in the excel file. Suspect data or entries with high probability of
duplication are marked in the column 'comment'. Theses validation markers
are explained in the file validation_marker.csv. Additionally, the Data
Package includes daily time series of cumulated installed capacity per
energy source type for Germany, Denmark, Switzerland, the United Kingdom
and Sweden. All data processing is  conducted in Python and pandas and has
been documented in the Jupyter Notebooks linked below. 

The data package covers the geographical region of Czechia, Denmark, France, Germany, Poland, Sweden, Switzerland, United Kingdom.

We follow the Data Package standard by the Frictionless Data project, a
part of the Open Knowledge Foundation: http://frictionlessdata.io/


Documentation and script
===========================================================================

This README only contains the most basic information about the data package.
For the full documentation, please see the notebook script that was used to
generate the data package. You can find it at:

https://nbviewer.jupyter.org/github/Open-Power-System-Data/renewable_power_plants/blob/2020-08-25/main.ipynb

Or on GitHub at:

https://github.com/Open-Power-System-Data/renewable_power_plants/blob/2020-08-25/main.ipynb

License and attribution
===========================================================================

Attribution:
    Open Power System Data. 2020. Data Package Renewable power plants.
    Version 2020-05-20.
    https://doi.org/10.25832/renewable_power_plants/2020-05-20. (Primary
    data from various sources, for a complete list see URL)


Version history
===========================================================================

* 2020-08-25 Updated all countries with new data available (DE, FR, PL, CH, DK, UK), added data for CZ and SE.
* 2019-04-05 Updated all countries with new data available (DE, FR, CH, DK), added data for UK and expanded renewable capacity timeseries to more countries (DK, UK, CH in addition to DE).
* 2018-03-08 Fixing incorrect coordinates in previous version.
* 2018-02-27 Update of German data to latest available versions.
* 2017-07-03 Included Swiss data, Updated all sources to newest available data and bug fixes
* 2017-02-16 Included Danish, French and Polish data, Updated German input data
* 2016-10-21 Included Danish, French and Polish data, Updated German input data


Resources
===========================================================================

* [Package description page](http://data.open-power-system-data.org/renewable_power_plants/2020-08-25/)
* [ZIP Package](http://data.open-power-system-data.org/renewable_power_plants/opsd-renewable_power_plants-2020-08-25.zip)
* [Script and documentation](https://github.com/Open-Power-System-Data/renewable_power_plants/blob/2020-08-25/main.ipynb)
* [Original input data](http://data.open-power-system-data.org/renewable_power_plants/2020-08-25/original_data/)


Sources
===========================================================================

* [Postleitzahlen Deutschland](http://www.suche-postleitzahl.org/downloads)
* [GeoNames](http://download.geonames.org/export/zip/)
* [Eurostat (NUTS tables)](https://ec.europa.eu/eurostat/home?)
* [Bundesnetzagentur](https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/ErneuerbareEnergien/ZahlenDatenInformationen/VOeFF_Registerdaten/2019_01_Veroeff_RegDaten.xlsx?__blob=publicationFile&v=2)
* [bnetza_pv_historic](https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/ErneuerbareEnergien/ZahlenDatenInformationen/PV_Datenmeldungen/Archiv_PV/Meldungen_Aug-Juni2017.xlsx?__blob=publicationFile&v=2)
* [bnetza_pv](https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/ErneuerbareEnergien/ZahlenDatenInformationen/PV_Datenmeldungen/Meldungen_Juli17-Jan19.xlsx?__blob=publicationFile&v=2)
* [Amprion](https://www.netztransparenz.de/portals/1/Netztransparenz%20Anlagenstammdaten%202019%20Amprion%20GmbH.zip)
* [TransnetBW](https://www.netztransparenz.de/portals/1/Netztransparenz%20Anlagenstammdaten%202019%20TransnetBW%20GmbH.zip)
* [50Hertz](https://www.netztransparenz.de/portals/1/Netztransparenz%20Anlagenstammdaten%202019%2050Hertz%20Transmission%20GmbH.zip)
* [Tennet](https://www.netztransparenz.de/portals/1/Netztransparenz%20Anlagenstammdaten%202019%20TenneT%20TSO%20GmbH.zip)
* [Energystyrelsen](https://ens.dk/sites/ens.dk/files/Statistik/anlaegprodtilnettet.xls)
* [Energinet](https://data.open-power-system-data.org/renewable_power_plants/2018-03-08/original_data/SolcellerGraf-2016-11.xlsx)
* [Ministère de la Transition écologique et solidaire](http://www.statistiques.developpement-durable.gouv.fr/sites/default/files/2019-01/donnees-locales-2017-loi2000-secretise.xls)
* [Open Data Réseaux Energies](https://opendata.reseaux-energies.fr/explore/dataset/registre-national-installation-production-stockage-electricite-agrege-311218/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B)
* [Urzad Regulacji Energetyki](https://www.ure.gov.pl/download/9/10922/Instalacjeodnawialnychzrodelenergiiwgstanunadzien31grudnia2019r.xlsx)
* [Bundesamt für Energie](https://pubdb.bfe.admin.ch/de/publication/download/9669)
* [UK Government Department for Business, Energy & Industrial Strategy](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/901383/renewable-energy-planning-database-June-2020-update.csv)
* [Vindbrukskollen](http://ext-dokument.lansstyrelsen.se/Gemensamt/Geodata/Externa%20dokument/VBK/VBK_export_allman_prod.xlsx)
* [Energetický regulační úřad](http://licence.eru.cz/index.php)
* [Opendatasoft](http://public.opendatasoft.com/explore/dataset/code-postal-code-insee-2015/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true)
* [Eurostat](https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/nuts/download/ref-nuts-2016-01m.shp.zip)


Field documentation
===========================================================================

renewable_power_plants_DE.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Subtype of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. DE1).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. DE11).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. DE111).
* lon
    - Type: number
    - Description: Longitude coordinates
* lat
    - Type: number
    - Description: Latitude coordinates
* municipality
    - Type: string
    - Description: Name of German Gemeinde (municipality)
* municipality_code
    - Type: string
    - Description: German Gemeindenummer (municipalitiy number)
* postcode
    - Type: string
    - Description: German zip-code
* address
    - Type: string
    - Description: Street name or name of land parcel
* federal_state
    - Type: string
    - Description: Name of German administrative level 'Bundesland'
* commissioning_date
    - Type: date
    - Description: Date of commissioning of specific unit
* decommissioning_date
    - Type: date
    - Description: Date of decommissioning of specific unit
* voltage_level
    - Type: string
    - Description: Voltage level of grid connection
* eeg_id
    - Type: string
    - Description: Power plant EEG (German feed-in tariff law) remuneration number
* dso
    - Type: string
    - Description: Name of distribution system operator of the region the plant is located in
* dso_id
    - Type: string
    - Description: Company number of German distribution grid operator
* tso
    - Type: string
    - Description: Name of transmission system operator of the area the plant is located


renewable_power_plants_DK.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Subtype of energy source.
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. DK0).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. DK01).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. DK013).
* lon
    - Type: number
    - Description: Longitude coordinates
* lat
    - Type: number
    - Description: Latitude coordinates
* municipality
    - Type: string
    - Description: Name of Danish Kommune
* municipality_code
    - Type: string
    - Description: Danish 3-digit Kommune-Nr
* postcode
    - Type: string
    - Description: Danish zip-code
* address
    - Type: string
    - Description: Street name or name of land parcel
* commissioning_date
    - Type: date
    - Description: date of the plant's commissioning
* hub_height
    - Type: number
    - Description: Wind turbine hub heigth in m
* rotor_diameter
    - Type: number
    - Description: Wind turbine rotor diameter in m
* model
    - Type: string
    - Description: Wind turbine model type
* gsrn_id
    - Type: integer
    - Description: Danish wind turbine identifier number (GSRN)
* dso
    - Type: string
    - Description: Name of distribution system operator of the region the plant is located in
* manufacturer
    - Type: string
    - Description: Company that has built the wind turbine


renewable_power_plants_FR.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Subtype of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. FR1).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. FR10).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. FR101).
* lon
    - Type: number
    - Description: Longitude coordinates
* lat
    - Type: number
    - Description: Latitude coordinates
* municipality
    - Type: string
    - Description: Name of French Commune
* municipality_code
    - Type: integer
    - Description: French 5-digit INSEE code for Communes
* region
    - Type: string
    - Description: Name of the French region
* region_code
    - Type: integer
    - Description: Code of the French region
* municipality_group
    - Type: string
    - Description: Name of the group of municipalities the plant is located in.
* municipality_group_code
    - Type: integer
    - Description: Code of the group of municipalities the plant is located in.
* departement
    - Type: string
    - Description: The name of the French departement
* departement_code
    - Type: integer
    - Description: The number of the French departement
* commissioning_date
    - Type: date
    - Description: The date of the plant's commissioning
* connection_date
    - Type: date
    - Description: The data when the plant was connected to the French grid
* disconnection_date
    - Type: date
    - Description: The date that the plant was disconnected from the French grid
* number_of_installations
    - Type: integer
    - Description: Number of installations of the energy source subtype in the municipality. Due to confidentiality reasons, the values smaller than 3 are published as ''<3'' (as in the source).
* site_name
    - Type: string
    - Description: The power plant's name.
* IRIS_code
    - Type: string
    - Description: IRIS code
* EIC_code
    - Type: string
    - Description: Energy Identification Code - the plant's unique identifier in the French grid
* as_of_year
    - Type: integer
    - Description: Year for which the data source compiled the original dataset.


renewable_power_plants_PL.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Subtype of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. PL1).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. PL11).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. PL113).
* region
    - Type: string
    - Description: The name of the Polish voivodeship.
* district
    - Type: string
    - Description: The name of the Polish powiat.
* URE_id
    - Type: integer
    - Description: The URE id of the plant.
* as_of_year
    - Type: integer
    - Description: Year for which the data source compiled the original dataset.


renewable_power_plants_UK.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Type of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: The source of database entries
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. UKD).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. UKD1).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. UKC12).
* lon
    - Type: string
    - Description: Longitude coordinates
* lat
    - Type: string
    - Description: Latitude coordinates
* municipality
    - Type: string
    - Description: Municipality
* postcode
    - Type: string
    - Description: Postcode
* address
    - Type: string
    - Description: Address
* region
    - Type: string
    - Description: Region
* country
    - Type: string
    - Description: The UK's constituent country in which the facility is located.
* commissioning_date
    - Type: date
    - Description: Date of commissioning of specific unit
* solar_mounting_type
    - Type: string
    - Description: For solar PV developments, whether the PV panels are ground or roof mounted
* chp
    - Type: string
    - Description: Is the project capable of combined heat and power output
* capacity_individual_turbine
    - Type: number
    - Description: For windfarms, the individual capacity of each wind turbine in megawatts (MW)
* number_of_turbines
    - Type: integer
    - Description: For windfarms, the number of wind turbines located on the site
* site_name
    - Type: string
    - Description: Name of site
* uk_beis_id
    - Type: integer
    - Description: ID for the plant as assigned by UK BEIS.
* operator
    - Type: string
    - Description: Name of operator
* comment
    - Type: string
    - Description: Shortcodes for comments related to this entry, explanation can be looked up in validation_marker.csv


renewable_power_plants_CH.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Type of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. CH0).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. CH03).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. CH031).
* lon
    - Type: number
    - Description: Longitude coordinate
* lat
    - Type: number
    - Description: Latitude coordinate
* municipality
    - Type: string
    - Description: Municipality
* municipality_code
    - Type: integer
    - Description: Municipality code
* postcode
    - Type: string
    - Description: Swiss zip code
* address
    - Type: string
    - Description: Street name
* canton
    - Type: string
    - Description: Name of the cantones/ member states of the Swiss confederation
* commissioning_date
    - Type: date
    - Description: Commissioning date
* contract_period_end
    - Type: date
    - Description: End of subsidy contract
* company
    - Type: string
    - Description: Name of the company
* tariff
    - Type: number
    - Description: Tariff in CHF for 2016
* project_name
    - Type: string
    - Description: Name of the project
* production
    - Type: number
    - Description: Yearly production in MWh


renewable_power_plants_SE.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW.
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Type of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. SE0).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. SE02).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. SE021).
* lon
    - Type: number
    - Description: Longitude coordinates
* lat
    - Type: number
    - Description: Latitude coordinates
* municipality
    - Type: string
    - Description: Municipality
* county
    - Type: string
    - Description: County
* commissioning_date
    - Type: date
    - Description: Commissioning date
* site_name
    - Type: string
    - Description: Name of site
* se_vindbrukskollen_id
    - Type: string
    - Description: The id in the vindbrukskollen data
* manufacturer
    - Type: string
    - Description: Manufacturer


renewable_power_plants_CZ.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW.
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Type of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. CZ0).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. CZ08).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. CZ08-).
* lon
    - Type: number
    - Description: Longitude coordinates
* lat
    - Type: number
    - Description: Latitude coordinates
* municipality
    - Type: string
    - Description: Municipality
* postcode
    - Type: string
    - Description: Postcode
* region
    - Type: string
    - Description: Region
* locality
    - Type: string
    - Description: Town or village
* owner
    - Type: string
    - Description: Owner
* site_name
    - Type: string
    - Description: Name of site


res_plants_separated_DE_outvalidated_plants.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Subtype of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. DE1).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. DE11).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. DE111).
* lon
    - Type: number
    - Description: Longitude coordinates
* lat
    - Type: number
    - Description: Latitude coordinates
* municipality
    - Type: string
    - Description: Name of German Gemeinde (municipality)
* municipality_code
    - Type: string
    - Description: German Gemeindenummer (municipalitiy number)
* postcode
    - Type: string
    - Description: German zip-code
* address
    - Type: string
    - Description: Street name or name of land parcel
* federal_state
    - Type: string
    - Description: Name of German administrative level 'Bundesland'
* commissioning_date
    - Type: date
    - Description: Date of commissioning of specific unit
* decommissioning_date
    - Type: date
    - Description: Date of decommissioning of specific unit
* voltage_level
    - Type: string
    - Description: Voltage level of grid connection
* eeg_id
    - Type: string
    - Description: Power plant EEG (German feed-in tariff law) remuneration number
* dso
    - Type: string
    - Description: Name of distribution system operator of the region the plant is located in
* dso_id
    - Type: string
    - Description: Company number of German distribution grid operator
* tso
    - Type: string
    - Description: Name of transmission system operator of the area the plant is located
* comment
    - Type: string
    - Description: Shortcodes for comments related to this entry, explanation can be looked up in validation_marker.csv


res_plants_separated_FR_outvalidated_plants.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Subtype of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energy source (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. FR1).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. FR10).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. FR101).
* lon
    - Type: number
    - Description: Longitude coordinates
* lat
    - Type: number
    - Description: Latitude coordinates
* municipality
    - Type: string
    - Description: Name of French Commune
* municipality_code
    - Type: integer
    - Description: French 5-digit INSEE code for Communes
* region
    - Type: string
    - Description: Name of the French region
* region_code
    - Type: integer
    - Description: Code of the French region
* municipality_group
    - Type: string
    - Description: Name of the group of municipalities the plant is located in.
* municipality_group_code
    - Type: integer
    - Description: Code of the group of municipalities the plant is located in.
* departement
    - Type: string
    - Description: The name of the French departement
* departement_code
    - Type: integer
    - Description: The number of the French departement
* commissioning_date
    - Type: date
    - Description: The date of the plant's commissioning
* connection_date
    - Type: date
    - Description: The data when the plant was connected to the French grid
* disconnection_date
    - Type: date
    - Description: The date that the plant was disconnected from the French grid
* number_of_installations
    - Type: integer
    - Description: Number of installations of the energy source subtype in the municipality. Due to confidentiality reasons, the values smaller than 3 are published as ''<3'' (as in the source).
* site_name
    - Type: string
    - Description: The power plant's name.
* IRIS_code
    - Type: string
    - Description: IRIS code
* EIC_code
    - Type: string
    - Description: Energy Identification Code - the plant's unique identifier in the French grid
* as_of_year
    - Type: integer
    - Description: Year for which the data source compiled the original dataset.
* comment
    - Type: string
    - Description: Shortcodes for comments related to this entry, explanation can be looked up in validation_marker.csv


validation_marker.csv
---------------------------------------------------------------------------

* Validation marker
    - Type: string
    - Description: Name of validation marker utilized in column comment in the renewable_power_plant_germany.csv
* Long explanation
    - Type: string
    - Description: Explanation of the validation marker
* Short explanation
    - Type: string
    - Description: Short comment on the meaning of the marker
* Country
    - Type: string
    - Description: The country for which the marker is defined.


renewable_power_plants_EU.csv
---------------------------------------------------------------------------

* electrical_capacity
    - Type: number
    - Description: Installed electrical capacity in MW
* energy_source_level_1
    - Type: string
    - Description: Type of energy source (e.g. Renewable energy)
* energy_source_level_2
    - Type: string
    - Description: Type of energy source (e.g. Wind, Solar)
* energy_source_level_3
    - Type: string
    - Description: Type of energy source (e.g. Biomass and biogas)
* technology
    - Type: string
    - Description: Technology to harvest energt (e.g. Onshore, Photovoltaics)
* data_source
    - Type: string
    - Description: Source of database entry
* nuts_1_region
    - Type: string
    - Description: The code of the NUTS 1 region the facility is in (e.g. NL1).
* nuts_2_region
    - Type: string
    - Description: The code of the NUTS 2 region the facility is in (e.g. NL11).
* nuts_3_region
    - Type: string
    - Description: The code of the NUTS 3 region the facility is in (e.g. NL112).
* lon
    - Type: number
    - Description: Geographical longitude
* lat
    - Type: number
    - Description: Geographical latitude
* municipality
    - Type: string
    - Description: The name of the municipality in which the facility is located.
* country
    - Type: string
    - Description: The country in which the facility is located
* commissioning_date
    - Type: date
    - Description: Date of commissioning of specific unit
* as_of_year
    - Type: integer
    - Description: Year for which the data source compiled the corresponding dataset
* geographical_resolution
    - Type: string
    - Description: Precision of geographical information (exact power plant location, municipality, district)



renewable_capacity_timeseries.csv
---------------------------------------------------------------------------

* day
    - Type: date
    - Description: The day of the timeseries entry
* CH_bioenergy_capacity
    - Type: number
    - Description: Cumulative bioenergy electrical capacity for Switzerland in MW
    - Source: [Own calculation based on plant-level data from Swiss Federal Office of Energy](input/original_data/CH/BFE/9669-Liste aller KEV-Bezüger im Jahr 2018.xlsx)
* CH_solar_capacity
    - Type: number
    - Description: Cumulative solar electrical capacity for Switzerland in MW
    - Source: [Own calculation based on plant-level data from Swiss Federal Office of Energy](input/original_data/CH/BFE/9669-Liste aller KEV-Bezüger im Jahr 2018.xlsx)
* CH_wind_onshore_capacity
    - Type: number
    - Description: Cumulative onshore wind electrical capacity for Switzerland in MW
    - Source: [Own calculation based on plant-level data from Swiss Federal Office of Energy](input/original_data/CH/BFE/9669-Liste aller KEV-Bezüger im Jahr 2018.xlsx)
* DE_bioenergy_capacity
    - Type: number
    - Description: Cumulative bioenergy electrical capacity for Germany in MW
    - Source: Own calculation based on plant-level data from BNetzA and Netztransparenz.de
* DE_geothermal_capacity
    - Type: number
    - Description: Cumulative geothermal electrical capacity for Germany in MW
    - Source: Own calculation based on plant-level data from BNetzA and Netztransparenz.de
* DE_solar_capacity
    - Type: number
    - Description: Cumulative solar electrical capacity for Germany in MW
    - Source: Own calculation based on plant-level data from BNetzA and Netztransparenz.de
* DE_wind_capacity
    - Type: number
    - Description: 
    - Source: Own calculation based on plant-level data from BNetzA and Netztransparenz.de
* DE_wind_offshore_capacity
    - Type: number
    - Description: Cumulative offshore wind electrical capacity for Germany in MW
    - Source: Own calculation based on plant-level data from BNetzA and Netztransparenz.de
* DE_wind_onshore_capacity
    - Type: number
    - Description: Cumulative onshore wind electrical capacity for Germany in MW
    - Source: Own calculation based on plant-level data from BNetzA and Netztransparenz.de
* DK_solar_capacity
    - Type: number
    - Description: Cumulative solar electrical capacity for Denmark in MW
    - Source: [Own calculation based on plant-level data from Energinet.dk](input/original_data/DK/Energinet/SolcellerGraf-2016-11.xlsx)
* DK_wind_capacity
    - Type: number
    - Description: Cumulative total wind electrical capacity for Denmark in MW
    - Source: [Own calculation based on plant-level data from Danish Energy Agency](input/original_data/DK/Energistyrelsen/anlaegprodtilnettet.xls)
* DK_wind_offshore_capacity
    - Type: number
    - Description: Cumulative offshore wind electrical capacity for Denmark in MW
    - Source: [Own calculation based on plant-level data from Danish Energy Agency](input/original_data/DK/Energistyrelsen/anlaegprodtilnettet.xls)
* DK_wind_onshore_capacity
    - Type: number
    - Description: Cumulative onshore wind electrical capacity for Denmark in MW
    - Source: [Own calculation based on plant-level data from Danish Energy Agency](input/original_data/DK/Energistyrelsen/anlaegprodtilnettet.xls)
* FR_bioenergy_capacity
    - Type: number
    - Description: Cumulative bioenergy electrical capacity for France in MW
    - Source: Own calculation based on plant-level data from ODRE and Ministère de la Transition écologique et solidaire
* FR_geothermal_capacity
    - Type: number
    - Description: Cumulative geothermal electrical capacity for France in MW
    - Source: Own calculation based on plant-level data from ODRE and Ministère de la Transition écologique et solidaire
* FR_hydro_capacity
    - Type: number
    - Description: Cumulative hydroenergy electrical capacity for France in MW
    - Source: Own calculation based on plant-level data from ODRE and Ministère de la Transition écologique et solidaire
* FR_marine_capacity
    - Type: number
    - Description: Cumulative marine electrical capacity for France in MW
    - Source: Own calculation based on plant-level data from ODRE and Ministère de la Transition écologique et solidaire.
* FR_solar_capacity
    - Type: number
    - Description: Cumulative solar electrical capacity for France in MW
    - Source: Own calculation based on plant-level data from ODRE and Ministère de la Transition écologique et solidaire.
* FR_wind_onshore_capacity
    - Type: number
    - Description: Cumulative wind onshore electrical capacity for France in MW
    - Source: Own calculation based on plant-level data from ODRE and Ministère de la Transition écologique et solidaire.
* GB-GBN_bioenergy_capacity
    - Type: number
    - Description: Cumulative bioenergy electrical capacity for Great Britain (England, Scotland, Wales) in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-GBN_hydro_capacity
    - Type: number
    - Description: Cumulative hydro electrical capacity for Great Britain (England, Scotland, Wales) in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-GBN_marine_capacity
    - Type: number
    - Description: Cumulative marine electrical capacity for Great Britain (England, Scotland, Wales) in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-GBN_solar_capacity
    - Type: number
    - Description: Cumulative solar electrical capacity for Great Britain (England, Scotland, Wales) in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-GBN_wind_capacity
    - Type: number
    - Description: Cumulative total wind electrical capacity for Great Britain (England, Scotland, Wales) in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-GBN_wind_offshore_capacity
    - Type: number
    - Description: Cumulative offshore wind electrical capacity for Great Britain (England, Scotland, Wales) in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-GBN_wind_onshore_capacity
    - Type: number
    - Description: Cumulative onshore wind electrical capacity for Great Britain (England, Scotland, Wales) in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-NIR_bioenergy_capacity
    - Type: number
    - Description: Cumulative bioenergy electrical capacity for Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-NIR_solar_capacity
    - Type: number
    - Description: Cumulative solar electrical capacity for Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-NIR_wind_onshore_capacity
    - Type: number
    - Description: Cumulative onshore wind electrical capacity for Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-UKM_bioenergy_capacity
    - Type: number
    - Description: Cumulative bioenergy electrical capacity for the United Kingdom of Great Britain and Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-UKM_hydro_capacity
    - Type: number
    - Description: Cumulative hydro electrical capacity for the United Kingdom of Great Britain and Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-UKM_marine_capacity
    - Type: number
    - Description: Cumulative marine electrical capacity for the United Kingdom of Great Britain and Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-UKM_solar_capacity
    - Type: number
    - Description: Cumulative solar electrical capacity for the United Kingdom of Great Britain and Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-UKM_wind_capacity
    - Type: number
    - Description: Cumulative total wind electrical capacity for the United Kingdom of Great Britain and Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-UKM_wind_offshore_capacity
    - Type: number
    - Description: Cumulative offshore wind electrical capacity for the United Kingdom of Great Britain and Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* GB-UKM_wind_onshore_capacity
    - Type: number
    - Description: Cumulative onshore wind electrical capacity for the United Kingdom of Great Britain and Northern Ireland in MW
    - Source: [Own calculation based on plant-level data from BEIS](input/original_data/UK/BEIS/renewable-energy-planning-database-march-2020-update.csv)
* SE_wind_capacity
    - Type: number
    - Description: Cumulative total wind electrical capacity for Sweden in MW
    - Source: [Own calculation based on plant-level data from Vindbrukskollen](input/original_data/SE/Vindbrukskollen/VBK_export_allman_prod.xlsx)
* SE_wind_offshore_capacity
    - Type: number
    - Description: Cumulative offshore wind electrical capacity for Sweden in MW
    - Source: [Own calculation based on plant-level data from Vindbrukskollen](input/original_data/SE/Vindbrukskollen/VBK_export_allman_prod.xlsx)
* SE_wind_onshore_capacity
    - Type: number
    - Description: Cumulative onshore wind electrical capacity for Sweden in MW
    - Source: [Own calculation based on plant-level data from Vindbrukskollen](input/original_data/SE/Vindbrukskollen/VBK_export_allman_prod.xlsx)


Feedback
===========================================================================

Thank you for using data provided by Open Power System Data. If you have
any question or feedback, please do not hesitate to contact us.

For this data package, contact:
Ingmar Schlecht <schlecht@neon-energie.de>

Milos Simic <milos.simic.ms@gmail.com>

For general issues, find our team contact details on our website:
http://www.open-power-system-data.org














