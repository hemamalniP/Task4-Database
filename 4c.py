import pandas as pd

data=pd.read_csv("/home/root63/order1.csv")

dow=data['order_dow'].max()
print("Maximum orders have been placed in day of the week:",dow)
