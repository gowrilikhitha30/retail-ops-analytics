# 📦 Retail Supply Chain & Operations Analytics Pipeline (AOP Case Study)

An enterprise-grade, end-to-end data pipeline and operations analysis ecosystem engineered to automate fulfillment tracking, isolate regional transit bottlenecks, and verify structural data integrity. This repository serves as a technical case study tailored for data-driven operations management.

## 📊 Business Problem Statement
Managing high-volume retail logistics requires strict observation of delivery health and product returns. Surface-level data averages often hide category-specific shipping delays and defect friction. This project automates the extraction of critical operational KPIs to ensure Service Level Agreements (SLAs) are met.

## ⚙️ Architecture & Technical Core Components

### 1. Data Pipeline Automation (`app.py`)
- Programmatically engineers a synthetic operational dataset consisting of **1,000 retail logistics records**.
- Models complex order variables across **4 core product categories** (Electronics, Apparel, Home, Books).
- Automatically exports processed rows into a relational baseline file (`retail_operations_data.csv`).

### 2. Relational Database KPI Extraction (`queries.sql`)
- Contains production-ready SQL scripts to query large tables using advanced groupings (`GROUP BY`).
- Leverages multi-conditional logic (`CASE WHEN`) to isolate **On-Time Delivery Rates (OTDR %)** and **Return Rates (RR %)**.
- Formulates deep-dives to flag high-value order anomalies and regional shipping delays.

### 3. Interactive Visual Dashboard (`dashboard.py`)
- Deploys a responsive web-based user interface using **Streamlit** and **Plotly**.
- Features executive metric cards summarizing gross fulfilled sales volume and logistics performance flags.
- Displays dynamic, real-time fulfillment status distribution graphs for cross-functional stakeholders.

### 4. Data Quality & Audit Layer (`validate_data.py`)
- Implements **3 strict schema assertions** to maintain data pipeline integrity.
- Audits records programmatically to isolate financial anomalies (negative revenue records) before visual rendering.
- Flags logical contradictions, ensuring cancelled orders are isolated from standard return metrics.

### 5. Production Environment & Package Distribution Controls
- Includes `requirements.txt` tracking a **4-dependency environmental control matrix** for clean replication.
- Formulates a modular package architecture setup file (`setup.py`) configured to version **v1.2.0**.

## 📈 Operational Key Performance Indicators (KPIs)
The analytics ecosystem calculates and tracks three vital supply chain metrics:
*   **On-Time Delivery Rate (OTDR %):** Measures fulfillment velocity to pinpoint carrier delay triggers.
*   **Return Rate Percentage (RR %):** Detects category-specific quality defects and customer mismatch trends.
*   **Volume Distribution Matrix:** Groups absolute order volume to track shifting product demands across **4 geographic regions**.
