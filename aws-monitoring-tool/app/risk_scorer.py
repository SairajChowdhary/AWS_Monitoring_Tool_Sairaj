class RiskScorer:
    def __init__(self):
        self.severity_weights = {
            'Critical': 10,
            'High': 7,
            'Medium': 4,
            'Low': 1
        }

    def calculate_risk_score(self, misconfigurations):
        """Calculate overall risk score."""
        total_score = 0
        for misconfig in misconfigurations:
            total_score += self.severity_weights.get(misconfig['Severity'], 0)
        return total_score
