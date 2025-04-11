class SafetyMonitorAgent:

    def __init__(self):

        pass



    def detect_fall(self, movement_data):

        if movement_data == "no_movement":

            return "[ALERT] Possible fall detected!"

        return "Movement normal"
