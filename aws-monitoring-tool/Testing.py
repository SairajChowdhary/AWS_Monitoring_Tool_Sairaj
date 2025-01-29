import pytest
from aws_scanner import AWSScanner

def test_scan_ec2_instances():
    scanner = AWSScanner()
    misconfigurations = scanner.scan_ec2_instances()
    assert isinstance(misconfigurations, list)
