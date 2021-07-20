import pandas as pd

data=pd.read_csv("/home/root63/order1.csv",usecols=["order_dow","order_hour_of_day"]).to_csv("/home/root63/table.csv")
data1=pd.read_csv("/home/root63/table.csv")
print(data1)
