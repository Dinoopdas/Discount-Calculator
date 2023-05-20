# Discount Calculator

This program calculates the total amount payable for a shopping cart based on a catalog of products, discount rules, and user input. It helps determine the subtotal, applicable discounts, shipping fee, gift wrap fee, and the final total amount.

## Table of Contents
- [Description](#description)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

## Description

The code provided is a Python program that allows users to input the quantity of each product from a predefined catalog and specify whether they want gift wrapping for certain products. The program then calculates the subtotal, applies any applicable discounts based on the defined rules, and determines the total amount payable.

The program uses the following components:
- `catalog`: A dictionary containing the products and their prices.
- `discount_rules`: A dictionary defining the discount rules and conditions.
- `product_quantities`: A dictionary storing the user input for product quantities.
- `product_gift_wraps`: A dictionary indicating whether each product should be gift-wrapped.
- `subtotal`: A variable holding the calculated subtotal based on the product quantities and prices.
- `applicable_discounts`: A list containing the names of discounts that apply based on the defined rules.
- `discount_amounts`: A list storing the calculated discount amounts for each applicable discount.
- `discount_name`: A variable holding the name of the applied discount.
- `discount_amount`: A variable storing the discount amount applied.
- `shipping_fee`: A variable holding the calculated shipping fee based on the number of products.
- `gift_wrap_fee`: A variable storing the calculated gift wrap fee.
- `total`: A variable containing the final total amount payable.

## Usage

To use this program, follow these steps:
1. Run the program using a Python interpreter.
2. For each product in the catalog, enter the quantity when prompted.
3. Specify whether you want gift wrapping for each product by entering "yes" or "no."
4. Once all input is provided, the program will calculate and display the product details, subtotal, applied discount, shipping fee, gift wrap fee, and the total amount payable.

## Installation

To run this program, ensure you have Python installed on your machine. You can download Python from the official website: https://www.python.org/downloads/

Once Python is installed, follow these steps:
1. Clone this repository to your local machine using the following command:

       $ git clone https://github.com/Dinoopdas/Discount-Calculator.git
