# File Name: gxe_05_olist_dim_order_reviews_suite.py
# Creation Date/Time: 2025-06-15 18:19:22.831491

# Usage:
#        from gx_exp_gxe_05_olist_dim_order_reviews_suite import build_expectations_gxe_05_olist_dim_order_reviews_suite
#        suite = build_expectations_gxe_05_olist_dim_order_reviews_suite(suite)

import great_expectations as gx

def build_expectations_gxe_05_olist_dim_order_reviews_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="review_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id_review_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeUnique(column="order_id_review_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="review_score", min_value=1, max_value=5)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="review_comment_title")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="review_comment_message")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="review_creation_date", type_="TIMESTAMP")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="review_answer_timestamp", type_="TIMESTAMP")
  suite.add_expectation(exp)
  return suite