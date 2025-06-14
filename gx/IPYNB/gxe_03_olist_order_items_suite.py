# File Name: gxe_03_olist_order_items_suite.py
# Creation Date/Time: 2025-06-14 17:18:47.949024

# Usage:
#        from gx_exp_gxe_03_olist_order_items_suite import build_expectations_gxe_03_olist_order_items_suite
#        suite = build_expectations_gxe_03_olist_order_items_suite(suite)

import great_expectations as gx

def build_expectations_gxe_03_olist_order_items_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="order_item_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="order_item_id", min_value=1, max_value=30)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="seller_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="shipping_limit_date", type_="TIMESTAMP")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="price", min_value=0, max_value=10000)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="freight_value", min_value=0, max_value=1000)
  suite.add_expectation(exp)
  return suite