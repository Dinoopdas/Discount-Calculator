catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

discount_rules = {
    "flat_10_discount": {"condition": "cart_total > 200", "discount_amount": 10},
    "bulk_5_discount": {"condition": "any(quantity > 10 for quantity in product_quantities.values())", "discount_percentage": 5},
    "bulk_10_discount": {"condition": "sum(product_quantities.values()) > 20", "discount_percentage": 10},
    "tiered_50_discount": {"condition": "sum(product_quantities.values()) > 30 and any(quantity > 15 for quantity in product_quantities.values())", "discount_percentage": 50}
}

product_quantities = {}
product_gift_wraps = {}

subtotal = 0

for product, price in catalog.items():
    quantity = int(input(f"Enter quantity for {product}: "))
    gift_wrap = input(f"Should {product} be wrapped as a gift? (yes/no): ")
    product_quantities[product] = quantity
    product_gift_wraps[product] = gift_wrap.lower() == "yes"
    subtotal += price * quantity

cart_total = subtotal

applicable_discounts = []

for rule, rule_details in discount_rules.items():
    condition = rule_details["condition"]
    if eval(condition):
        applicable_discounts.append(rule)

discount_amounts = []

for discount in applicable_discounts:
    if "discount_amount" in discount_rules[discount]:
        discount_amounts.append(discount_rules[discount]["discount_amount"])
    else:
        discount_amounts.append(subtotal * discount_rules[discount]["discount_percentage"] / 100)

discount_name = ""
discount_amount = 0

if discount_amounts:
    max_discount_index = discount_amounts.index(max(discount_amounts))
    discount_name = applicable_discounts[max_discount_index]
    discount_amount = discount_amounts[max_discount_index]
    subtotal -= discount_amount

shipping_fee = 5 * (sum(product_quantities.values()) // 10)
gift_wrap_fee = sum(product_quantities[product] for product, gift_wrap in product_gift_wraps.items() if gift_wrap) * 1

total = subtotal + shipping_fee + gift_wrap_fee

print("Product Details:")
for product, quantity in product_quantities.items():
    total_amount = catalog[product] * quantity
    print(f"{product}: Quantity: {quantity}, Total Amount: ${total_amount}")

print(f"Subtotal: ${subtotal}")
print(f"Discount Applied: {discount_name}, Discount Amount: ${discount_amount}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee}")
print(f"Total Amount Payable: ${total}")
