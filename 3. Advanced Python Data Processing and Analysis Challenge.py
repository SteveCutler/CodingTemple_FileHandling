# Objective:
# This assignment is aimed at challenging your skills in advanced data processing 
# and analysis using Python. It encompasses a broad range of topics, including file 
# handling, regular expressions, data structures, and complex problem-solving, at a medium-hard difficulty level.

# Task 1: Travel Blog Sentiment Analysis:

#     Problem Statement:
#     Perform sentiment analysis on a collection of travel blog entries stored in 
# travel_blogs.txt. Identify and count the occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") 
# and negative words (e.g., "bad", "disappointing", "poor").

    # - Dataset Example:

    # Travel Blog Entries:

    # 1. "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."

    # 2. "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."

    # 3. "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."

    # 4. "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."

    # 5. "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."

    # 6. "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."

    # 7. "The food on our trip was excellent. We sampled delicious local cuisine at every stop."

    # 8. "The historical tour was enlightening. We learned so much about the culture and heritage of the region."

    # 9. "Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"

#     Code Example:

import os
import re

positive =["amazing", "enjoy", "beautiful"]
negative = ["bad", "disappointing", "poor"]

def analyzeSentiments(file):
    pos = 0
    neg = 0
    with open(file, "r") as file:

        for line in file:
            for word in positive:
                if re.search(r'\b' + re.escape(word) + r'\b', line, re.IGNORECASE):
                    pos +=1
            for word in negative:
                if re.search(r'\b' + re.escape(word) + r'\b', line, re.IGNORECASE):
                    neg +=1
    
    return pos, neg
        


pos, neg = analyzeSentiments("travel_blogs.txt")
print(f"pos = {pos}, neg = {neg}")

#         # Implement sentiment analysis logic on the blog file

#     Expected Outcome:
#     A summary report indicating the number of positive and negative words in the travel blogs, 
# demonstrating the ability to process text data and apply basic sentiment analysis.

# Task 2: Historical Weather Data Compiler

# Problem Statement:
# Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). 
# Each file contains daily temperature data. Calculate the average temperature for each year and identify 
# the year with the highest average.

#     - Dataset Example:
#         File: weather_2020.txt

    # 2020-01-01,5°C
    # 2020-01-15,6°C
    # 2020-02-05,4°C
    # 2020-02-20,7°C
    # 2020-03-10,8°C
    # 2020-03-25,9°C
    # 2020-04-05,12°C
    # 2020-04-20,14°C
    # 2020-05-05,17°C
    # 2020-05-20,19°C
    # 2020-06-05,22°C
    # 2020-06-20,25°C
    # 2020-07-05,28°C
    # 2020-07-20,30°C
    # 2020-08-05,32°C
    # 2020-08-20,31°C
    # 2020-09-05,27°C
    # 2020-09-20,24°C
    # 2020-10-05,19°C
    # 2020-10-20,16°C
    # 2020-11-05,11°C
    # 2020-11-20,9°C
    # 2020-12-05,6°C
    # 2020-12-20,4°C

#         File: weather_2021.txt

    # 2021-01-01,3°C
    # 2021-01-15,4°C
    # 2021-02-05,6°C
    # 2021-02-20,8°C
    # 2021-03-10,10°C
    # 2021-03-25,11°C
    # 2021-04-05,14°C
    # 2021-04-20,16°C
    # 2021-05-05,19°C
    # 2021-05-20,21°C
    # 2021-06-05,24°C
    # 2021-06-20,27°C
    # 2021-07-05,30°C
    # 2021-07-20,32°C
    # 2021-08-05,33°C
    # 2021-08-20,31°C
    # 2021-09-05,28°C
    # 2021-09-20,26°C
    # 2021-10-05,21°C
    # 2021-10-20,18°C
    # 2021-11-05,13°C
    # 2021-11-20,10°C
    # 2021-12-05,7°C
    # 2021-12-20,5°C

#     Code Example:

import os
import re

def compileWeatherData(dir):
    #access directory
    #for each file, go line by line, grab the weather data and add to a list.
    temps = []
    yearlyTemps = {}
    
    contents = os.listdir(dir)

    for files in contents:
        year = re.findall(r"_(.*)\.",files)
        #print(f"year = {year}\n")
        fullPath = os.path.join(dir,files)
        temps = []
        with open(fullPath,"r") as file:
            for line in file:
                
                match = re.findall(r",(.*?)°C",line)
                #print(match)
                if match:
                    temps.append(match)
                    yearlyTemps[year[0]] = temps
            #print(yearlyTemps)
   
    return yearlyTemps

yearlyTemps = compileWeatherData("weatherData")
#print(yearlyTemps)
averageTemps = {}

for keys, values in yearlyTemps.items():
   # print(keys)
    sum = 0
    for x in values:
        x = int(x[0])
        sum += x
        average = sum/len(values)
    averageTemps[keys] = str(round(average))

sortedAverage = sorted(averageTemps.items(), key=lambda item: item[1], reverse=True)

print(f"The year with the highest average temperature was {sortedAverage[0][0]} with an average temperature of {sortedAverage[0][1]}  ")

        
    



#         # Aggregate temperature data and calculate the yearly averages

#     Expected Outcome:
#     An aggregated view of average temperatures for each year and identification of the year with the 
#     highest average temperature, showcasing data aggregation and analysis skills.
