#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, MapType
from pyspark.sql.functions import from_json, col
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium import plugins
from folium.plugins import MarkerCluster
from folium.plugins import FastMarkerCluster


# In[2]:


spark = SparkSession.builder.appName('ISS_stream').getOrCreate()


# ### Spark dataframe

# In[3]:


json_location = (spark.readStream
                      .format('socket')
                      .option('host', 'localhost')
                      .option('port', 22223)
                      .load()
                ) 


# ### Define schema

# In[4]:


json_schema = (StructType([
                    StructField('iss_position', MapType(StringType(), StringType(), False), False),
                    StructField('timestamp', StringType(), False),
                    StructField('message', StringType(), False)])
               )


# ### Parse the json_location object

# In[5]:


iss = (json_location
       .select(from_json(col('value'), json_schema).alias('data'))
       .select('data.*')
       .withColumn('lat', col('iss_position').getItem('latitude'))
       .withColumn('long', col('iss_position').getItem('longitude'))
      )


# ### Create writer

# In[6]:


writer = (iss
         .writeStream
         .format('memory')
         .queryName('issTable')
         .outputMode('append')
         )


# ### Start writer

# In[7]:


streamer = writer.start()


# ### Stop the streamer 

# In[9]:


streamer.stop()


# ### Query spark dataframe

# In[10]:


query_result = spark.sql("select timestamp, lat, long from issTable")
query_result.show()


# ### Manipulate the spark dataframe to pandas dataframe

# In[11]:


pdf = query_result.toPandas()
print(pdf)


# ### Visualize the path of the ISS in that timeframe on a folium map

# In[16]:


m = folium.Map()
for index, row in pdf.iterrows():
    folium.CircleMarker([row['lat'], row['long']],
                        radius=0.01,
                        popup=row['timestamp'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(m)
m


# In[14]:


m.save("hw06_map.html")


# In[ ]:




