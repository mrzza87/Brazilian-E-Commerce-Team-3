# File Name: gxe_03_olist_dim_time_suite.py
# Creation Date/Time: 2025-06-15 18:19:22.824537

# Usage:
#        from gx_exp_gxe_03_olist_dim_time_suite import build_expectations_gxe_03_olist_dim_time_suite
#        suite = build_expectations_gxe_03_olist_dim_time_suite(suite)

import great_expectations as gx

def build_expectations_gxe_03_olist_dim_time_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="time_id", type_="TIMESTAMP")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="hour", min_value=0, max_value=23)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="minute", min_value=0, max_value=59)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToMatchRegex(column="time_hhmm", regex="^\\d{2}:\\d{2}$")
  suite.add_expectation(exp)
  return suite