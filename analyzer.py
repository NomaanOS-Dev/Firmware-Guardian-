import re
import math

class FirmwareScanner:
    def __init__(self):
        # Common firmware security risk patterns
        self.patterns = {
            "Private RSA Key": r"-----BEGIN (RSA|OPENSSH|PRIVATE) KEY-----",
            "Hardcoded API Key": r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"]([A-Za-z0-9_\-]{16,})['\"]",
            "Hardcoded Password": r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"]([^'\"]{4,})['\"]",
            "IPv4 Address": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
            "AWS Access Key": r"AKIA[0-9A-Z]{16}",
        }

    def scan_text(self, content):
        results = []
        for risk_type, pattern in self.patterns.items():
            matches = re.findall(pattern, content)
            if matches:
                results.append({
                    "type": risk_type,
                    "count": len(matches),
                    "samples": [str(m) for m in matches[:3]]
                })
        return results

    def calculate_entropy(self, data):
        """Calculates Shannon entropy to detect encrypted/compressed blocks."""
        if not data:
            return 0
        entropy = 0
        for x in range(256):
            p_x = data.count(bytes([x])) / len(data)
            if p_x > 0:
                entropy -= p_x * math.log2(p_x)
        return round(entropy, 2)
