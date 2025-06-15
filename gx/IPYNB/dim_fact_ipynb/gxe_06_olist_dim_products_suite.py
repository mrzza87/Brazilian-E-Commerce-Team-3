# File Name: gxe_06_olist_dim_products_suite.py
# Creation Date/Time: 2025-06-15 18:19:22.840196

# Usage:
#        from gx_exp_gxe_06_olist_dim_products_suite import build_expectations_gxe_06_olist_dim_products_suite
#        suite = build_expectations_gxe_06_olist_dim_products_suite(suite)

import great_expectations as gx

def build_expectations_gxe_06_olist_dim_products_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToBeUnique(column="product_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="product_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="product_category_name")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="product_name_length", min_value=1, max_value=100)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="product_description_length", min_value=1, max_value=4000)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="product_photos_qty", min_value=0, max_value=25)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="product_weight_g", min_value=0, max_value=50000)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="product_length_cm", min_value=0, max_value=200)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="product_height_cm", min_value=0, max_value=200)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="product_width_cm", min_value=0, max_value=200)
  suite.add_expectation(exp)
  return suite