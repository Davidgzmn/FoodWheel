
import pandas as pd
from matplotlib import pyplot as plt

restaurants = pd.read_csv('/Users/david/Documents/GitHub/FoodWheelProject/restaurants.csv')

print(restaurants.head())

unique_cuisine = restaurants.cuisine.nunique()
print(unique_cuisine)

cuisine_counts= restaurants.groupby('cuisine').id.count()
rest_names = restaurants.groupby('cuisine').cuisine.unique()
print(rest_names.head(5))
print(cuisine_counts)
type(rest_names)

restaurant_pie = plt.pie(cuisine_counts, labels=rest_names, autopct='%.1f%%')
plt.axis('equal')
plt.show()
