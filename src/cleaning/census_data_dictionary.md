# DATA EXPLANATION 
## YEAR
YEAR reports the four-digit year when the household was enumerated or included in the census, the ACS, and the PRCS.

For the multi-year ACS/PRCS samples, YEAR indicates the last year of data included (e.g., 2007 for the 2005-2007 3-year ACS/PRCS; 2008 for the 2006-2008 3-year ACS/PRCS; and so on). For the actual year of survey in these multi-year data, see MULTYEAR.
## SAMPLE (can probably drop this)
SAMPLE identifies the IPUMS sample from which the case is drawn. Each sample receives a unique 6-digit code. The codes are structured as follows:

The first four digits are the year of the census/survey.
The next two digits identify the sample within the year.
For most censuses, IPUMS has multiple datasets which were constructed using different sampling techniques (i.e. size/demographic of the sample population, geographic coverage level or location, or duration of the sampling period for the ACS/PRCS samples).

The availability table for each variable indicates whether that variable is available in only certain samples for a given year. For further discussion of sample differences, see "Sample Designs.".

Note: SAMPLE replaces DATANUM. Though the last two digits in SAMPLE do not correlate exactly with the now-deprecated DATANUM, the variable serves the same purpose of assigning a unique id to all cases that belong to the same dataset.
## SERIAL
SERIAL is an identifying number unique to each household record in a given sample. All person records are assigned the same serial number as the household record that they follow. (Person records also have their own unique identifiers - see PERNUM.) A combination of SAMPLE and SERIAL provides a unique identifier for every household in the IPUMS; the combination of SAMPLE, SERIAL, and PERNUM uniquely identifies every person in the database.

For 1850-1930, households that are part of a multi-household dwelling can be identified by using the DWELLING and DWSEQ variables. See "Sample Designs" for further discussion of sampling from within multi-household dwellings.
## STATEICP
STATEICP identifies the state in which the housing unit was located, using the coding scheme developed by the Inter-University Consortium for Political and Social Research (ICPSR). The ICPSR scheme orders states first by geographic division and then alphabetically within each division. Note that the ICPSR geographic divisions do not correspond exactly with the census regions used in the IPUMS variable REGION.

State or territory names represent that state or territory's contemporary political boundaries for a given year. Users should familiarize themselves with any historical changes in these boundaries that might affect their research. (Go here for year-by-year maps of states and territories in the U.S.) IPUMS assigns current state codes to territories that later became states; for example, Arizona Territory in 1880 and 1900 is given the Arizona state code (61). In 1880, Dakota Territory counties are split between areas that ultimately became North and South Dakota.
## STATEFIP
STATEFIP reports the state in which the household was located, using the Federal Information Processing Standards (FIPS) coding scheme, which orders the states alphabetically.

In the 1980 Urban/Rural sample, STATEFIP identifies state groups that are not available in STATEICP; these state groups (codes 61-68) are only available for that particular sample.

See "Geographic Coding and Comparability" for more information on the geographic detail available in particular samples.
## GQ
GQ classifies all housing units as falling into one of three main categories: households, group quarters, or vacant units. It also identifies fragmentary sample units for 1850-1930 (see below). In all years, the data available about a person and their co-residents depend on whether the person lives in a household or in group quarters. Households are sampled as units, meaning that everyone in the household is included in the sample, and most household-level variables are available. People living in group quarters are generally sampled as individuals; other people in their unit may or may not be included in the sample, and there is no way of linking co-residents' records to one another. If, however, a sampled person in group quarters was living with relatives, the related group was sampled for 1850-1930. Most household-level variables are not available for group quarters or for vacant units.

Group quarters are largely institutions and other group living arrangements, such as rooming houses and military barracks. The definitions vary from year to year, but the pre-1940 samples have generally used a definition of group quarters that includes units with 10 or more individuals unrelated to the householder. See the comparability discussion below and "Sample Designs" for more details about changing definitions of group quarters. Group-quarters types are identified in further detail by GQTYPE and GQFUNDS.
## PERNUM
PERNUM numbers all persons within each household consecutively in the order in which they appear on the original census or survey form. When combined with SAMPLE and SERIAL, PERNUM uniquely identifies each person within the IPUMS.
## PERWT
PERWT indicates how many persons in the U.S. population are represented by a given person in an IPUMS sample.

It is generally a good idea to use PERWT when conducting a person-level analysis of any IPUMS sample. The use of PERWT is optional when analyzing one of the "flat" or unweighted IPUMS samples. Flat IPUMS samples include the 1% samples from 1850-1930, all samples from 1960, 1970, and 1980, the 1% unweighted samples from 1990 and 2000, the 10% 2010 sample, and any of the full count 100% census datasets. PERWT must be used to obtain nationally representative statistics for person-level analyses of any sample other than those.

For further explanation of the sample weights, see "Sample Designs" and "Sample Weights". See also HHWT for a corresponding variable at the household level, and SLWT for a weight variable used with sample-line records in 1940 and 1950.
## RACE
With the exception of the 1970-1990 Puerto Rican censuses, RACE was asked of every person in all years. The concept of race has changed over the more than 150 years represented in the IPUMS. Currently, the Census Bureau and others consider race to be a sociopolitical construct, not a scientific or anthropological one. Many detailed RACE categories consist of national origin groups. Beginning in 2000, the race question changed substantially to allow respondents to report as many races as they felt necessary to describe themselves. In earlier years, only one race response was coded.

IPUMS offers several variables describing the answer(s) to the race question. RACE provides the full detail given by the respondent and/or released by the Census Bureau; it is not always historically compatible (see comparability discussion below). Users primarily interested in historical compatibility should consider using RACESING, and should consult the race code relationship page, Relationship between RACE and RACESING codes, for detail about how the RACE and RACESING codes are related.

In addition, specific combinations of major races can be discerned using the following bivariate indicators of whether a particular race group was reported: RACAMIND, RACASIAN, RACBLK, RACOTHER, RACPACIS, and RACWHT. RACNUM indicates the total number of major race groups reported for an individual. The information contained in the bivariate indicators and in RACNUM is integrated into the detailed version of RACE. Users primarily interested in historical comparability should consider using RACESING and/or the accompanying variables PROBAI, PROBAPI, PROBBLK, PROBOTH, and PROBWHT. Note that Hispanic origin is assessed through separate questioning (see HISPAN).

Prior to 1960, the census enumerator was responsible for categorizing persons and was not specifically instructed to ask the individual his or her race. In 1970 and later years, an individual's race was reported by someone in the household or group quarters. In the 1990 U.S. census, the 2000 U.S. and Puerto Rican censuses, the ACS, and the PRCS respondents were specifically asked what race the person "considers himself/herself" to be, although such self-description was more or less operative since 1960.

User Note: Race questions were not asked in the Puerto Rican censuses of 1970, 1980, and 1990. They were asked in the 1910 and 1920 Puerto Rican censuses, the 2000-2010 Puerto Rican censuses, and the PRCS.
## RACED
Detailed version of Race? look for more clarification 
## HISPAN
HISPAN identifies persons of Hispanic/Spanish/Latino origin and classifies them according to their country of origin when possible. Origin is defined by the Census Bureau as ancestry, lineage, heritage, nationality group, or country of birth. People of Hispanic origin may be of any race; see RACE for a discussion of coding issues involved. Users should note that race questions were not asked in the Puerto Rican censuses of 1970, 1980 and 1990. They were asked in the 1910 and 1920 Puerto Rican censuses, and in the 2000 and 2010 Puerto Rican census and the PRCS. However, questions assessing Spanish/Hispanic origin were not asked in the Puerto Rican censuses prior to 2000.

The HISPAN general code covers country-of-origin classifications common to all years; the detailed code distinguishes additional groups and subgroups. See HISPRULE for details on how country of origin information was assigned prior to 1980.
## HISPAND
## BPL
BPL indicates the U.S. state, the outlying U.S. area or territory, or the foreign country where the person was born.
## BPLD
## MBPL
MBPL reports the state, territory, or foreign country where the respondent's mother was born. The codes for MBPL are the same as for BPL (Birthplace). As with BPL, MBPL has a general code distinguishing places available in multiple years and a detailed code noting places unique to certain years or indicating areas that are strictly subsets of other countries.
## MBPLD
## FBPL
FBPL reports the U.S. state, the outlying U.S. area or territory, or the foreign country where the respondent's father was born. The codes for FBPL are the same as for BPL (Birthplace). As with BPL, FBPL has a general code distinguishing places available in multiple years and a detailed code noting places unique to certain years or indicating areas that are strictly subsets of other countries.
## FBPLD
## NATIVITY
NATIVITY indicates whether respondents were native-born or foreign-born; for native-born respondents, it indicates whether their mothers and/or fathers were native-born or foreign-born. NATIVITY is constructed from the IPUMS variables BPL, MBPL, and FBPL. Those U.S. possessions and territories classified as "U.S. outlying areas" in BPL are considered foreign. For a similar variable that identifies those who are foreign or native born in 1970 for Puerto Rico, see NATIVPR.
## CITIZEN
CITIZEN reports the citizenship status of respondents, distinguishing between naturalized citizens and non-citizens. For 1900-1940, respondents who were not yet citizens but who had begun the naturalization process ("received first papers") are identified.
## RACESING
RACESING codes race responses into a simple, historically compatible scheme. Multiple-race responses in the 2000 census, the ACS and the PRCS are recoded (or ''bridged'') into single-race responses. Although this simplification was done carefully, it should not be assumed that it is useful or required in every situation. It may not be needed if the user can tolerate a "break" in the racial coding system of their data series, or if an analysis includes only data from 2000 and beyond. The full detail available for responses to the race question is preserved in the RACE variable.

RACESING assigns a single race to multiple-race people. Each multiple-race person is assigned to the single race response category deemed most likely, depending on the individual's age, sex, Hispanic origin, region and urbanization level of residence, and the racial diversity of their local area. Local areas are defined as super-PUMAs for the Census 2000 1% sample, PUMAs for the Census 2000 5% sample, the 2005-onward ACS, the 2005-onward PRCS, and states for the 2001-2004 ACS samples. RACESING was created using the methods described in Ingram, et al. (2003). Users wishing to replicate RACESING in any other dataset with state-level geographic identifiers, can use the "race bridge" STATA program. Note, however that the IPUMS USA RACESING variable uses more detailed geographic information, so this program will not perfectly replicate the variable.

For each multiple-race person, probabilities were calculated for each of five single-race responses: American Indian/Alaska Native (PROBAI), Asian and/or Pacific Islander (PROBAPI), black (PROBBLK), white (PROBWHT), and other race (PROBOTH). IPUMS used the highest of these probabilities to assign each multiple-race person to a RACESING group. The sum of values for PROBAI, PROBAPI, PROBBLK, PROBOTH, and PROBWHT equals 100 for all people.

Almost all Hispanics are classified as white in RACESING. This includes respondents who checked the "other" box for the race question and wrote in a Hispanic race. It also includes respondents who checked the "other" box for the race question but did NOT write in a Hispanic race, as long as they identified themselves as Hispanic in the direct question about Hispanic status (only asked from 1980 on, see HISPAN). We chose to explicitly classify Hispanics as white in the years from 1980 onward because our historical Hispanic variable suggests that more than 95% of Hispanics were classified as white prior to 1970 (see HISPAN). The only Hispanic persons who are not coded as white in RACESING are those who explicitly reported their race as Black, American Indian/Alaska Native, any Asian or Pacific Islander group, and those who reported multiple races but ended up getting bridged to one of these three categories.

Details about how the RACE and RACESING codes are related is offered in the table, Relationship between RACE and RACESING codes. For single-race responses the relationship between RACE and RACESING codes is a straightforward data translation. For multiple-race responses, the page linked above shows the range of possible destination categories for each combination of racial responses. For example, a person who indicates that they are both Black and White (code 801 in the RACE variable) could either end up being classified as Black (code 20) or White (code 10) in the RACESING variable.
## RACESINGD
## HISTID
HISTID is a consistent individual-level identifier.

The variables SERIAL and PERNUM uniquely identify individuals within a dataset. However, the specific respondents associated with those unique values can change as historical full count datasets are improved. HISTID allows researchers to track specific individuals regardless of any such changes as it is a unique identifier independent of household and position within household. Researchers can then merge their existing data with newer versions of the data file using HISTID and identify updates, corrections, or improvements that may have been applied to the data.