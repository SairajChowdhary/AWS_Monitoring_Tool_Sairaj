# 🔒 Automated AWS Cloud Configuration Monitoring Tool

An **MVP (Minimum Viable Product)** tool for monitoring AWS resources to detect **misconfigurations, security risks, and compliance issues**.
This project uses **boto3, Flask, pandas, and matplotlib** to provide API-based scanning and reporting.

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=F7B42C&background=FFFFFF00&center=true&vCenter=true&width=600&lines=By+Sairaj+Chowdhary;" alt="Animated Typing SVG" />

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=16&pause=1300&color=C0C0C0&background=FFFFFF00&center=true&vCenter=true&width=1000&lines=One+of+the+most+common+causes+of+data+breaches+in+cloud+environments+is+publicly+accessible+S3+buckets;But+With+this+tool;A+company’s+security+team+can+scan+and+immediately+see+if+any+S3+buckets+are+publicly+exposed." alt="Animated Typing SVG" />

---

## 🚀 Features

* **EC2 Scan** → Detects instances with potential misconfigurations(e.g:open ports)
* **S3 Scan** → Flags publicly accessible S3 buckets.
* **IAM Policy Scan** → Identifies overly permissive IAM policies (e.g.,`*` in `Action` or `Resource`)
* **RDS Scan** →  Finds publicly accessible RDS instances.
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
