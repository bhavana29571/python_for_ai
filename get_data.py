import requests
from datetime import datetime,timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

today=datetime.now()
weak_ago = today-timedelta(days=7)

start_date=weak_ago.strftime("%Y-%m-%d")
end_date=today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)
#_________________________________________________________________
#loading into pandas


daily_data = data["daily"]

df=pd.DataFrame({
    'date':daily_data["time"],
    'max_temp':daily_data["temperature_2m_max"],
    'min_temp':daily_data["temperature_2m_min"]
})

df['date']=pd.to_datetime(df['date'])#date will be in string format so we need to convert it into date time format

print(df)
 #------------------------------------------------------------------------


 #create a plot 

plt.figure(figsize=(10,6))
plt.plot(df['date'],df['max_temp'],marker='o',label='Max Temp')#here we are plotting the date on x-axis and max_temp on y-axis and marker is o which means circle and label is Max Temp which will be shown in legend
plt.plot(df['date'],df['min_temp'],marker='o',label='Min Temp')#marker is o which means circle and label is Min Temp which will be shown in legend

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Daily Max and Min Temperatures in Paris for the Past Week')
plt.legend() #legend will show the label for each line

plt.xticks(rotation=45)#xticks will be rotated by 45 degree to make it more readable
plt.tight_layout()#tight layout will make sure that the plot is not cut off and everything is visible

plt.savefig('temperature_plot.png')  # Save the plot as a PNG file

plt.show()  # Display the plot

#---------------------------------------------------------------------------


#create a dta folder if not exists

if not os.path.exists('data'):
    os.makedirs('data')

#Save to CSV

df.to_csv('data/temperature_data.csv',index=False) #index=False means we don't want to save the index column in the csv file
print("Data saved to data/temperature_data.csv")



