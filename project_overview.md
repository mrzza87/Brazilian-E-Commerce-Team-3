**Module 2 Assignment**

Project Documentation: Brazilian E-Commerce Data Pipeline**

### 1. Overview

This documentation outlines the architecture, tools, and processes used in developing a modern data pipeline for the Brazilian E-Commerce dataset (Olist), selected from Kaggle. The pipeline spans raw data ingestion to model transformation and validation in BigQuery, following modular and scalable engineering practices.

---

### 2. Dataset and Toolset Justification

### 2.1 Dataset Selection

#### 📌 Step 1: Dataset Selection

- **Chosen Dataset**: [Brazilian E-Commerce (Olist)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Justification**:
  - Rich, relational dataset with real-world complexity (orders, reviews, payments, geolocation, etc.)
  - Publicly available and well-documented
  - Suitable for star schema modeling, with clear fact and dimension candidates

### 2.2 Toolset Selection

#### Overall data flow

- ![Add diagram later](https://)


#### 📌 Step 2: GitHub Repository Setup

- **Tool Used**: 
    - `GitHub`
- **Justification**:
  - Version control for team collaboration
  - Central hub to store scripts, configurations, and documentation
  - Integrates seamlessly with Meltano

---

#### 📌 Step 3: Data Ingestion Using Meltano

- **Tool Used**: 
    - `Meltano`
- **Plugins**:
  - `tap-csv` (extractor)
  - `target-bigquery` (loader)
- **Justification**:
  - Open-source ELT framework with YAML-based configuration
  - Easy local development, and future extensibility to orchestrators like Airflow or Dagster
  - Prebuilt taps and targets for CSV and BigQuery

- **Process**:

    - Configured `tap-csv` to load raw `.csv` files from `data/raw/`
    - Connected Meltano to BigQuery via `target-bigquery`
    - Used `meltano elt` to run the ELT job into a staging schema


---

#### 📌 Step 4: Schema Design and Modeling with dbt

- **Tool Used**: 
    - `dbt` (Data Build Tool)
- **Justification**:
  - SQL-based transformation with version-controlled models
  - Easy testing and documentation
  - Supports `BigQuery` backend

**Star Schema Design**:

- **Fact table**: `fact_sales`
- **Dimension tables**: `dim_customers`, `dim_products`, `dim_sellers`, `dim_reviews`, `dim_geolocation`, `dim_payments`, `dim_orders`, `dim_date`, `dim_time`
- **Justification**:
  - Fact table centered around transactional sales
  - Dimensions normalized for efficient joins and filtering
  - Schema supports OLAP-style queries and dashboards

**Files Created**:

- `.sql` models in `/models/`
- Tests (e.g. `not_null`, `unique`) in `schema.yml`
- Sources and documentation in `sources.yml`

---

#### 📌 Step 5: Data Validation and Testing

- **Tool Used**: 
    - `dbt tests`, `Great_Expectations`
- **Justification**:
  - Built-in testing framework with declarative syntax
  - Ensures schema integrity (e.g. primary keys not null, no duplicates)
  - `GE` Documentation is a work in progress

**Tests Written**:

*Status: Ongoing*
- `not_null` and `unique` for all primary keys
- Sanity checks on foreign keys
- Documentation to be completed later.
- 
---

### 3. Pipeline Architecture Diagram

- **Tool**: 
    - `Draw.io` (or Excalidraw)
- **Diagrams**: 
    - `docs/star_schema.drawio` and 
    - `docs/ecommerce_star_schema_valid.drawio`

**High-Level Architecture**:

1. **Raw CSV Files** →
2. **Meltano tap-csv** →
3. **target-bigquery (staging)** →
4. **dbt transformations (models/)** →
5. **BigQuery tables (production)** →
6. **Testing, docs, analysis**

---

### 4. Visual Outputs & Exploratory Analysis
- Work in progress
- Location: `/notebooks/`
  - `fact_order_items.ipynb`
  - `2_fact_table_dimensions_updated.ipynb`
- Processed tables: `/data/processed/`
- Charts/Graphs: Previewed in `.ipynb`, future plans include Looker Studio or Power BI

---