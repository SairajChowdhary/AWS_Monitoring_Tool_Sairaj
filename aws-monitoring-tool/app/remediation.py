class Remediation:
    def get_recommendations(self, misconfigurations):
        """Generate remediation steps."""
        recommendations = []
        for misconfig in misconfigurations:
            if misconfig['Issue'] == 'Public IP assigned':
                recommendations.append({
                    'Resource': misconfig['Resource'],
                    'Action': 'Remove public IP or restrict access using security groups.'
                })
            elif misconfig['Issue'] == 'Public access granted':
                recommendations.append({
                    'Resource': misconfig['Resource'],
                    'Action': 'Update bucket policy to restrict public access.'
                })
            elif misconfig['Issue'] == 'Overly permissive policy':
                recommendations.append({
                    'Resource': misconfig['Resource'],
                    'Action': 'Update IAM policy to follow the principle of least privilege.'
                })
            elif misconfig['Issue'] == 'Publicly accessible':
                recommendations.append({
                    'Resource': misconfig['Resource'],
                    'Action': 'Disable public accessibility for the RDS instance.'
                })
        return recommendations
