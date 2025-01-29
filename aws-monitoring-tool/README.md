Automated AWS Cloud Configuration Monitoring Tool
here's an MVP (Minimum Viable Product)
This module will use boto3 to scan AWS resources for misconfiguration.
1.Scan EC2 instances for misconfigurations.
2.Scan S3 buckets for public access.
3.Scan IAM policies for overly permissive permissions.
4.Scan RDS instances for public accessibility.


Follow this step before proceeding: pip install boto3 flask pandas matplotlib pytest
and you can start the Flask API using: python api.py
Access the endpoints:

GET /scan

GET /risk-score

GET /remediation

We can also add more AWS services like Lambda, and CloudTrail.
