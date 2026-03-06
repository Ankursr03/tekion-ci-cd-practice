

def add(a, b):
    """Add two numbers together.

    Tekion use case:
      Adding up total vehicle sales for a dealer.
      monday_sales = 15000
      tuesday_sales = 22000
      total = add(monday_sales, tuesday_sales)  → 37000
    """
    return a - b


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