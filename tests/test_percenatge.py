# tests/test_percentage.py
# ═══════════════════════════════════════════════════
# Tests for the percentage calculation functions.
# These tests will run as part of CI when we create a PR.
# ═══════════════════════════════════════════════════

import pytest
import sys
import os

# Add src/ to Python's search path (same as before)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.calculator import percentage, percentage_change, apply_discount


class TestPercentage:
    """Tests for the percentage() function."""

    def test_ten_percent_of_hundred(self):
        """10% of 100 = 10."""
        result = percentage(100, 10)
        assert result == 10

    def test_percentage_of_zero(self):
        """Any percentage of 0 = 0."""
        result = percentage(0, 50)
        assert result == 0

        # EDGE CASE:
        # What if the base value is 0?
        # 50% of 0 should be 0.
        # This catches bugs where code might divide by 0 or crash.

    def test_hundred_percent(self):
        """100% of a value = the value itself."""
        result = percentage(250, 100)
        assert result == 250

    def test_dealer_commission(self):
        """Tekion: 3% commission on a $50,000 sale."""
        commission = percentage(50000, 3)
        assert commission == 1500

    def test_small_percentage(self):
        """0.5% (half a percent) of $10,000."""
        result = percentage(10000, 0.5)
        assert result == 50


class TestPercentageChange:
    """Tests for the percentage_change() function."""

    def test_positive_growth(self):
        """Sales grew from $500K to $600K = 20% growth."""
        result = percentage_change(500000, 600000)
        assert result == 20.0

        # HOW THE MATH WORKS:
        #   (600000 - 500000) / 500000 × 100
        #   = 100000 / 500000 × 100
        #   = 0.2 × 100
        #   = 20.0%

    def test_negative_decline(self):
        """Sales dropped from $600K to $480K = 20% decline."""
        result = percentage_change(600000, 480000)
        assert result == -20.0

        # Negative result means DECLINE (sales went down).
        # This is important for Tekion dashboards — dealers
        # need to see if their performance is dropping.

    def test_no_change(self):
        """Same value = 0% change."""
        result = percentage_change(100, 100)
        assert result == 0.0

    def test_zero_old_value_raises_error(self):
        """Can't calculate change from 0 (division by zero)."""
        with pytest.raises(ValueError, match="Old value cannot be zero"):
            percentage_change(0, 100)

        # WHY THIS IS IMPORTANT:
        # If a dealer had $0 sales last month and $100 this month,
        # what's the percentage change? It's mathematically undefined.
        # (100 - 0) / 0 = division by zero!
        # Our code should raise an error, not crash silently.

    def test_doubling(self):
        """Value doubled = 100% increase."""
        result = percentage_change(100, 200)
        assert result == 100.0

    def test_dealer_monthly_growth(self):
        """Tekion: Dealer sales grew from $1.2M to $1.5M."""
        growth = percentage_change(1200000, 1500000)
        assert growth == 25.0


class TestApplyDiscount:
    """Tests for the apply_discount() function."""

    def test_basic_ten_percent_discount(self):
        """$100 item with 10% discount = $90."""
        result = apply_discount(100, 10)
        assert result == 90

    def test_no_discount(self):
        """0% discount = original price unchanged."""
        result = apply_discount(40000, 0)
        assert result == 40000

    def test_full_discount(self):
        """100% discount = free (price becomes 0)."""
        result = apply_discount(40000, 100)
        assert result == 0

    def test_vehicle_discount(self):
        """Tekion: $40,000 vehicle with 15% discount."""
        final_price = apply_discount(40000, 15)
        assert final_price == 34000

        # 15% of 40000 = 6000
        # 40000 - 6000 = 34000

    def test_discount_over_100_raises_error(self):
        """Discount can't be more than 100%."""
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            apply_discount(100, 150)

    def test_negative_discount_raises_error(self):
        """Discount can't be negative."""
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            apply_discount(100, -10)

        # WHY TEST NEGATIVE?
        # A negative discount would INCREASE the price.
        # That's not a discount! Our code should prevent this.
        # At Tekion, this could mean charging a customer MORE
        # than the listed price — a serious business error.