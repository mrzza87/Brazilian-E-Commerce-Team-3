# File Name: gxe_02_olist_dim_date_suite.py
# Creation Date/Time: 2025-06-16 11:20:19.698416

# Usage:
#        from gx_exp_gxe_02_olist_dim_date_suite import build_expectations_gxe_02_olist_dim_date_suite
#        suite = build_expectations_gxe_02_olist_dim_date_suite(suite)

import great_expectations as gx

def build_expectations_gxe_02_olist_dim_date_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToBeOfType(column="date_id", type_="DATE")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="year", min_value=2000, max_value=2030)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="month", min_value=1, max_value=12)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="day", min_value=1, max_value=31)
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeInSet(column="day_name", value_set=['Monday','Tuesday','Wednesday', 'Thursday', 'Friday','Saturday','Sunday'], mostly="0.9")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeInSet(column="month_name", value_set=['January','February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], mostly="0.9")
  suite.add_expectation(exp)
  return suite