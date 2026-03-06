
import sys
import os
import pytest

# This line adds the "src" folder to Python's search path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# EXPLANATION:
# os.path.dirname(__file__)  = the folder THIS test file is in (tests/)
# '..'                       = go up one level (to tekion-cicd-lab/)
# 'src'                      = go into src/
# os.path.join(...)          = combine them into a path: "tests/../src"
# sys.path.insert(0, ...)    = tell Python "also look HERE for imports"
#
# NOW Python can find calculator.py!

from src.calculator import (
    add,
    subtract,
    multiply,
    divide,
    calculate_dealer_metrics,
)

# EXPLANATION:
# "from calculator import add, subtract, ..."
# This says: From the file calculator.py, import these functions.
# Now we can use add(), subtract(), etc. in our tests.


# ─────────────────────────────────────────
# TEST GROUP 1: Testing the add() function
# ─────────────────────────────────────────

class TestAdd:
    """Tests for the add function.

    WHY A CLASS?
    Grouping related tests into a class keeps things organized.
    All add() tests are together, all subtract() tests are together.
    This is optional — you could use standalone functions too.
    But classes make it cleaner, especially with many tests.
    """

    def test_add_positive_numbers(self):
        """Test: 2 + 3 should equal 5."""
        result = add(2, 3)
        assert result == 5

        # EXPLANATION OF "assert":
        #
        # "assert" = VERIFY that something is true
        #
        # assert result == 5  means:
        #   "I assert (claim) that result equals 5"
        #   If True  → test PASSES ✅
        #   If False → test FAILS ❌
        #
        # It's like saying:
        #   "I guarantee 2 + 3 = 5. Prove me wrong."
        #   If the code is correct, no problem.
        #   If the code is buggy, assert will catch it.

    def test_add_negative_numbers(self):
        """Test: -1 + -1 should equal -2."""
        assert add(-1, -1) == -2

    def test_add_zero(self):
        """Test: 5 + 0 should equal 5."""
        assert add(5, 0) == 5

    def test_add_large_numbers(self):
        """Tekion: Total sales across two months."""
        january_sales = 1500000
        february_sales = 1800000
        total = add(january_sales, february_sales)
        assert total == 3300000


# ─────────────────────────────────────────
# TEST GROUP 2: Testing the subtract() function
# ─────────────────────────────────────────

class TestSubtract:
    def test_subtract_positive(self):
        """Test: 10 - 3 should equal 7."""
        assert subtract(10, 3) == 7

    def test_subtract_resulting_negative(self):
        """Test: 3 - 10 should equal -7."""
        assert subtract(3, 10) == -7

    def test_subtract_dealer_profit(self):
        """Tekion: Calculate dealer profit."""
        revenue = 500000
        costs = 350000
        profit = subtract(revenue, costs)
        assert profit == 150000

# ─────────────────────────────────────────
# TEST GROUP 3: Testing the multiply() function
# ─────────────────────────────────────────

class TestMultiply:
    def test_multiply_positive(self):
        """Test: 4 x 5 should equal 20."""
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        """Test: anything x 0 should equal 0."""
        assert multiply(100, 0) == 0

        # WHY TEST THIS?
        # Multiplying by zero is an "edge case" — a boundary condition.
        # Good tests check normal cases AND weird/extreme cases.
        # Edge cases are where bugs love to hide!

    def test_multiply_negative(self):
        """Test: 3 x -4 should equal -12."""
        assert multiply(3, -4) == -12

    def test_multiply_inventory_value(self):
        """Tekion: Total inventory value.
        A dealer has 45 vehicles at $38,000 each.
        """
        num_vehicles = 45
        avg_price = 38000
        total_value = multiply(num_vehicles, avg_price)
        assert total_value == 1710000


# ─────────────────────────────────────────
# TEST GROUP 4: Testing the divide() function
# ─────────────────────────────────────────

class TestDivide:
    def test_divide_evenly(self):
        """Test: 10 / 2 should equal 5."""
        assert divide(10, 2) == 5

    def test_divide_with_decimal(self):
        """Test: 7 / 2 should equal 3.5."""
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self):
        """Test: dividing by zero should raise an error.

        EXPLANATION OF pytest.raises():

        Sometimes you WANT code to crash — that's the correct behavior.
        Dividing by zero SHOULD raise a ValueError.
        If it doesn't raise an error, that's actually a BUG.

        pytest.raises(ValueError) means:
          "I expect this code to raise a ValueError.
           If it does → test PASSES ✅
           If it doesn't raise anything → test FAILS ❌"

        "match='Cannot divide by zero'" means:
          "And the error message should contain this text."
        """
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

        # WHAT "with" MEANS HERE:
        #
        # "with pytest.raises(ValueError):" creates a context that
        # EXPECTS an error. It's like saying:
        #   "Run the code inside this block.
        #    I know it will crash.
        #    That crash IS the correct behavior.
        #    If it crashes with ValueError → PASS
        #    If it doesn't crash → FAIL"

    def test_average_vehicle_price(self):
        """Tekion: Average price per vehicle.
        Total revenue: $950,000
        Vehicles sold: 25
        Average: $38,000
        """
        total_revenue = 950000
        vehicles_sold = 25
        average = divide(total_revenue, vehicles_sold)
        assert average == 38000


# ─────────────────────────────────────────
# TEST GROUP 5: Testing calculate_dealer_metrics()
# ─────────────────────────────────────────

class TestDealerMetrics:
    def test_basic_metrics(self):
        """Test: Calculate metrics for a list of sales.

        Given 5 sales: [25000, 35000, 42000, 28000, 31000]
        Expected:
          total = 161000
          count = 5
          average = 32200.0
          highest = 42000
          lowest = 25000
        """
        sales = [25000, 35000, 42000, 28000, 31000]
        result = calculate_dealer_metrics(sales)

        # EXPLANATION:
        # result is a dictionary (key-value pairs).
        # result["total_sales"] means "get the value for key total_sales"
        # We check EACH value in the dictionary.

        assert result["total_sales"] == 161000
        assert result["num_transactions"] == 5
        assert result["average_sale"] == 32200.0
        assert result["highest_sale"] == 42000
        assert result["lowest_sale"] == 25000

    def test_single_sale(self):
        """Test: Metrics with only one sale.

        Edge case: What if the dealer only made one sale?
        All metrics should reflect that single sale.
        """
        sales = [45000]
        result = calculate_dealer_metrics(sales)

        assert result["total_sales"] == 45000
        assert result["num_transactions"] == 1
        assert result["average_sale"] == 45000.0
        assert result["highest_sale"] == 45000
        assert result["lowest_sale"] == 45000

    def test_empty_sales_raises_error(self):
        """Test: Empty sales list should raise an error.

        Edge case: What if we pass an empty list?
        The function should refuse and raise ValueError.
        You can't calculate metrics for zero sales.
        """
        with pytest.raises(ValueError, match="Sales list cannot be empty"):
            calculate_dealer_metrics([])

    def test_luxury_dealer_metrics(self):
        """Tekion: A luxury dealer's daily sales.

        A high-end dealer selling luxury vehicles.
        Daily sales: $85K, $92K, $78K, $110K, $95K, $88K
        """
        daily_sales = [85000, 92000, 78000, 110000, 95000, 88000]
        result = calculate_dealer_metrics(daily_sales)

        assert result["total_sales"] == 548000
        assert result["num_transactions"] == 6
        assert result["highest_sale"] == 110000
        assert result["lowest_sale"] == 78000


