# File Name: gxe_01_olist_dim_customers_suite.py
# Creation Date/Time: 2025-06-16 11:20:19.694523

# Usage:
#        from gx_exp_gxe_01_olist_dim_customers_suite import build_expectations_gxe_01_olist_dim_customers_suite
#        suite = build_expectations_gxe_01_olist_dim_customers_suite(suite)

import great_expectations as gx

def build_expectations_gxe_01_olist_dim_customers_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToBeUnique(column="customer_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="customer_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="customer_unique_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToMatchRegex(column="customer_zip_code_prefix", regex="^\\d{5}$")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="customer_city")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="customer_state")
  suite.add_expectation(exp)
  return suite