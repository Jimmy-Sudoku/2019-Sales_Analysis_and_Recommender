# <img src="https://i.pinimg.com/originals/8e/24/03/8e24031175b855889b54bce691617263.png" width = "100" height="75"> Google Trends in Canada (April 2023)

# Introduction

There has been a rise in content creator all around the world, espicially in Canada<a href="https://canadianbusiness.com/sponsored-canadas-creator-economy-youtube/" target="_blank"><sup>1</sup></a>. Content creator, sometime known as influencers, is where one generate money through the use of content to communicate with their target audience<a href="https://www.adobe.com/express/learn/blog/content-creator#:~:text=A%20content%20creator%20is%20someone,earn%20revenue%20through%20your%20efforts." target="_blank"><sup>2</sup></a>. 
<br><br>
For content creator, they usually need to find ideas to generate content for the right target audience to earn a living. While doing so, many of them faced creator's block. It causes them to unable to generate creative content/ideas <a href="https://www.freepik.com/blog/improve-creativity-beat-creators-block/#:~:text=Just%20like%20writer's%20block%2C%20creator's,the%20patience%20for%20creator's%20block." target="_blank"><sup>3<sup></a> and this will distrpt their source of income.
One of the ways they find idea is to look for current trending topics or things and Google Trend can be one of the ways to generate ideas for content creators. 
<br><br>
For this project, I will be focusing on Canada and Google Trend will be used.


# Problem Statement

For this project, there are 2 things to find: 
- trending searched terms
- top searched terms

With these data, the content creators facing creator's block, they can use the result above to catch the attention of their target audience and at the same time, generate more income.


# Data Source, Data Cleaning & EDA

The Google Trends datasets are taken from Big Query. Big Query is a data warehouse cloud platform developed by Google itself  <a href="https://cloud.google.com/bigquery." target="_blank"><sup>4<sup></a> . It is free for public to use and SQL is used to clean and query the required data. The data is then saved as csv file for analysis. As I am using the free version of Big Query, there is a limit to much I can use SQL for cleaning, data wrangling analysis and visualisation. Therefore, I used both Excel's power query & power pivot and tableau for additional cleaning, data wrangling analysis and visualisation.


# Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**country_name**|object|Big Query|Country of the dataset.| 
|**region_name**|object|Big Query|Region in Canada.| 
|**refresh_date**|int64|Big Query|The date of when the data is refreshed. Meaning it is where the new set of terms, country, region and combination of scores are added.| 
|**week**|int64|Big Query|The first day of the week. It is used as a time series for the analysis.| 
|**rank**|int64|Big Query|The rank of the top 25 terms for the current dataset, which is based on the refresh date.| 
|**percent_gain**|int64|Big Query|Percentage gain (rate) at which term rose compared to previous date period.| 
|**term**|object|Big Query|The human readable identifier for a term, i.e. 'Acme Inc'.| 
|**score**|int64|Big Query|Presents the maximum search interest of the term for the time and location selected. The index of the value 100 will imply that in the specified time range, a specific term was trending mostly where the peek is, i.e. where the score was highest.| 
|**category**|object|Excel|Category of the term.| 
|**latitude**|int64|Excel|The latitude of the region.|
|**longitude**|int64|Excel|The longitude of the region.|


# Dashboard

Check out the <a href="https://public.tableau.com/app/profile/jimmy5898/viz/GoggleTrendsinCanadaApril2023/storytelling">dashboard</a> that was done using Tableau!
<br>
I have also link a photo of a sample of the google trend from googe for comparsion!


# Limitation

Big Query google trend's dataset only stores the top current 25 terms based on the refreshed date. Meaning, any terms that is less than 25 is not analysed and any terms that is previously in the top 25 terms but not in the current terms are not included in the analysis. In other words, I am only able to analyse the current top 25 terms and the timeline of the current 25 terms.
As there was a change in google's data collection system in 2022, the data before 2022 might be not. Therefore, more studies and data are required. Previous years were not taken in to consideration as comsumer behavior have changed after covid <a href="https://www.mckinsey.com/industries/paper-forest-products-and-packaging/our-insights/beyond-covid-19-the-new-consumer-behavior-is-sticking-in-the-tissue-industry." target="_blank"><sup>5<sup></a>. Therefore, results based on previous years are not used and the dataset only consist of datas after 1st Jan 2022.


# Conclusion & Recommendation

Based on the dashboard, the following are the findings:
- "Premier League" or "EPL", which is a english football league system  <a href="https://en.wikipedia.org/wiki/Premier_League." target="_blank"><sup>6<sup></a>, is the most searched term in April 2023 
- "Blue Jays vs Angels", which is a MBL (Major League Baseball) team match <a href="https://www.espn.com.sg/mlb/game/_/gameId/401471127" target="_blank"><sup>7<sup></a>, is the fastest rising searched term in April 2023

This means that content creator can generate idea based on EPL or MBL to attact more target audience and therefore, increase their income.


# Future Directions

To further improve the results, a recommender system based on machine learning model (Supervised, UnSupervised and deep learning) can be impletmented and it will be another forthcoming project in a foreseeable future.





# Special Mention

I would like to thank the following people/software platoform/websites:
- Kaggle for providing the places for like-minded people to gather and kaggle user @Knightbearr for providing the datasets<a href="https://www.kaggle.com/datasets/knightbearr/sales-product-data/" target="_blank"><sup>1</sup></a> for free for community to use
- Stackoverflow and data science stack exchange for solving coding issues/bugs/ understand concepts
- youtuber @datatutorials1 for the inspiration of tableau ideas
- Tableau for allowing community to publish their findings for free

# Motivation

I am curious about how sales works, what does people usually buys and how does it recommend customer items to buy. Which is why I decided do this project to get some insights.


# Introduction

The dataset is taken from @Knightbearr,a kaggle user, who provided me with these datasets. There are a total of 12 datasets where it is separated by month. Before analyisng, microsoft excel is used to perform ETL (Extract Transform Load), data cleaning and combining the datset into 1 and then after python is used to do EDA and recommender system. [Recommender system is built to improve sales via upselling and cross-selling and increase of conversion rate by up to 45%](https://blog.saleslayer.com/recommendation-systems-ecommerce#collab).

There are also a few task to finding and the below are the tasks:
- How much was earned that Year?
- What was the best month for sales? How much was earned that month?
- What City had the highest number of sales?
- What time should we display adverstisement to maximize likelihood of customer's buying product?
- What products are most often sold together?
- What product sold the most? Why do you think it sold the most? 
- How much probability for next people will ordered USB-C Charging Cable?
- How much probability for next people will ordered iPhone?
- How much probability for next people will ordered Google Phone?
- How much probability other peoples will ordered Wired Headphones?

# Problem Statement

- To answer the tasks above
- Find insights about the customer behaviour
- Build a recommender system to generate more sales by cross-selling and up-selling


# Data Cleaning & EDA

Dataset is downloaded from kaggle, excel is used to to ETL(Extract Transform Load) , data cleaning and combined into 1 csv file for analysis. As I am using the free version of Big Query, there is a limit to much I can use SQL for cleaning, data wrangling analysis and visualisation. Therefore, I used both Excel's power query & power pivot and tableau for additional cleaning, data wrangling analysis and visualisation.


# Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**country_name**|object|Big Query|Country of the dataset.| 
|**region_name**|object|Big Query|Region in Canada.| 
|**refresh_date**|int64|Big Query|The date of when the data is refreshed. Meaning it is where the new set of terms, country, region and combination of scores are added.| 
|**week**|int64|Big Query|The first day of the week. It is used as a time series for the analysis.| 
|**rank**|int64|Big Query|The rank of the top 25 terms for the current dataset, which is based on the refresh date.| 
|**percent_gain**|int64|Big Query|Percentage gain (rate) at which term rose compared to previous date period.| 
|**term**|object|Big Query|The human readable identifier for a term, i.e. 'Acme Inc'.| 
|**score**|int64|Big Query|Presents the maximum search interest of the term for the time and location selected. The index of the value 100 will imply that in the specified time range, a specific term was trending mostly where the peek is, i.e. where the score was highest.| 
|**category**|object|Excel|Category of the term.| 
|**latitude**|int64|Excel|The latitude of the region.|
|**longitude**|int64|Excel|The longitude of the region.|


# Dashboard

Check out the <a href="https://public.tableau.com/app/profile/jimmy5898/viz/2019SalesRecommenderDashboard/Dashboard">dashboard</a> that was done using Tableau!


# Limitation and Further Studies

The limitation for the project are the following :
1. time constraint to complete the project,
2. the limitations of Apriori Algorithm which is it is performance inefficient<a href="https://en.wikipedia.org/wiki/Apriori_algorithm" target="_blank"><sup>2</sup></a>. 
3. More revelent datas for analysis. For example, datas for multiple years, education and income of the customers, and other factors that may affect the buying decisions of the customers.

For further studies, it is possible to explore other algorithm such as max miner<a href="https://www2.cs.sfu.ca/CourseCentral/741/jpei/readings/baya98.pdf" target="_blank"><sup>3</sup></a> or fast miner<a href="https://www.researchgate.net/publication/253105580_Efficiently_mining_maximal_frequent_patterns_fast-miner" target="_blank"><sup>4</sup></a> or FP-growth<a href="https://towardsdatascience.com/fp-growth-frequent-pattern-generation-in-data-mining-with-python-implementation-244e561ab1c3to" target="_blank"><sup>5</sup></a> or FP-max<a href="https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/fpmax/" target="_blank"><sup>6</sup></a> solve the performance inefficiency, getting more data to visualise the trends.


# Conclusion

The key takeaways for this project :
1. Sales
- 34.46 million was earned in Year 2019.
- best month for sale is December and 4.61 million was earned.
- San Francisco has the highest number of sales, around 8.25 million for the year ended 2019.
- most sales product is Macbook pro.
- most sold products is aaa batteries(4-pack). Even though it is the most sold item, it made one of the lowest sales. This means that people buy more lower cost proudcts as compared expensive products.

2. Advertisement recommendation
- recommended advertisement display is around 1900 hours to maximise the likelihood of customers buying the product as that hour has the highest number of sales.

3. Customer purchased analysis
- most often 2 bundle sold products are lightening charging cable and iphone.
- most often 3 bundle sold products are usb-c charging cable , wired headphones , google phone.
- most often 4 bundle sold products are usb-c charging cable , wired headphones , bose soundsport headphones , google phone.
- probability of next people ordering USB-C Charging Cable is 0.12.
- probability of next people ordering Iphone is 0.04.
- probability of next people ordering Google Phone is 0.03.
- probability of next people ordering Wired Headphone is 0.1.
- customers usually only do 1 purchase item.

4. Up-sell recommendations
- usb-c charging cable or wired headphone customers to google phone
- lighwired headphonetning charging cable or apple airpods headphones or wired headphones customers to iphone
- wired headphone customers to iphone or google phone

5. Cross-sell recommendations
- google or vareebadd phone customers to usb-c charging cable or wired headphone customers
- iphone customers to lightning charging cable or apple airpods headphones or wired headphones

