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
### Codes
0	Vacant unit	·
Households:	
1	Households under 1970 definition	X
2	Additional households under 1990 definition	X
Group Quarters:	
3	Institutions	X
4	Other group quarters	X
5	Additional households under 2000 definition	·
6	Fragment	·

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
### Codes
1	White	X
2	Black/African American/Negro	X
3	American Indian or Alaska Native	X
4	Chinese	X
5	Japanese	X
6	Other Asian or Pacific Islander	X
7	Other race, nec	·
8	Two major races	·
9	Three or more major races	·

## RACED
Detailed RACE
## HISPAN
HISPAN identifies persons of Hispanic/Spanish/Latino origin and classifies them according to their country of origin when possible. Origin is defined by the Census Bureau as ancestry, lineage, heritage, nationality group, or country of birth. People of Hispanic origin may be of any race; see RACE for a discussion of coding issues involved. Users should note that race questions were not asked in the Puerto Rican censuses of 1970, 1980 and 1990. They were asked in the 1910 and 1920 Puerto Rican censuses, and in the 2000 and 2010 Puerto Rican census and the PRCS. However, questions assessing Spanish/Hispanic origin were not asked in the Puerto Rican censuses prior to 2000.

The HISPAN general code covers country-of-origin classifications common to all years; the detailed code distinguishes additional groups and subgroups. See HISPRULE for details on how country of origin information was assigned prior to 1980.

## Codes
0	Not Hispanic	X
1	Mexican	X
2	Puerto Rican	X
3	Cuban	X
4	Other	X
9	Not Reported	·

## HISPAND
Detailed HISPAN
## Codes

## BPL
BPL indicates the U.S. state, the outlying U.S. area or territory, or the foreign country where the person was born.
### Codes
	UNITED STATES	
001	Alabama	X
002	Alaska	X
004	Arizona	X
005	Arkansas	X
006	California	X
008	Colorado	X
009	Connecticut	X
010	Delaware	X
011	District of Columbia	X
012	Florida	X
013	Georgia	X
015	Hawaii	X
016	Idaho	X
017	Illinois	X
018	Indiana	X
019	Iowa	X
020	Kansas	X
021	Kentucky	X
022	Louisiana	X
023	Maine	X
024	Maryland	X
025	Massachusetts	X
026	Michigan	X
027	Minnesota	X
Code	Label	
1900
full
028	Mississippi	X
029	Missouri	X
030	Montana	X
031	Nebraska	X
032	Nevada	X
033	New Hampshire	X
034	New Jersey	X
035	New Mexico	X
036	New York	X
037	North Carolina	X
038	North Dakota	X
039	Ohio	X
040	Oklahoma	X
041	Oregon	X
042	Pennsylvania	X
044	Rhode Island	X
045	South Carolina	X
046	South Dakota	X
047	Tennessee	X
048	Texas	X
049	Utah	X
050	Vermont	X
051	Virginia	X
053	Washington	X
054	West Virginia	X
Code	Label	
1900
full
055	Wisconsin	X
056	Wyoming	X
090	Native American	X
099	United States, ns	X
US OUTLYING AREAS/TERRITORIES	
100	American Samoa	X
105	Guam	X
110	Puerto Rico	X
115	U.S. Virgin Islands	X
120	Other US Possessions	·
OTHER NORTH AMERICA	
150	Canada	X
155	St. Pierre and Miquelon	·
160	Atlantic Islands	X
199	North America, ns	X
CENTRAL AMERICA AND CARIBBEAN	
200	Mexico	X
210	Central America	X
Caribbean:	
250	Cuba	X
260	West Indies	X
299	Americas, n.s.	·
300	SOUTH AMERICA	X
EUROPE	
Northern Europe:	
Code	Label	
1900
full
400	Denmark	X
401	Finland	X
402	Iceland	X
403	Lapland, n.s.	X
404	Norway	X
405	Sweden	X
United Kingdom and Ireland:	
410	England	X
411	Scotland	X
412	Wales	X
413	United Kingdom, ns	X
414	Ireland	X
419	Northern Europe, ns	·
Western Europe:	
420	Belgium	X
421	France	X
422	Liechtenstein	X
423	Luxembourg	X
424	Monaco	X
425	Netherlands	X
426	Switzerland	X
429	Western Europe, ns	·
Southern Europe:	
430	Albania	X
431	Andorra	X
Code	Label	
1900
full
432	Gibraltar	X
433	Greece	X
434	Italy	X
435	Malta	X
436	Portugal	X
437	San Marino	·
438	Spain	X
439	Vatican City	·
440	Southern Europe, ns	·
Central/Eastern Europe:	
450	Austria	X
451	Bulgaria	X
452	Czechoslovakia	X
453	Germany	X
454	Hungary	X
455	Poland	X
456	Romania	X
457	Yugoslavia	X
458	Central Europe, ns	X
459	Eastern Europe, ns	X
Russian Empire:	
Baltic States:	
460	Estonia	·
461	Latvia	X
462	Lithuania	X
Code	Label	
1900
full
463	Baltic States, ns	·
465	Other USSR/Russia	X
499	Europe, ns	X
ASIA	
East Asia:	
500	China	X
501	Japan	X
502	Korea	X
509	East Asia, ns	·
Southeast Asia:	
510	Brunei	·
511	Cambodia (Kampuchea)	·
512	Indonesia	X
513	Laos	·
514	Malaysia	·
515	Philippines	X
516	Singapore	X
517	Thailand	X
518	Vietnam	·
519	Southeast Asia, ns	X
India/Southwest Asia:	
520	Afghanistan	X
521	India	X
522	Iran	X
523	Maldives	·
Code	Label	
1900
full
524	Nepal	·
Middle East/Asia Minor:	
530	Bahrain	·
531	Cyprus	X
532	Iraq	X
533	Iraq/Saudi Arabia	·
534	Israel/Palestine	X
535	Jordan	·
536	Kuwait	·
537	Lebanon	X
538	Oman	X
539	Qatar	·
540	Saudi Arabia	·
541	Syria	X
542	Turkey	X
543	United Arab Emirates	·
544	Yemen Arab Republic (North)	·
545	Yemen, PDR (South)	·
546	Persian Gulf States, n.s.	X
547	Middle East, ns	X
548	Southwest Asia, nec/ns	X
549	Asia Minor, ns	X
550	South Asia, nec	·
599	Asia, nec/ns	X
AFRICA	
Code	Label	
1900
full
600	AFRICA	X
Northern Africa:	
West Africa:	
East Africa:	
Central Africa:	
Southern Africa:	
OCEANIA	
700	Australia and New Zealand	X
710	Pacific Islands	X
800	Antarctica, ns/nec	·
900	Abroad (unknown) or at sea	X
950	Other n.e.c.	·
999	Missing/blank	·

## BPLD
Detailed BPL
## MBPL
MBPL reports the state, territory, or foreign country where the respondent's mother was born. The codes for MBPL are the same as for BPL (Birthplace). As with BPL, MBPL has a general code distinguishing places available in multiple years and a detailed code noting places unique to certain years or indicating areas that are strictly subsets of other countries.
### Codes: Basically the same as BPL
## MBPLD
Detailed MBPL
## FBPL
FBPL reports the U.S. state, the outlying U.S. area or territory, or the foreign country where the respondent's father was born. The codes for FBPL are the same as for BPL (Birthplace). As with BPL, FBPL has a general code distinguishing places available in multiple years and a detailed code noting places unique to certain years or indicating areas that are strictly subsets of other countries.
### Codes: Basically the same as BPL

## FBPLD
Detailed FBPL
## NATIVITY
NATIVITY indicates whether respondents were native-born or foreign-born; for native-born respondents, it indicates whether their mothers and/or fathers were native-born or foreign-born. NATIVITY is constructed from the IPUMS variables BPL, MBPL, and FBPL. Those U.S. possessions and territories classified as "U.S. outlying areas" in BPL are considered foreign. For a similar variable that identifies those who are foreign or native born in 1970 for Puerto Rico, see NATIVPR.
### Codes
0	N/A or unknown	·
Native-Born	
1	Both parents native-born	X
2	Father foreign, mother native	X
3	Mother foreign, father native	X
4	Both parents foreign	X
5	Foreign-Born	X

## CITIZEN
CITIZEN reports the citizenship status of respondents, distinguishing between naturalized citizens and non-citizens. For 1900-1940, respondents who were not yet citizens but who had begun the naturalization process ("received first papers") are identified.
### Codes
0	N/A	X
1	Born abroad of American parents	·
2	Naturalized citizen	X
3	Not a citizen	X
4	Not a citizen, but has received first papers	·
5	Foreign born, citizenship status not reported	·

## RACESING
RACESING codes race responses into a simple, historically compatible scheme. Multiple-race responses in the 2000 census, the ACS and the PRCS are recoded (or ''bridged'') into single-race responses. Although this simplification was done carefully, it should not be assumed that it is useful or required in every situation. It may not be needed if the user can tolerate a "break" in the racial coding system of their data series, or if an analysis includes only data from 2000 and beyond. The full detail available for responses to the race question is preserved in the RACE variable.

RACESING assigns a single race to multiple-race people. Each multiple-race person is assigned to the single race response category deemed most likely, depending on the individual's age, sex, Hispanic origin, region and urbanization level of residence, and the racial diversity of their local area. Local areas are defined as super-PUMAs for the Census 2000 1% sample, PUMAs for the Census 2000 5% sample, the 2005-onward ACS, the 2005-onward PRCS, and states for the 2001-2004 ACS samples. RACESING was created using the methods described in Ingram, et al. (2003). Users wishing to replicate RACESING in any other dataset with state-level geographic identifiers, can use the "race bridge" STATA program. Note, however that the IPUMS USA RACESING variable uses more detailed geographic information, so this program will not perfectly replicate the variable.

For each multiple-race person, probabilities were calculated for each of five single-race responses: American Indian/Alaska Native (PROBAI), Asian and/or Pacific Islander (PROBAPI), black (PROBBLK), white (PROBWHT), and other race (PROBOTH). IPUMS used the highest of these probabilities to assign each multiple-race person to a RACESING group. The sum of values for PROBAI, PROBAPI, PROBBLK, PROBOTH, and PROBWHT equals 100 for all people.

Almost all Hispanics are classified as white in RACESING. This includes respondents who checked the "other" box for the race question and wrote in a Hispanic race. It also includes respondents who checked the "other" box for the race question but did NOT write in a Hispanic race, as long as they identified themselves as Hispanic in the direct question about Hispanic status (only asked from 1980 on, see HISPAN). We chose to explicitly classify Hispanics as white in the years from 1980 onward because our historical Hispanic variable suggests that more than 95% of Hispanics were classified as white prior to 1970 (see HISPAN). The only Hispanic persons who are not coded as white in RACESING are those who explicitly reported their race as Black, American Indian/Alaska Native, any Asian or Pacific Islander group, and those who reported multiple races but ended up getting bridged to one of these three categories.

Details about how the RACE and RACESING codes are related is offered in the table, Relationship between RACE and RACESING codes. For single-race responses the relationship between RACE and RACESING codes is a straightforward data translation. For multiple-race responses, the page linked above shows the range of possible destination categories for each combination of racial responses. For example, a person who indicates that they are both Black and White (code 801 in the RACE variable) could either end up being classified as Black (code 20) or White (code 10) in the RACESING variable.
### Codes
1	White	X
2	Black	X
3	American Indian/Alaska Native	X
4	Asian and/or Pacific Islander	X
5	Other race, non-Hispanic	·

## RACESINGD
Detailed RACESING
## HISTID
HISTID is a consistent individual-level identifier.

The variables SERIAL and PERNUM uniquely identify individuals within a dataset. However, the specific respondents associated with those unique values can change as historical full count datasets are improved. HISTID allows researchers to track specific individuals regardless of any such changes as it is a unique identifier independent of household and position within household. Researchers can then merge their existing data with newer versions of the data file using HISTID and identify updates, corrections, or improvements that may have been applied to the data.