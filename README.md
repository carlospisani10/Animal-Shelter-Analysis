# Project: Be a hero & save a pet today
## Team Name: In the Dawg Houz
### Team:  Emily Cogsgill, Marya Crigler,  Carlos Pisani, Stephen Schadt

We analyzed animal shelter intake and outcome data from two publicly available datasets. One dataset came from the city of Austin TX, and the other came from Louisville, KY. The Louisville data contained both intake and outcome data for each animal, while the Austin data contained intakes and outcomes in separate datasets that we merged as part of the data cleaning process.

## Data Sources
### Austin, TX Animal Shelter Data came from the following URLs:

Intakes: https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm 
Outcomes: https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238 

### Louisville, KY Shelter Data came from the following URL:
https://portal.louisvilleky.gov/dataset/animal-services-outcomes-data 


### Pre-Processing
City of Austin Animal Center Intake and Outcomes files cleansed separately.  The intake and outcome dates were converted to pandas datetime fields and then split to create two new columns for month and year. The Breed at intake and outcome was transformed using s defined function to a boolean purebred status field. The Sex upon Intake and Sex at Outcome columns contained both the animal sex and the span/neuter status.  These columns were split using mapping to create two new columns, one for animal sex and another for spay/neuter status. The cleansed files were merged matching on the Animal ID.  In the final merged file records without an Animal ID and duplicate records were dropped. An Income to Outcome Days column was calculated by taking the difference of the Outcome datetime minus the Intakes datetime. Based on limited sample size for some animal types, the file was filtered to just Cats and Dogs.

In order to analyze factors that drove how long animals stayed in the shelter system, we needed to calculate the difference between Intake and Outcome times. This involved creating timedelta objects in pandas by subtracting Intake times from Outcome times, and then converting those timedelta objects into “number of days” to provide an integer value that could be used for arithmetic operations (such as computing the mean and standard deviation across different subsets of the data).

## Questions for Analysis
Is there a difference between why cats and dogs are entered into animal shelters and does time of year affect the intake of animals, (i.e do holidays impact the number of dogs or cats taken in)?
What are the outcomes for animals that go into the animal center and does it differ between cats and dogs?  Do purebred dogs have better outcome than mutts?
What are factors that impact time between animal intake and outcome?



## Local Animal Center Analysis

City of Austin Animal Center takes in a wide variety animals categorized in “Animal Type” classifications of Bird, Cat, Dog, Livestock and Other.  

* Bird - 328
* Cat - 28,489
* Dog - 42,590
* Livestock - 8
* Other - 4,162

Due to the limited sample size Birds and Livestock were eliminated from the sample data set.  
For each “Animal Type”  the specific breed is recorded.  For the Other animal type the breed further identifies 91 additional animal types from armadillos to turtles with most common being bats, raccoons, rabbits, opossums and guinea pigs.  

* Bats - 2,049
* Racoons - 678
* Rabbits - 290
* Opossums - 271
* Guinea Pigs - 145

Due to the wide variety of animal types and limited sample size for each, the Other animal type was also eliminated from the final sample data set. 

The final data set contained 57,593 records for animal types Cats and Dogs.

* Cat - 25,896
* Dog - 31,697

The number of annual Animal Intakes were plotted to a bar chart by year to determine if there was any overall change to the number of annual animal intakes.  

![Intakes](/figures/Intakes_Year.png)


The data was further analysed by stacking the Intake types to determine if there were any significant annual changes to animal intakes. Review indicated that proportionally the intake by type remains consistent year over year. 

![Intakes](/figures/Intakes_Type_Year.png)

Intakes were next analyzed to determine if there were any month to month fluctuations.  There was slight variation month to month for dogs; however the fluctuations month to month for cats was very pronounced, with significantly higher volume in warmer months and significantly lower volume colder months.

![Intakes](/figures/Intakes_Month.png)

Stacking the intake type month to month reveals that the fluctuations are attributable to strays. 

![Intakes](/figures/Intakes_Type_Month.png)

Analysis of the annual outcomes reveals that relative to cats dogs as a whole are highly adoptable.  Dogs are also more likely to be returned to their owner.   By contrast cats are most often transferred and have a higher rate of euthanasia.   Euthanasia rates for both cats and dogs have declined; however, dogs have had much better outcomes with euthanasia rates cut in half year over year. 

![Outcome](/figures/Outcomes_Dog_Year.png)

![Outcome](/figures/Outcomes_Cat_Year.png)

There is also a marked difference in the mean number of days to outcome for dogs and cats.  Dogs have a mean adoption time of 23 days versus cats of 39 days.  Dogs are also given more days in shelter before transfer (11 days) as compared to cats (6 days).   The time before euthanasia increased for both cats and dogs; however dogs are given nearly twice as much time before euthanizing. 

![Outcome](/figures/Days_Outcomes_Dog_Year.png)

![Outcome](/figures/Days_Outcomes_Cat_Year.png)

The change in spay neuter status changes dramatically between intake and outcome and is consistent in both cats and dogs with one quarter of animals spayed or neutered at intake and three quarters spayed or neutered at outcome. 

![Spay](/figures/SpayNeuter_intake_Cat.png)

![Spay](/figures/SpayNeuter_outcome_Cat.png)

## Location Analysis

In general, the most animal intakes center around the I-35 corridor, with one large patch south of 290 near downtown, and another north of downtown near 183.
![location](/figures/map1.png)

###Strays vs. Pets in Homes
Stray intakes tended to center around the same corridor in Austin, while intakes from pets in homes were more spread out inside and outside the city.

![location](/figures/map2.png)
![location](/figures/map3.png)

###Dogs vs. Cats
Dog intakes were more prevalent than cat intakes, and more concentrated in the downtown area, and around the I-35/71/183 corridors. Cat intakes tended to be a little more spread out than dog intakes.

![location](/figures/map4.png)
![location](/figures/map5.png)
![location](/figures/map6.png)

###Frequency of Vets
We created a scatter plot of the number of intake addresses within a 1,700 meter radius of all veterinary clinics in Austin.

![location](/figures/map7.png)

* In areas with lowest vet count, the frequency of intakes was highest.
* As vet count increased up to a certain point, intake frequency decreased. 
* In areas with a higher concentration of vets, the number of intakes increased again.
    *  This could imply a higher concentration of animals in more densely-populated areas.
* In one area with the highest concentration of vet clinics, there was a very low intake count. This could imply that a more affluent suburban area required fewer intakes. 


## Louisville vs. Austin

In both the Austin and Louisville datasets contained timestamp data associated with the intake and outcome times for each animal in the system. The difference between these timestamp values therefore represents the total time that each animal spent in the shelter system. We used this information to evaluate how different factors influence the amount of time that animals spend in the system.


### Days from Intake to Outcome
We started with a basic comparison between the two cities to assess whether they showed significant differences in how long animals stayed in their systems. To perform this analysis, we concatenated data from the two cities, created a new variable indicating the city associated with the data, grouped the data by the new “City” variable, and compared the mean Intake-to-Outcome time differences between them.

![Louisville](/figures/time_to_outcome_by_city.png)

This comparison revealed that although Austin’s median time-to-outcome was lower than Louisville’s (5.4 vs 6.0 days), its mean time-to-outcome was higher (17.8 days vs. 13.5 days). An independent samples t-test (assuming unequal variances per results from Levene’s test) revealed that this difference was statistically significant (t = 22.6, p < .001).


### Outcome Type

Outcome type is another factor that could potentially be associated with how long animals stay in the shelter systems.

We used a one-way ANOVA to compare time-to-outcome between cats and dogs (analyzed together and combined across Austin and Louisville) that experienced different outcome types. The vast majority of animals had one of a set of four outcome types: Adoption, Euthanasia, Transfer, and Death. Other outcome types were either mysterious/alarming (e.g., “Disposal”) or had very small sample sizes (e.g., Trap-Neuter-Release) that rendered them unsuitable for analysis.

![Louisville](/figures/time_to_outcome_by_outcome_type.png)

The one-way ANOVA revealed that the difference in means between these four groups was statistically significant (F = 4086.97, p < .001). Specifically, animals that were Adopted were in the system for the longest, with a mean time-to-outcome of 31.1 days. Animals that were euthanized had the shortest time in the system, with an average of only 8.4 days.

Animals that ended up being adopted also had much higher variance in time-to-outcome than animals with other outcome types. This likely reflects efforts to keep adoptable animals in the system for as long as possible, while animals that are unsuitable for adoption (for either behavioral or medical reasons) are either unable or not permitted to spend arbitrarily long periods of time in the shelter system.
