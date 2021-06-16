# prison_project
# changes made to general data (in 'state data' & 'foreign data')
* putting porto rico in foreign 
* Hawaii and Alaska back to states


## changes made to foreign data modernized
* alsace --> France
* Assyria -> Turkey
* Bohemia --> Czech Republic
* Crete -> Greece
* Holland -> Netherlands
* Isle of Man --> England
* Jugo-Slovakia (slavia) --> Yugoslavia
* New Brunswick/British Columbia/New Foundland/Nova Scotia/Ontario/Prince Edward Isle -> Canada
* Philippine Islands -> Philippines
* Prussia/Saxony -> Germany
* Romania spelling fixed
* Siam --> Thailand
* Siberia -> Russia
* Sicily -> Italy
* South Sea Islands -> Solomon Islands
* South Wales -> Wales
* Africa -> Egypt 
* Bermuda Islands -> UK
* Central America -> Costa Rica
* Czechoslovakia -> Czech Republic
* East Indies -> Phillipines 
* Java -> Indonesia
* Likely an error for Yugoslavia (26 one year all of a sudden?)
* Yugoslavia split between Serbia/Croatia based on their totals (2 went to Croatia in the year with 26, the rest went to Serbia)
* Korea -> South Korea 
* West Indies split between Cuba, Jamaica, and Porto Rico
* Wales, Scotland, England -> United Kingdom 

# Books previously used for Race & Foreign Data
## Historical statistics of the states of the United States : two centuries of the census, 1790-1990 / compiled by Donald B. Dodd.
* ISBN: 978-0-313-28309-3
* LCCN: 93025014 //r94
* Publication Date: 1993
## Historical Statistics of the United States: Millenial Edition (maybe the right one? not totally sure)
* Authors: Heffer, Jean
* Publication Year: 2008
* ISSN: 0982-1783 1957-7745
### Possible Alternative: Historical Statistics of the United States: Earliest Times to the Present-Millenial Edition.
* Authors: Bulson, Christine
* ISSN: 0006-7385
* Source: Booklist. 9/15/2006, Vol. 103 Issue 2, p92. 1p. 1 Color Photograph
## 100 Years of Census
* No idea what book I was referring to here, would probably need to dig through library sources 


# Census Data Notes
* consider adding 'HISPRULE'
* look at other economic metrics if you decide to use

## Unmatched Variables:
* not sure what 99 means in LANGUAGE, just leave it with nothing for now 
* same goes for LANGUAGED for 9900
    * might be 9999 (blank at end of LANGUAGED description)
    * consider assigning this blank to both? 
* 9 in SPEAKENG
    * codes end at 8 
* 996 & 975 in OCC1950
* 985 in IND1950
* DONT SEEM TO SEE ANY SIMPLE EXPLANATION IN VARIABLE DOCUMENTATION, PERHAPS A GOOGLE WILL HELP?

* there were no unmatched in the sample set 

## Variable Descriptions
### HHWT
HHWT indicates how many households in the U.S. population are represented by a given household in an IPUMS sample.

It is generally a good idea to use HHWT when conducting a household-level analysis of any IPUMS sample. The use of HHWT is optional when analyzing one of the "flat" or unweighted IPUMS samples. Flat IPUMS samples include the 1% samples from 1850-1930, all samples from 1960, 1970, and 1980, the 1% unweighted samples from 1990 and 2000, the 10% 2010 sample, and any of the full count 100% census datasets. HHWT must be used to obtain nationally representative statistics for household-level analyses of any sample other than those.

Users should also be sure to select one person (e.g., PERNUM = 1) to represent the entire household.

For further explanation of the sample weights, see "Sample Designs" and "Sample Weights". See also PERWT for a corresponding variable at the person level, and SLWT for a weight variable used with sample-line records in 1940 1% and 1950.
### SAMPLE
SAMPLE identifies the IPUMS sample from which the case is drawn. Each sample receives a unique 6-digit code. The codes are structured as follows:

The first four digits are the year of the census/survey.
The next two digits identify the sample within the year.
For most censuses, IPUMS has multiple datasets which were constructed using different sampling techniques (i.e. size/demographic of the sample population, geographic coverage level or location, or duration of the sampling period for the ACS/PRCS samples).

The availability table for each variable indicates whether that variable is available in only certain samples for a given year. For further discussion of sample differences, see "Sample Designs.".

Note: SAMPLE replaces DATANUM. Though the last two digits in SAMPLE do not correlate exactly with the now-deprecated DATANUM, the variable serves the same purpose of assigning a unique id to all cases that belong to the same dataset.

### CLUSTER: Why is this in the full sample but not STRATA?
CLUSTER is designed for use with STRATA in Taylor series linear approximation for correction of complex sample design characteristics. See the STRATA variable description for more details.


### GQ: could probably remove
GQ classifies all housing units as falling into one of three main categories: households, group quarters, or vacant units. It also identifies fragmentary sample units for 1850-1930 (see below). In all years, the data available about a person and their co-residents depend on whether the person lives in a household or in group quarters. Households are sampled as units, meaning that everyone in the household is included in the sample, and most household-level variables are available. People living in group quarters are generally sampled as individuals; other people in their unit may or may not be included in the sample, and there is no way of linking co-residents' records to one another. If, however, a sampled person in group quarters was living with relatives, the related group was sampled for 1850-1930. Most household-level variables are not available for group quarters or for vacant units.

Group quarters are largely institutions and other group living arrangements, such as rooming houses and military barracks. The definitions vary from year to year, but the pre-1940 samples have generally used a definition of group quarters that includes units with 10 or more individuals unrelated to the householder. See the comparability discussion below and "Sample Designs" for more details about changing definitions of group quarters. Group-quarters types are identified in further detail by GQTYPE and GQFUNDS.

### PERNUM: could probably remove, but feel as though this was mentioned as having applications for samplesets
PERNUM numbers all persons within each household consecutively in the order in which they appear on the original census or survey form. When combined with SAMPLE and SERIAL, PERNUM uniquely identifies each person within the IPUMS.

### PERWT 
indicates how many persons in the U.S. population are represented by a given person in an IPUMS sample.

It is generally a good idea to use PERWT when conducting a person-level analysis of any IPUMS sample. The use of PERWT is optional when analyzing one of the "flat" or unweighted IPUMS samples. Flat IPUMS samples include the 1% samples from 1850-1930, all samples from 1960, 1970, and 1980, the 1% unweighted samples from 1990 and 2000, the 10% 2010 sample, and any of the full count 100% census datasets. PERWT must be used to obtain nationally representative statistics for person-level analyses of any sample other than those.

For further explanation of the sample weights, see "Sample Designs" and "Sample Weights". See also HHWT for a corresponding variable at the household level, and SLWT for a weight variable used with sample-line records in 1940 and 1950.

### HISTID
HISTID is a consistent individual-level identifier.

The variables SERIAL and PERNUM uniquely identify individuals within a dataset. However, the specific respondents associated with those unique values can change as historical full count datasets are improved. HISTID allows researchers to track specific individuals regardless of any such changes as it is a unique identifier independent of household and position within household. Researchers can then merge their existing data with newer versions of the data file using HISTID and identify updates, corrections, or improvements that may have been applied to the data.

# Determine whether prison stats include women (and if so, for which years - go thru biennial reports)

# Determine whether prison stats include women (and if so, for which years - go thru biennial reports)

# CONFIRM THAT WEIGHTING IS BEING DONE CORRECTLY!
* Looks like it is: Multiply by PERWT to get roughly the entire population
    * [PERWT Documentation](https://usa.ipums.org/usa/chapter2/chapter2.shtml#6070)
    * look year by year to make sure this is done correctly
        * but it seems like documentation explains methadology they used for the process, rather than how the user ought to deal with it 
* Years:
    * seems like 