# DSAI - Team 3 - Module 2 Project

## Team 3 Project Members:
- LuiKK
- Marissa
- Mark
- Thomas
- Priyanga
- Yogan

# Brazilian E-Commerce Data Pipeline Documentation

## Executive Summary

This documentation provides a comprehensive overview of the Brazilian E-Commerce Team-3 data pipeline project, designed to build an end-to-end data engineering solution using the Brazilian E-Commerce dataset from Kaggle. The project implements a complete ELT pipeline from raw data ingestion through to analytical insights, following modern data engineering best practices.

## 1. Data Pipeline Architecture

### 1.1 High-Level Architecture Overview

![team-3-architecture](/docs/team-3-architecture.png)


The data pipeline follows an ELT (Extract, Load, Transform) approach, which has become the modern standard for cloud-based data warehousing. The architecture consists of the following key components:

**Data Sources**:

- Brazilian E-Commerce Public Dataset by Olist (CSV files)
- Contains 100,000+ orders from 2016-2018 across multiple marketplaces in Brazil

**Data Ingestion Layer**:

- `meltano` using `tap-csv` and `target-bigquery`

**Transformation Layer**:

- `dbt` (data build tool) for data modeling and transformations
- Implementation of star schema design patterns

**Data Testing and Validation Layer**:

- `great_expectations` for data testing and validation

**Data Warehouse**

- `BigQuery` contains all all the tables and transformed views

**Analytics Layer**:

- `Jupyter notebook` for analysis using `python` with `pandas`, `SQLAlchemy`, `matplotlib.pyplot`, `seaborn`

**Orchestration**:

- `Dagster` was intended to be deployed, but since there is low potential for additional data from Kaggle, orchestration as a whole is addressed in the Future Architecture portion.


### 1.2 Data Lineage

Data lineage in this pipeline flows through several distinct stages:

1. **Raw Data Layer**: Original CSV files from Kaggle dataset
2. **Staging Layer**: Ingestion by `meltano` into `BigQuery`
3. **Transformed Layer**: Star schema dimensional model via dbt from `BigQuery` tables into views
4. **Analytics Layer**: Aggregated metrics and KPIs for business intelligence

This lineage enables comprehensive impact analysis and root cause identification when data quality issues arise.

## 2. Technical Architecture Decisions

### 2.1 Technology Stack Justification

**`BigQuery` as Primary Database and Data Warehouse**:

- Chosen for its robust ACID compliance and excellent performance with analytical workloads
- Strong support for complex queries and aggregations required for e-commerce analysis
- Ease of multi-user access 
- Ease of Scalability, Serverless Architecture and Management

**`dbt` for Transformations**:

- Familiarity of tool used in class
- Enables version-controlled, testable SQL transformations
- Built-in data testing capabilities align with project requirements
- Supports modular, reusable code through macros and models

**`Python` in `Jupyter Notebooks` for Analysis**:

- Pandas provides powerful data manipulation capabilities
- Rich ecosystem of visualization libraries (matplotlib, seaborn)


### 2.2 Schema Design Strategy

![star_schema](/docs/ecommerce_star_schema_v1.8.png)

The project implements a **star schema design** optimized for analytical queries. This approach was chosen over a normalized schema for several key reasons:

**Performance Benefits**:

- Denormalized structure reduces join operations in analytical queries
- Dimensional tables support efficient filtering and grouping operations
- Fact table design enables fast aggregation calculations

**Business Intelligence Alignment**:

- Schema structure mirrors business processes (orders, customers, products)
- Supports intuitive dashboard creation and reporting
- Enables drill-down analysis across multiple dimensions


## 3. Data Model Design

### 3.1 Star Schema Implementation

The dimensional model consists of the following key components:

**Fact Tables**:

- `fact_sales_corrected`: Central fact table containing order metrics, foreign keys to dimensions

**Dimension Tables**:

- `dim_products`: Product details
- `dim_order_reviews`: Review scores and feedback data linked to orders
- `dim_payments`: Payment method and transaction details
- `dim_customers`: Customer details and address information
- `dim_sellers`: Seller details and address information
- `dim_geolocation`: Geolocation Data
- `dim_date`: Date dimension for temporal analysis
- `dim_time`: Time dimension for temporal analysis

**Code for creating the Star Schema**

- SQL code in [star_schema.ipynb](/notebooks/star_schema.ipynb)

### 3.2 Schema Benefits for Query Performance

The star schema design provides several performance advantages:

1. **Simplified Joins**: Fact tables connect directly to dimensions, eliminating complex multi-hop joins
2. **Aggregation Efficiency**: Pre-calculated metrics in fact tables speed up analytical queries
3. **Indexing Strategy**: Foreign keys and commonly queried columns can be optimized with targeted indexes

## 4. Data Quality and Testing Framework

### 4.1 Data Quality Measures

Following the project requirements, comprehensive data quality testing includes:

**Completeness Tests**:

- Null value validation across critical fields
- Required field presence verification

**Consistency Tests**:

- Referential integrity between fact and dimension tables
- Data type validation and format checking

**Business Logic Tests**:

- Order total calculations accuracy
- Date range validations (orders within expected timeframes)
- Product category consistency checks


### 4.2 Implementation Approach

Data quality tests are implemented using:

- `dbt`'s built-in testing framework for schema validation
- `Great Expectations` integration for advanced data profiling
    - [/gx/IPYNB/gx_olist_tables_validation.ipynb](/gx/IPYNB/gx_olist_tables_validation.ipynb)



![GX flowchart](/gx/GX-BET3-result.jpg)

## 5. Pipeline Orchestration and Automation

### 5.1 Orchestration Strategy

The pipeline uses dagster for automated scheduling and monitoring through:

**Batch Processing**:

- Weekly ETL runs to process new order data (Current expected frequency)
- Incremental loading strategies to handle large datasets efficiently

**Error Handling**:

- Comprehensive logging and alerting mechanisms
- Data validation checkpoints at each pipeline stage

**Monitoring**:

- Data quality metrics tracking over time
- Pipeline performance monitoring and optimization
- Business KPI trend analysis and alerting


## 6. Key Analytical Insights - The Executive Summaries

For full analytical details, follow the titles to the individual notebooks.

Refer to [/notebooks/analysis_fact_sheet.ipynb](/notebooks/analysis_fact_sheet.ipynb) for a glossery of terms.

### 6.1 Customer Behavior

- [/notebooks/customer_behavior.ipynb](/notebooks/customer_behavior.ipynb)
-  High-value but dissatisfied customers drive disproportionate churn losses—targeted recovery and retention strategies could unlock $468K in annual revenue upside with just $72K investment. 

### 6.2 Geolocation Analysis

- [/notebooks/geolocation_analysis.ipynb](/notebooks/geolocation_analysis.ipynb)
- By addressing extreme delays, optimizing delivery networks, and improving seller compliance, the business can recover ~$700K/year in revenue opportunities while improving customer satisfaction.

### 6.3 Payments & Spending

- [/notebooks/payments_spending.ipynb](/notebooks/payments_spending.ipynb)
- By optimizing payment configurations, improving Boleto recovery, automating installment operations, and introducing predictive CLV models, the business can unlock ~$5.77M in revenue opportunities while improving customer loyalty, retention, and operational efficiency.

### 6.4 Product Seller Analysis

- [/notebooks/product_seller_reviews.ipynb](/notebooks/product_seller_reviews.ipynb)
- By improving seller performance, enhancing product quality controls, and addressing operational delays, the business can recover ~$20M+ in revenue opportunities while improving customer satisfaction.

### 6.5 Purchasing Patterns

- [/notebooks/purchasing_patterns.ipynb](/notebooks/purchasing_patterns.ipynb)
- By optimizing product assortment, targeting bundling opportunities, removing low-performing SKUs, and enhancing loyalty programs, the business can unlock ~$300K+ in revenue and operational cost savings while maximizing customer value.


### 6.6 Returns & Complaints

- [/notebooks/returns_complaints.ipynb](/notebooks/returns_complaints.ipynb)
- By improving product quality controls and addressing geographic risk zones, the business can recover ~$5.7M in revenue opportunities while improving customer satisfaction and protecting long-term customer value. Delivery delay is not a major contributor to returns-related complaints.


## 7. Scalability and Future Enhancements

### 7.1 Architecture Scalability

The current architecture supports several enhancement opportunities:

**Cloud Migration**:

- Potential migration to full cloud data architecture on Google Cloud Services 
- Serverless computing options for cost-effective processing
- Pipeline & Orchestration done on the cloud

**Real-time Processing**:

- Potential to add stream processing implementation for real-time analytics
- Event-driven architecture for immediate data updates

**Advanced Analytics**:

- Comprehensive tools available to build dashboards to monitor any improvement measures implemented by the business, and to build new analysis.
- Machine learning model integration for predictive analytics
- Customer churn prediction and recommendation systems

**Future Architecture Overview**:


![future_architecture](/docs/future-team-3-architecture-dark.png)

### 7.2 Data Governance

Future implementations should include:

- Comprehensive data cataloging and metadata management
- Privacy and security controls for customer data
- Data retention and archival policies


## 8. Conclusion

The Brazilian E-Commerce data pipeline successfully implements a robust, scalable solution for comprehensive e-commerce analytics. The star schema design optimizes query performance while maintaining data integrity, and the chosen technology stack provides a solid foundation for future enhancements.

The pipeline's modular architecture enables easy maintenance and extension, while comprehensive testing ensures data quality and reliability. Key performance indicators demonstrate the business value delivered through this data engineering solution, with clear insights into customer behavior, regional performance, and operational efficiency.

This implementation serves as a strong foundation for advanced analytics initiatives and demonstrates adherence to modern data engineering best practices and principles.

