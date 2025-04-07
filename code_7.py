import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
#If any of this libraries is missing from your computer. Please install them using pip.

filename = 'Flight_Delays_2018.csv'
df = pd.read_csv(filename)

df.boxplot(column="ARR_DELAY", by="CARRIER_DELAY")


plt.title('Flight_Delays_2018.csv')
plt.xlabel('PREDICTED DELAYS IN ARRIVALS')
plt.ylabel('ARR_DELAY')
plt.show()
#ARR_DELAY is the column name that should be used as dependent variable (Y).

