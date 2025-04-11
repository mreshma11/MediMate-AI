class HealthMonitorAgent:

    def __init__(self):

        self.bp_threshold = 140  # Normal is below 140



    def check_bp(self, bp_value):

        if bp_value > self.bp_threshold:

            return f"[ALERT] High BP detected: {bp_value} mmHg"

        return "BP normal"
