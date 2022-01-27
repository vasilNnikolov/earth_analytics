# Import necessary packages
from traceback import print_tb
import matplotlib.pyplot as plt
import pandas as pd

# Create data
boulder_precip = pd.DataFrame(columns=["date", "precip"], 
                              data=[
                                  ["2013-09-09", 0.1], ["2013-09-10", 1.0], 
                                  ["2013-09-11", 2.3], ["2013-09-12", 9.8], ["2013-09-13", 1.9],
                                  ["2013-09-14", 0.01], ["2013-09-15", 1.4], ["2013-09-16", 0.4]])      
# Create plot
fig, ax = plt.subplots()
ax.bar(boulder_precip['date'].values, boulder_precip['precip'].values)
ax.set(title="Daily Precipitation (inches)\nBoulder, Colorado 2013", 
       xlabel="Date", ylabel="Precipitation (Inches)")
plt.setp(ax.get_xticklabels(), rotation=45)
print(24/4)

plt.show()


