# 🔒 Automated AWS Cloud Configuration Monitoring Tool

An **MVP (Minimum Viable Product)** tool for monitoring AWS resources to detect **misconfigurations, security risks, and compliance issues**.
This project uses **boto3, Flask, pandas, and matplotlib** to provide API-based scanning and reporting.

By **Sairaj Raman Kumar Chowdhary**

---

## 🚀 Features

* **EC2 Scan** → Detects instances with potential misconfigurations (e.g., open ports).
* **S3 Scan** → Flags publicly accessible S3 buckets.
* **IAM Policy Scan** → Identifies overly permissive IAM policies (e.g., `*` in `Action` or `Resource`).
* **RDS Scan** → Finds publicly accessible RDS instances.
* **Risk Scoring** → Assigns an overall risk score to your AWS environment.
* **Remediation Guidance** → Provides suggestions to fix detected issues.
* **REST API** → Simple endpoints to trigger scans and view results.

---

## 🏗️ Architecture

```text
                +---------------------------+
                |   Flask REST API Layer    |
                |   (api.py)                |
                +-------------+-------------+
                              |
                              v
                 +------------+-------------+
                 |  AWS Scanner Module      |
                 |  (boto3 based)           |
                 +------------+-------------+
                              |
      ---------------------------------------------------
      |                  |                  |           |
      v                  v                  v           v
+------------+    +------------+    +------------+ +------------+
|   EC2      |    |    S3      |    |    IAM     | |    RDS     |
| Scanner    |    | Scanner    |    | Scanner    | | Scanner    |
+------------+    +------------+    +------------+ +------------+
      |                  |                  |           |
      ---------------------------------------------------
                              |
                              v
                 +------------+-------------+
                 | Risk Scoring Engine      |
                 | & Remediation Generator  |
                 +------------+-------------+
                              |
                              v
                +---------------------------+
                |   JSON API Responses      |
                |   /scan /risk-score etc.  |
                +---------------------------+
```

---
## Automated AWS Cloud Configuration Monitoring Tool
here's an MVP (Minimum Viable Product)
This module will use boto3 to scan AWS resources for misconfiguration.
1.Scan EC2 instances for misconfigurations.
2.Scan S3 buckets for public access.
3.Scan IAM policies for overly permissive permissions.
4.Scan RDS instances for public accessibility.


## Follow this step before proceeding: 
Also you can start the Flask API using: python api.py
Access the endpoints:

GET /scan

GET /risk-score

GET /remediation

We can also add more AWS services like Lambda, and CloudTrail.

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/aws-cloud-monitoring.git
   cd aws-cloud-monitoring
   ```

2. Install dependencies:

   ```bash
   pip install boto3 flask pandas matplotlib pytest
   ```

3. Configure AWS credentials:
   Make sure your AWS credentials are available either via:

   * `~/.aws/credentials`
   * Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
   * IAM role if running on EC2

---

## ▶️ Usage

Start the Flask API:

```bash
python api.py
```

### Available Endpoints

* **Run a full scan:**

  ```
  GET /scan
  ```

  Returns details of misconfigurations across EC2, S3, IAM, and RDS.

* **Get environment risk score:**

  ```
  GET /risk-score
  ```

  Provides a consolidated risk score based on findings.

* **Get remediation suggestions:**

  ```
  GET /remediation
  ```

  Suggests actionable steps to fix misconfigurations.

---

## 📊 Example Output

* **Risk Score:**

  ```json
  {
    "risk_score": 72,
    "summary": "High risk due to 2 public S3 buckets and overly permissive IAM policy"
  }
  ```

* **Remediation Example:**

  ```json
  {
    "s3_bucket": "my-bucket",
    "issue": "Publicly accessible",
    "remediation": "Disable public access via S3 Block Public Access settings"
  }
  ```

---

## 🧪 Testing

Run unit tests with:

```bash
pytest
```

---

## 🌱 Roadmap

* [ ] Add **AWS Lambda scanning** (e.g., overly permissive roles, timeouts).
* [ ] Add **CloudTrail logging checks** (detect if disabled or misconfigured).
* [ ] Add **Visualization dashboard** using Flask + matplotlib.
* [ ] Integrate with **Slack/Email alerts** for critical findings.
* [ ] Multi-account scanning support.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and open a PR.

---

## 📜 License

MIT License © 2025 **Sairaj Raman Kumar Chowdhary**

---

👉 Do you also want me to make a **fancy architecture image (PNG/SVG)** with colors and icons (AWS-style) that you can upload to GitHub, or do you prefer keeping the ASCII diagram only?


