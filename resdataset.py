#dataset https://github.com/jvns/pandas-cookbook/blob/master/data/bikes.csv
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('data/bikes.csv',
                       sep=';', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')

fixed_df['Berri 1'].plot()
fixed_df.plot(figsize=(15, 10))