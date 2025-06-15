# File Name: gxe_09_olist_fact_sales_suite.py
# Creation Date/Time: 2025-06-15 18:19:22.898158

# Usage:
#        from gx_exp_gxe_09_olist_fact_sales_suite import build_expectations_gxe_09_olist_fact_sales_suite
#        suite = build_expectations_gxe_09_olist_fact_sales_suite(suite)

import great_expectations as gx

def build_expectations_gxe_09_olist_fact_sales_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="order_item_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="order_item_id", min_value=1, max_value=30)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="customer_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="product_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="seller_id")
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
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="price", min_value=0, max_value=10000)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="freight_value", min_value=0, max_value=1000)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="payment_value", min_value=0, max_value=20000)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeInSet(column="payment_type", value_set=['boleto','canceled','credit_card', 'debit_card', 'voucher', 'not_defined'], mostly="0.8")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="review_score", min_value=1, max_value=5)
  suite.add_expectation(exp)
  return suite