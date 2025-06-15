# File Name: gxe_07_olist_dim_sellers_suite.py
# Creation Date/Time: 2025-06-15 18:19:22.850188

# Usage:
#        from gx_exp_gxe_07_olist_dim_sellers_suite import build_expectations_gxe_07_olist_dim_sellers_suite
#        suite = build_expectations_gxe_07_olist_dim_sellers_suite(suite)

import great_expectations as gx

def build_expectations_gxe_07_olist_dim_sellers_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToBeUnique(column="seller_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="seller_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToMatchRegex(column="seller_zip_code_prefix", regex="^\\d{5}$")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="seller_city")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="seller_state")
  suite.add_expectation(exp)
  return suite