import boto3

class AWSScanner:
    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.s3 = boto3.client('s3')
        self.iam = boto3.client('iam')
        self.rds = boto3.client('rds')

    def scan_ec2_instances(self):
        """Scan EC2 instances for misconfigurations."""
        instances = self.ec2.describe_instances()
        misconfigurations = []
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                # Check if public IP is assigned
                if 'PublicIpAddress' in instance:
                    misconfigurations.append({
                        'Resource': instance['InstanceId'],
                        'Issue': 'Public IP assigned',
                        'Severity': 'High'
                    })
        return misconfigurations

    def scan_s3_buckets(self):
        """Scan S3 buckets for public access."""
        buckets = self.s3.list_buckets()
        misconfigurations = []
        for bucket in buckets['Buckets']:
            acl = self.s3.get_bucket_acl(Bucket=bucket['Name'])
            for grant in acl['Grants']:
                if 'URI' in grant['Grantee'] and 'AllUsers' in grant['Grantee']['URI']:
                    misconfigurations.append({
                        'Resource': bucket['Name'],
                        'Issue': 'Public access granted',
                        'Severity': 'Critical'
                    })
        return misconfigurations

    def scan_iam_policies(self):
        """Scan IAM policies for overly permissive permissions."""
        policies = self.iam.list_policies(Scope='Local')
        misconfigurations = []
        for policy in policies['Policies']:
            policy_version = self.iam.get_policy_version(
                PolicyArn=policy['Arn'],
                VersionId=policy['DefaultVersionId']
            )
            for statement in policy_version['PolicyVersion']['Document']['Statement']:
                if statement.get('Effect') == 'Allow' and statement.get('Resource') == '*':
                    misconfigurations.append({
                        'Resource': policy['PolicyName'],
                        'Issue': 'Overly permissive policy',
                        'Severity': 'High'
                    })
        return misconfigurations

    def scan_rds_instances(self):
        """Scan RDS instances for public accessibility."""
        instances = self.rds.describe_db_instances()
        misconfigurations = []
        for instance in instances['DBInstances']:
            if instance['PubliclyAccessible']:
                misconfigurations.append({
                    'Resource': instance['DBInstanceIdentifier'],
                    'Issue': 'Publicly accessible',
                    'Severity': 'High'
                })
        return misconfigurations
