# print Write a program to print the total cost.
# question asked in globallogic , failed to answer

products_dict = {
    "Product A": {"price": 10.0, "quantity": 2},
    "Product B": {"price": 5.0, "quantity": 3},
    "Product C": {"price": 8.0, "quantity": 1},
    "Product D": {"price": 18.0, "quantity": 10}
}

total_cost = 0.0
for product_name, product_info in products_dict.items():
    price = product_info["price"]
    quantity = product_info["quantity"]

    product_cost = price * quantity
    total_cost += product_cost

print("total cost: ", total_cost)



