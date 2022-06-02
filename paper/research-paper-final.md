# Big Data in the Aviation Industry

### Abstract

Leveraging big data insights presents a multitude of opportunities for the aviation industry. In this era of explosion of real-time data, the implementation of big data analytics helps to improving passenger experience and allow to predict flight safety. The future aviation concepts require modern big data processing and analysis technologies. In this regard, aviation data provided by International Civil Aviation Organization (ICAO) and tracking tools like FlightRadar24 provide users the capability to track and see the details of daily flights and perform big data analysis and visualizations. By connecting GraphFrames for Apache Spark, DataFrames, and D3 visualizations, it is possible to visualize the scope of all flight connections as noted for all on-time or early departing flights within a flight dataset. The aviation industry can ultimately fuel better and faster decision-making, modeling and predicting future outcomes, and enhanced business intelligence with big data analytics. 

Keywords: Big Data, Aviation, Flight, Spark, GraphFrames


## 1	Introduction
Big data analysis methods have revolutionized how both government and commercial researchers can analyze massive aviation databases that were previously too cumbersome, inconsistent, or irregular to drive high-quality output. The ability to mine massive volumes of data from a myriad of sources to analyze and gain insights has radically altered the dynamics of business functions, marketing, and sales. Aviation is a global enterprise and is one of the biggest industries that have access to various kinds of data from multiple sources. For example, a modern aircraft produces gigabytes of data every day: operational parameters, technical indicators, logs reports. Moreover, the airline industry has been a customer experience expert (pre-flight and flight) with its successful loyalty programs from the beginning. However, most airlines have not taken advantage of big data technology yet. They have access to great data, and with prioritization in data collection and analysis and they could use big data to respond to market trends and customer needs and achieve safety.

Leveraging big data insights bring airlines a great competitive advantage. Using various data sources that airlines have access to will allow companies in calculating real-time predicting metrics to present customers with the right offer at the right time. In this sense, airline big data modeling is big business and it’s driving new revenues for airlines and their loyalty programs. In addition, armed with customers’ behavioral data, airline loyalty programs can hyper-personalize the content customers see, the marketing emails that customers receive, and the prices displayed. In this sense, companies can provide the right incentive to the right person at the right time. The ‘How big data is changing the way we fly’ explains how some airline loyalty programs are feeding behavioral data into their internet booking engines. To optimize and streamline aviation operations, industry leaders and decision-makers need to effectively manage and leverage big data. However, to create meaningful and sustainable plans that address increased air traffic and congestion, air and noise pollution, airport security, and other growing concerns, operators need the right tools and technologies.
This research paper aims to study how big data in the aviation industry is working and its impacts and what kinds of information aviation companies and airlines process every day? It also presented a use case on flight performance and visualization with GraphFrames for Apache Spark. 

## 2	What is Big Data?
Big Data is often described as extremely large data sets that have grown beyond the ability to manage and analyze them with traditional data processing tools. It’s a situation in which data sets have grown to such enormous sizes that conventional information technologies can no longer effectively handle either the size of the data set or the scale and growth of the data set. In other words, the data set has grown so large that it is difficult to manage and even harder to gain value out of it. The primary difficulties are the acquisition, storage, searching, sharing, analytics, and visualization of data. Sources of big data are becoming more complex than those for traditional data because they are being driven by artificial intelligence (AI), mobile devices, social media, and the Internet of Things (IoT).  For example, the different types of data originate from sensors, devices, video/audio, networks, log files, transactional applications, web, and social media  ̶  much of it is generated in real-time and at a very large scale.  

#### 2.1	Characteristics of Big Data
Although there is no commonly accepted definition of big data, it can be defined by some combination of the following characteristics:                                                                                        
•	Volume – Where the amount of data to be stored and analyzed is large enough to require special considerations.                                                                                                    
•	Variety – Where the data consists of multiple types of data, potentially from multiple sources; here we need to consider structured data held in tables or objects for which the metadata is well defined, semi-structured data held as documents or similar where the metadata is contained internally (for example XML documents) or unstructured data, which can be photographs, video or any other form of binary data.                              
•	Velocity – Where the data is produced at high rates and operating on ‘stale’ data is not valuable.            
•	Value – Where the data has perceived or quantifiable benefit to the enterprise or organization using it.       
•	Veracity – Where the correctness of the data can be assessed.                                                  

#### 2.2	Benefits of Big Data Analytics 
The ability to analyze and get insights using big data at a faster rate can provide big benefits to an organization, allowing it to more efficiently use data to answer important questions. Moreover, big data analytics is important because it lets organizations use colossal amounts of data in multiple formats from multiple sources to identify opportunities and risks, helping organizations move quickly and improve their bottom lines.
According to IBM, big data analytics has the following benefits:
1.	Fast, better decision making: Businesses can access a large volume of data and analyze a large variety of sources of data to gain new insights and take action. Get started small and scale to handle data from historical records and in real-time.
2.	Cost reduction and operational efficiency: Flexible data processing and storage tools can help organizations save costs in storing and analyzing large amounts of data. Discover patterns and insights that help you identify and do business more efficiently. 
3.	Improved data-driven go-to-market: Analyzing data from sensors, devices video, logs, transactional applications, web, and social media empowers an organization to be data-driven. Gauge customer needs and potential risks and create new products and services.


## 3	Big Data in the Aviation Industry
Big data analytics is significantly changing the outlook for the aviation industry, economically, strategically, and operationally. Nowadays, due to the rapid development of advanced technologies, a massive amount of real-time data regarding flight information, flight performance, airport conditions, air traffic conditions, weather, ticket prices, passengers’ comments, crew comments, etc., are all available from a diverse set of sources, including flight performance monitoring systems, operational systems of airlines and airports, and social media platforms. 
![Airline big data modeling](https://www.markrs.co/articles/ff_big_data_markrs_copyright.jpg)

Fig 1. How big data is changing the way we fly                                                                    

Image: https://www.traveldatadaily.com/how-big-data-is-changing-the-way-we-fly/                                                                                        
 
With the explosion of data, there is a possibility of improving passenger experience by customizing customer service, predicting aircraft failures for increased flight safety, optimizing air traffic flows, and limiting the impact on the environment. Moreover, building predictions on top of this data will significantly reduce the number of unpleasant surprises, improve flight safety and aircraft economics, provide for reliable planning, and more.

## 4	How are airlines using Big Data?
Big data presents a multitude of opportunities for the aviation industry. Through analysis, airlines can streamline maintenance, improve safety, and cut costs. Moreover, big data can help airlines to have a better understanding of their customer. They can study everyone’s behavior, track their performances, and project future demands. By leveraging big data insights, airlines can develop their operations and marketing strategy, enabling them to stand out in an intensely competitive market. In aviation public databases such as those available from the Federal Aviation Administration (FAA), Bureau of Transportation Statistics, and the International Civil Aviation Organization (ICAO) and other opensource like OpenFlights (https://openflights.org/data.html), there is a wealth of data that has the potential to engage in active learning and to participate in big data research. 

Free Aviation tracking tools like FlightRadar24 provide users the capability to track and see the details of daily flights. Each plane has its unique number, flight origin and destination, number of passengers, route, and terabytes of technical data regarding every single part and component that keeps the aircraft in the air. Then there is the weather data. According to the Airports Council International (ACI), there are over 17,000 commercial airports in the world. Every single one of these airports is vitally interested in weather data. Both airports and airlines want to know about the potential storm, heavy rain, fog, and any other weather phenomenon that could hurt the airport’s work and planes’ routes. 

![Flightradar24 tracking real-time flight information](https://raw.githubusercontent.com/Addis-Get/data603-sp22/ed76aa28a69578a17ba3ff6dc7f98f4cbf4644cf/Tracking%20real-time%20flight%20information.png)
Fig 2. Flightradar24 tracks real-time flight information of aircraft around the world                            


Image: https://www.flightradar24.com


Passenger data is yet another significant source of big data for every airport and airline. In the booking process, each passenger’s identity has to be verified. Each ticket contains information about the flight, seat, class, and personal data. Given each flight can take 100-300 people, on average, over 10 million people are in the air every single day. This shows how big data in the aviation industry works. Presumably, the entire sector of passenger, transportation, and cargo planes is interested in big data including weather data, and with big data applications, airline companies can easily schedule flights and predict delays based on weather data.
![Total-number-of-flights](https://raw.githubusercontent.com/Addis-Get/data603-sp22/ed76aa28a69578a17ba3ff6dc7f98f4cbf4644cf/Total-number-of-flights.png)
Fig 3. Total number of flights tracked by Flightrada24, per day (UTC)                                                                             

Image: https://www.flightradar24.com/data/statistics 
 
## 5	Role of Big Data Analytics in Aviation
The increase of available data in almost every domain raises the necessity of employing algorithms for automated data analysis. Big Data Analytics will completely overhaul the travel experience in the upcoming years. Big data analytics in the aviation industry is effectively using concepts like Demand Forecasting, and Differential Pricing Strategy to generate the maximum revenue. TechVidvan has summarized the role of Big Data Analytics in Aviation as stated below:  
![Role of Big Data Analytics in Aviation Industry]( https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/03/big-data-in-aviation-industry.jpg)
 
Fig 4. Role of Big Data Analytics in Aviation

Image: https://techvidvan.com/tutorials/big-data-aviation/


With Big Data, IoT, and predictive analytics (or any other machine learning algorithm), aviation companies will be able to cut costs and generate new revenue streams. 
The ultimate benefits of big data analytics together with airline business acumen and experience would include timely responses to current and future market demands, better planning and strategically aligned decision making, and a clear understanding and monitoring of all key performance drivers relevant to the airline industry. Achieving these benefits in a timely and intelligent manner will ultimately result in lower operating costs, better customer service, market-leading competitiveness, and increased profit margin and shareholder value.

## 6	Big Data Applications in Aviation - Case Study 

### On-Time Flight Performance with GraphFrames for Apache Spark

According to Databricks, Graph structures are a more intuitive approach to many classes of data problems.  Whether traversing social networks, restaurant recommendations, or flight paths, it is easier to understand these data problems within the context of graph structures: vertices, edges, and properties.  For example, flight data analysis is a classic graph problem as airports are represented by vertices and flights are represented by edges.  As well, there are numerous properties associated with these flights including but not limited to departure delays, plane type, and carrier. 

GraphFrames support general graph processing, similar to Apache Spark’s GraphX library. However, GraphFrames are built on top of Spark DataFrames, resulting in some key advantages:                                                
•	Provide uniform APIs for all 3 languages including Python, Java & Scala.                             
•	Powerful queries: GraphFrames allow users to phrase queries in the familiar, powerful APIs of Spark SQL and DataFrames.                                                                                                        
•	Saving & loading graphs: GraphFrames fully support DataFrame data sources, allowing writing and reading graphs using many formats like Parquet, JSON, and CSV.


GraphFrames provides a scalable and easy way to query and process large graph datasets, which can be used to solve many types of analysis problems. In GraphFrames, vertices and edges are represented as DataFrames, allowing us to store arbitrary data with each vertex and edge.  

Databricks has used GraphFrames within their Databricks notebooks to quickly and easily analyze flight performance data organized in graph structures.  Because they’re using graph structures, they could easily ask several questions that are not as intuitive as tabular structures such as finding structural motifs, airport ranking using PageRank, and shortest paths between cities. GraphFrames leverage the distribution and expression capabilities of the DataFrame API to both simplify your queries and leverage the performance optimizations of the Apache Spark SQL engine.  In addition, with GraphFrames, graph analysis is available in Python, Scala, and Java.


### Visualizing Flights Using D3

A significant feature of the Big Data era is the rise of data visualization. Its basic idea is to show attribute values with multidimensional graphs, i.e., analyze data by using graphical methods from different dimensions. Leveraging the airport D3 visualization, it is possible to get a powerful and fun visualization of flight paths and connections. By connecting GraphFrames, DataFrames, and D3 visualizations, it is possible to visualize the scope of all the flight connections as noted for all on-time or early departing flights within a dataset. In the figure below, the blue circles represent the vertices (that is, airports) where the size of the circle represents the number of edges (that is, flights) in and out of those airports. The black lines are the edges themselves (that is, flights) and their respective connections to the other vertices (that is, airports). Note for any edges that go offscreen, they are representing vertices (that is, airports) in the states of Hawaii and Alaska.

![Visualizing Flights using D3](https://camo.githubusercontent.com/cf3f6f8eabbe9d9c4caf16ada9036e5d11514a5c2af60ee42bfdb76f3f58d2c9/68747470733a2f2f6769746875622e636f6d2f64656e6e79676c65652f64617461627269636b732f626c6f622f6d61737465722f696d616765732f616972706f7274732d64332d6d2e6769663f7261773d74727565)

Fig. 5 Visualizing Flights Using D3

Image: https://mbostock.github.io/d3/talk/20111116/airports.html

One can hover over the airports (blue circle, vertex) in the airports D3 visualization where the lines are the edges (flights). By executing queries against graph structures,  one can perform a lot of powerful data analysis. With GraphFrames, you can leverage the power, simplicity, and performance of the DataFrame API against your graph problems.

## 7	Conclusions

Big data has become an essential requirement for the aviation industry looking to harness its business potential. It helps to build the airline network, improve revenue management, increase customer satisfaction and loyalty, reduce maintenance costs, and improve flight operations. Continuously growing amounts of data sources such as sensors, radars, cameras, weather stations, airports, etc. produce terabytes of high dynamic data each second. The future aviation concepts require modern data storing, data processing, and data analysis technologies. To build a big data solution, it is useful to consider open-source software such as Apache Hadoop, and Apache Spark as cost-effective, flexible data processing and storage tools designed to handle the volume of data being generated everyday.


## References

•	Burmester, G., Ma, H., Steinmetz, D., Hartmannn, S. (2018). Big Data and Data Analytics in Aviation. In: Durak, U., Becker, J., Hartmann, S., Voros, N. (eds) Advances in Aeronautical Informatics. Springer, Cham. https://doi.org/10.1007/978-3-319-75058-3_5

•	Bureau of Transportation Statistics: https://www.transtats.bts.gov/ 

•	P. Domek. (2020). Big Data and the aviation industry – in search for new revenue: https://www.nubeasoft.com/insights/big-data-in-aviation 

•	FAA Aviation Safety Information Analysis and Sharing: https://www.asias.faa.gov

•	Federal Aviation Administration: https://www.faa.gov/data_research/

•	S. Firdous, H. Fathiya, and L. Sadath, "Exploratory Data Analysis on Aviation Dataset," 2021 International Conference on Computational Intelligence and Knowledge Economy (ICCIKE), 2021, pp. 541-546, doi: 10.1109/ICCIKE51210.2021.9410686

•	Flightradar24. Total number of flights tracked by Flightradar24, per day (UTC time), 2019 vs 2020 vs 2021 vs 2022. URL: https://www.flightradar24.com/data/statistics. Accessed Apr 17, 2022

•	IBM. https://www.ibm.com/analytics/big-data-analytics

•	International Civil Aviation Organization (ICAO): https://www.icao.int/sustainability/Pages/eap-statistics-programme.aspx 

•	D. Lee, J. Bradley, B. Chambers & Webops (2016). On-Time Flight Performance with GraphFrames for Apache Spark. https://databricks.com/blog/2016/03/16/on-time-flight-performance-with-graphframes-for-apache-spark.html 

•	C. McDonald (2020). Analyzing Flight Delays with Apache Spark GraphFrames and MapR Database. https://developer.hpe.com/blog/analyzing-flight-delays-with-apache-spark-graphframes-and-mapr-database/. Accessed Apr 15, 2022

•	M. A. Martínez-Prieto, A. Bregon, I. García-Miranda, P. C. Álvarez-Esteban, F. Díaz and D. Scarlatti, "Integrating flight-related information into a (Big) data lake," 2017 IEEE/AIAA 36th Digital Avionics Systems Conference (DASC), 2017, pp. 1-10, doi: 10.1109/DASC.2017.8102023.  

•	M. Ross-Smith. (2017). How Big Data Is Changing The Way We Fly. https://www.traveldatadaily.com/how-big-data-is-changing-the-way-we-fly/ 

•	Sky is the limit for Big Data Analytics in the Aviation Industry. https://techvidvan.com/tutorials/big-data-aviation/ (unpublished)

•	Symington (2022). Mapping the World’s Flight paths with Python: https://towardsdatascience.com/mapping-the-worlds-flight-paths-with-python Accessed Apr 19, 2022

•	Xiangsheng Dou & Albert W. K. Tan, 2020. "Big data and smart aviation information management system," Cogent Business & Management, Taylor & Francis Journals, vol. 7(1), pages 1766736-176
