#### 🔧 Prerequisites:

- Python 3.8+
- Git
- VS Code (recommended)
- Google Cloud SDK installed and authenticated
- A BigQuery project and dataset created

#### 🧰 Installation Steps:

1. **Clone the GitHub Repository**:

   ```bash
   git clone https://github.com/your-username/brazilian-ecommerce-pipeline.git
   cd brazilian-ecommerce-pipeline
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Meltano**:

   ```bash
   pip install meltano
   meltano install
   ```

4. **Install dbt (for BigQuery)**:

   ```bash
   pip install dbt-bigquery
   ```

5. **Configure Meltano**:

   - Place your raw CSVs in `data/raw/`
   - Edit `meltano.yml` to configure `tap-csv` and `target-bigquery`
   - Run:
     ```bash
     meltano elt tap-csv target-bigquery
     ```

6. **Set Up dbt**:

   ```bash
   cd transform/
   dbt deps
   dbt seed
   dbt run
   dbt test
   ```

7. **Run Jupyter Notebooks (optional)**:

   ```bash
   pip install notebook
   jupyter notebook
   ```

8. **Authentication**:

   - Ensure `gcloud auth application-default login` has been run
   - Set `GOOGLE_APPLICATION_CREDENTIALS` environment variable if needed

---

### 6. Next Steps

- Finalize data validation tests in dbt
- Add orchestration with Dagster (future stretch goal)
- Design and publish dashboard using Looker Studio or Power BI

---

### 7. Summary

This project demonstrates a fully modular, cloud-based ELT pipeline using modern data stack components (Meltano, dbt, BigQuery, GitHub). Each tool was chosen to maximize reproducibility, maintainability, and scalability, with a clear path for testing and visualization.

---

### 8. Team

**Project Name**: Brazilian E-Commerce Team 3\
**GitHub Repo**: [Linked in final submission]\
**GCP Project ID**: `brazilian-ecommerce-team-3`\
**Collaborators**: [Add team names here]

---

*This document is a work-in-progress. Updates will be made as testing and dashboards are finalized.*

