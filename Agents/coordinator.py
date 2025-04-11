from Agents.health_monitor_agent import HealthMonitorAgent

from Agents.safety_monitor_agent import SafetyMonitorAgent

from Agents.reminder_agent import ReminderAgent

from Utils.alert_service import send_combined_alert



class Coordinator:

    def __init__(self):

        self.health_agent = HealthMonitorAgent()

        self.safety_agent = SafetyMonitorAgent()

        self.reminder_agent = ReminderAgent()



    def run_checks(self, bp, movement):

        alerts_triggered = False



        if self.health_agent.check_bp(bp):

            alerts_triggered = True



        if self.safety_agent.detect_fall(movement):

            alerts_triggered = True



        self.reminder_agent.send_reminder()



        if alerts_triggered:

            send_combined_alert("Emergency: High BP and/or Fall detected. Please check now!")
