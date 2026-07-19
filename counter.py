# Counter is a sub-class of dictionary data type of python

from collections import Counter

sales = Counter(
    apple=10,
    banana=20,
    pineapple=24,
    mango=12
)

print("Starting Sales: ", dict(sales))

monday_sales = Counter(
    apple=12,
    mango=10,
    pineapple=13,
    banana=12
)

print("\nMonday Sales: ", dict(monday_sales))

sales.update(monday_sales)
print("\nTotal sales: ", dict(sales))

tuesday_sales = Counter(
    apple=11,
    mango=13,
    pineapple=14,
    banana=11
)

print("\nTuesday Sales: ", dict(tuesday_sales))

sales.update(tuesday_sales)
print("\nTotal sales: ", dict(sales))

print("\nMost common item: ", sales.most_common(1))

loss_items = Counter(
    apple=10,
    mango=9,
    pineapple=8,
    banana=9
)

print("\nLoss of items: ", dict(loss_items))

sales.subtract(loss_items)
print("\nTotal Sales: ", dict(sales))

total_sales = sales.total()
print("\nTotal quantity sold: ", total_sales)