from flask import Flask, jsonify
from aws_scanner import AWSScanner
from risk_scorer import RiskScorer
from remediation import Remediation

app = Flask(__name__)

@app.route('/scan', methods=['GET'])
def scan():
    scanner = AWSScanner()
    misconfigurations = (
        scanner.scan_ec2_instances() +
        scanner.scan_s3_buckets() +
        scanner.scan_iam_policies() +
        scanner.scan_rds_instances()
    )
    return jsonify(misconfigurations)

@app.route('/risk-score', methods=['GET'])
def risk_score():
    scanner = AWSScanner()
    misconfigurations = (
        scanner.scan_ec2_instances() +
        scanner.scan_s3_buckets() +
        scanner.scan_iam_policies() +
        scanner.scan_rds_instances()
    )
    scorer = RiskScorer()
    score = scorer.calculate_risk_score(misconfigurations)
    return jsonify({'risk_score': score})

@app.route('/remediation', methods=['GET'])
def remediation():
    scanner = AWSScanner()
    misconfigurations = (
        scanner.scan_ec2_instances() +
        scanner.scan_s3_buckets() +
        scanner.scan_iam_policies() +
        scanner.scan_rds_instances()
    )
    remediator = Remediation()
    recommendations = remediator.get_recommendations(misconfigurations)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
