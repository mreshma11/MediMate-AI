import time



class ReminderAgent:

    def __init__(self):

        self.reminders = ["Take your BP medicine"]



    def send_reminder(self):

        for reminder in self.reminders:

            print(f"[REMINDER] {reminder}")

            time.sleep(1)
