# Overview
In the summer of 2017 I received a grant from the Colorado College History Department to study the resources available at the Canon City Prison Museum archive. These documents dated from Colorado Territorial Correctional Facility’s inception in 1878 until 1940. After completing a data science bootcamp during the spring of 2021, I decided to revisit that data and create some visualizations. Although still a work in progress, the visualizations are available to be viewed at this link: http://54.177.157.57/

My hope is that I will be able to continue revisiting these visualizations and improve upon them, as well as the EC2 instance which currently hosts the site. I used Pandas and Python to deal with the data I collected, and Tableau to create the visualizations. The specifics of each section are explained below. 

# Prisoner Birthplace
There are four categories listed under Prisoner Birthplace: US States, US Regions, Foreign Countries, and Foreign Regions. They all depict the distribution of birthplaces of Colorado's prisoners. All the visualizations follow the same general schema. The first seven slides show the birthplace distribution from a group of four biennial reports. The prison usually, but not always, released a report every two years. Most of the charts encompass an eight-year timespan. As a consequence of a few missing biennial reports, there are some charts that include a timespan longer than eight years:

* 1896-1906: Missing 1898/1904
* 1908-1916: Missing 1910

The scales are always the same across years, but are different in the final visualization ('All Years') which is an aggregate of the seven prior slides.

# Comparison to Census Data
This chart compares the demographics of the prison to the demographics of Colorado, as inferred from census data. For years when no census was conducted, I used a simple linear regression to extrapolate likely demographic distributions. 
The first slide compares the percent of prisoners listed as "Black" with the percent of the population counted as "Black" in the census. The rest of the slides use the birthplaces of prisoners/censused individuals. The slide on Mexicans uses birthplace data rather than race data, as the census counted those with Latino heritage as being "White" for all the included years,with the exception of 1930. 

I hope to improve upon these visualizations by filtering the census data to more closely conform to the ages and genders of the prisoners. Some biennial reports include women in race and birthplace statistics, while some do not. It is likely that the prison population was composed of fewer children and elderly individuals than the general population. Another consideration is that census data does not always perfectly represent the individuals living in any one region. For example, many miners living in Colorado in the 19th century were of foreign heritage, and did not lay down permanent roots in the state. It may be beneficial to look for other data which accounts for possible underrepresentation. 

# Crime By Category
These slides attempt to categorize the crimes for which prisoners were incarcerated.. The first slide shows each crime category, the number of prisoners incarcerated for those crimes, and the demographics of those prisoners. The following slides give a more detailed look at each crime category, showing the demographics of the prisoners incarcerated for those crimes, the average sentence length for each demographic, and the crimes included in the category. 

# Sentence Length
This chart analyzes the sentence lengths of prisoners incarcerated in Colorado. The first slide shows the average prison term by demographic group. The second slide shows the average prison term from 1878 until 1940. The third slide looks at the average prison length of foreign prisoners. The fourth slide shows the percent of prisoners with life/death sentences compared to those with standard prison sentences. The final two slides look at life and death sentences by prisoner background. Prisoners with longer sentences are overrepresented, most likely because they are included in multiple biennial reports. Because going forward some efforts should be made to distinguish between prisoners counted by a previous Biennial Report and those who are appearing for the first time in the prisoner logs. 

# Going Forward
It is important to keep in mind that prisoners with terms longer than a few years are likely represented in multiple biennial reports. This means that these visualizations, as well as the ones under other tabs, are weighted by how many biennial reports in which a prisoner appeared. This might be remedied with additional data collection that distinguishes between repeated prisoners. 

As I become more skilled with Tableau I hope to improve upon the visualizations already created. I also plan to add more expository information to the Tableau visualizations, as well as the website which hosts them. I would like for this website to have some sort of narrative flow to it, rather than forcing the viewer to make inferences on their own. 
