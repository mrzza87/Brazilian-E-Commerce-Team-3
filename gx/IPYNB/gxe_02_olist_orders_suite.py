# File Name: gxe_02_olist_orders_suite.py
# Creation Date/Time: 2025-06-14 17:18:47.943949

# Usage:
#        from gx_exp_gxe_02_olist_orders_suite import build_expectations_gxe_02_olist_orders_suite
#        suite = build_expectations_gxe_02_olist_orders_suite(suite)

import great_expectations as gx

def build_expectations_gxe_02_olist_orders_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToBeUnique(column="order_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="customer_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeInSet(column="order_status", value_set=['approved','canceled','created', 'delivered', 'invoiced','processing','shipped','unavailable'], mostly="0.8")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="order_purchase_timestamp", type_="TIMESTAMP")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="order_approved_at", type_="TIMESTAMP")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="order_delivered_carrier_date", type_="TIMESTAMP")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="order_delivered_customer_date", type_="TIMESTAMP")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="order_estimated_delivery_date", type_="TIMESTAMP")
  suite.add_expectation(exp)
  return suite