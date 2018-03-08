
import pandas as pd
from matplotlib import pyplot as plt

restaurants = pd.read_csv('/Users/david/Documents/GitHub/FoodWheelProject/restaurants.csv')

print(restaurants.head())

unique_cuisine = restaurants.cuisine.nunique()
print(unique_cuisine)

cuisine_counts = restaurants.groupby('cuisine').id.count()
rest_names = restaurants.groupby('cuisine').cuisine.unique()
print(rest_names.head(5))
print(cuisine_counts)

restaurant_pie = plt.subplot(3,1,1)
plt.pie(cuisine_counts, labels=rest_names, autopct='%.1f%%')
plt.axis('equal')

orders = pd.read_csv('/Users/david/Documents/GitHub/FoodWheelProject/orders.csv')
print(orders.head())

split_month = lambda row: row.date.split('-')[0]
orders['month'] = orders.apply(split_month, axis=1)
print(orders.head())

avg_order = orders.groupby('month').price.mean()
print(avg_order)
std_order = avg_order.std()
print(std_order)

sales_month = plt.subplot(3,1,2)

sales_month.set_xticks(range(len(avg_order)))
months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
sales_month.set_xticklabels(months)

plt.bar(range(len(avg_order)), avg_order, yerr=std_order, capsize=5)
plt.xlabel("Months")
plt.ylabel("Avg Order Price")
plt.title("Average order price over the last months")
#plt.show()

customer_amount = orders.groupby('customer_id').price.sum()

acg_spent_hist = plt.subplot(3,1,3)
plt.hist(customer_amount, bins=40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Average amount spent by customers')
plt.show()
