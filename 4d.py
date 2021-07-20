import pandas as pd

data=pd.read_csv("/home/root63/order1.csv")

hr=data['order_hour_of_day'].max()
print("Maximum orders have been placed in hour of the day:",hr)
