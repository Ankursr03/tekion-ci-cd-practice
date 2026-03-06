

def add(a, b):
    """Add two numbers together.

    Tekion use case:
      Adding up total vehicle sales for a dealer.
      monday_sales = 15000
      tuesday_sales = 22000
      total = add(monday_sales, tuesday_sales)  → 37000
    """
    return a + b


def subtract(a, b):
    """Subtract b from a.

    Tekion use case:
      Calculating profit.
      revenue = 50000
      costs = 35000
      profit = subtract(revenue, costs)  → 15000
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers.

    Tekion use case:
      Calculating total inventory value.
      num_cars = 12
      price_per_car = 35000
      total_value = multiply(num_cars, price_per_car)  → 420000
    """
    return a * b


def divide(a, b):
    """Divide a by b.

    Tekion use case:
      Calculating average price per vehicle.
      total_revenue = 500000
      cars_sold = 20
      avg_price = divide(total_revenue, cars_sold)  → 25000

    Raises:
      ValueError: If b is zero (can't divide by zero).
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_dealer_metrics(sales_list):
    """Calculate basic metrics for a dealer.

    This is similar to what Tekion's data platform does:
    takes raw sales data and computes summary metrics
    for the dealer dashboard.

    Args:
      sales_list: A list of sale amounts.
        Example: [25000, 35000, 42000, 28000, 31000]

    Returns:
      A dictionary with computed metrics:
        {
          "total_sales": 161000,
          "num_transactions": 5,
          "average_sale": 32200.0,
          "highest_sale": 42000,
          "lowest_sale": 25000
        }

    Raises:
      ValueError: If the sales list is empty.
    """
    if not sales_list:
        raise ValueError("Sales list cannot be empty")

    total = sum(sales_list)
    count = len(sales_list)
    average = divide(total, count)
    highest = max(sales_list)
    lowest = min(sales_list)

    return {
        "total_sales": total,
        "num_transactions": count,
        "average_sale": round(average, 2),
        "highest_sale": highest,
        "lowest_sale": lowest,
    }

# ═══════════════════════════════════════════════════
# NEW FEATURE: Percentage Calculations
# ═══════════════════════════════════════════════════


def percentage(value, percent):
    """Calculate a percentage of a value.

    Tekion use case:
      Calculate dealer commission.
      If dealer gets 3% commission on a $50,000 sale:
        commission = percentage(50000, 3)   → $1,500

    Args:
        value: The base value (e.g., sale price)
        percent: The percentage to calculate (e.g., 3 for 3%)

    Returns:
        The calculated amount.
        percentage(200, 10) → 20.0  (10% of 200 = 20)
    """
    return (value * percent) / 100


def percentage_change(old_value, new_value):
    """Calculate how much something changed in percentage.

    Tekion use case:
      How much did dealer sales grow month over month?
      January: $500,000
      February: $600,000
      Growth: percentage_change(500000, 600000) → 20.0%

    Args:
        old_value: The original value
        new_value: The new value

    Returns:
        Percentage change as a number.
        Positive = growth, Negative = decline.

    Raises:
        ValueError: If old_value is zero (can't calculate change from 0).
    """
    if old_value == 0:
        raise ValueError("Old value cannot be zero")
    return round(((new_value - old_value) / old_value) * 100, 2)


def apply_discount(price, discount_percent):
    """Apply a discount to a price.

    Tekion use case:
      Calculate discounted vehicle price.
      Vehicle listed at $40,000 with 10% discount:
        final_price = apply_discount(40000, 10)  → $36,000

    Args:
        price: Original price
        discount_percent: Discount percentage (must be 0-100)

    Returns:
        Price after discount applied.

    Raises:
        ValueError: If discount is not between 0 and 100.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    discount_amount = percentage(price, discount_percent)
    return price - discount_amount