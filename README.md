# 2019 Product Sales Analysis and Recommender


## Special Mentions

I would like to thank the following people/software platform/websites:
- Kaggle for providing the places for like-minded people to gather and kaggle user @Knightbearr for providing the datasets<a href="https://www.kaggle.com/datasets/knightbearr/sales-product-data/" target="_blank"><sup>1</sup></a> for free for community to use
- Stackoverflow and data science stack exchange for solving coding issues/bugs/ understand concepts
- youtuber @datatutorials1 for the inspiration of tableau ideas
- Tableau for allowing community to publish their findings for free

## Motivation

I am curious about how sales works, what does people usually buys and how does it recommend customer items to buy. Which is why I decided do this project to get some insights.


## Introduction

The dataset is taken from @Knightbearr,a kaggle user, who provided me with these datasets. There are a total of 12 datasets where it is separated by month. Before analyisng, microsoft excel is used to perform ETL (Extract Transform Load), data cleaning and combining the datset into 1 and then after python is used to do EDA and recommender system. Recommender system is built to improve sales via upselling and cross-selling and increase of conversion rate by up to 45%<a href="https://blog.saleslayer.com/recommendation-systems-ecommerce#collab" target="_blank"><sup>2</sup></a> .

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

## Problem Statement

- To answer the tasks above
- Find insights about the customer behaviour
- Build a recommender system to generate more sales by cross-selling and up-selling


## Data Cleaning & EDA

Dataset is downloaded from kaggle, excel's PowerQuery is used to for ETL(Extract Transform Load), data cleaning and combined into 1 csv file for analysis. Python is used for EDA (Exploratory Data Analysis), data mining and saving different csv files to built a dashboard using Tableau. 


## Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Order ID**|int64|Kaggle|An Order ID is the number system that Amazon uses exclusively to keep track of orders. Each order receives its own Order ID that will not be duplicated. This number can be useful to the seller when attempting to find out certain details about an order such as shipment date or status.| 
|**Product**|object|Kaggle|The product that have been sold.| 
|**Price Each**|float64|Kaggle|The product that have been sold.| 
|**Quantity Ordered**|int64|Kaggle|Ordered Quantity is the total item quantity ordered in the initial order (without any changes).| 
|**Price Each**|float64|Kaggle|The price of each products.| 
|**Order Date**|datetime64[ns]|Kaggle|This is the date the customer is requesting the order be shipped.|
|**Purchase Address**|object|Kaggle|The purchase order is prepared by the buyer, often through a purchasing department. The purchase order, or PO, usually includes a PO number, which is useful in matching shipments with purchases; a shipping date; billing address; shipping address; and the request items, quantities and price.| 
|**Sales**|float64|Kaggle|Sales made from the product. It is derived from Price Each x Quantity Ordered| 
|**City**|object|Kaggle|City where the buyer stays. It is derived from Purchase Address.| 


## Dashboard

Check out the <a href="https://public.tableau.com/app/profile/jimmy5898/viz/2019SalesRecommenderDashboard/Dashboard">dashboard</a> that was done using Tableau!


## Limitation and Further Studies

The limitation for the project are the following :
1. time constraint to complete the project,
2. the limitations of Apriori Algorithm which is it is performance inefficient<a href="https://en.wikipedia.org/wiki/Apriori_algorithm" target="_blank"><sup>3</sup></a>. 
3. More revelent datas for analysis. For example, datas for multiple years, education and income of the customers, and other factors that may affect the buying decisions of the customers.

For further studies, it is possible to explore other algorithm such as max miner<a href="https://www2.cs.sfu.ca/CourseCentral/741/jpei/readings/baya98.pdf" target="_blank"><sup>4</sup></a> or fast miner<a href="https://www.researchgate.net/publication/253105580_Efficiently_mining_maximal_frequent_patterns_fast-miner" target="_blank"><sup>5</sup></a> or FP-growth<a href="https://towardsdatascience.com/fp-growth-frequent-pattern-generation-in-data-mining-with-python-implementation-244e561ab1c3to" target="_blank"><sup>6</sup></a> or FP-max<a href="https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/fpmax/" target="_blank"><sup>7</sup></a> solve the performance inefficiency, getting more data to visualise the trends.


## Conclusion

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

