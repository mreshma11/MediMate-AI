MediMate is a simple AI-powered assistant that simulates elderly care monitoring. It uses Python agents to detect health issues, falls, and send medication reminders.

---

## 🔍 Features

- Detects high blood pressure
- Simulates fall detection
- Sends medication reminders
- Voice alerts using a basic assistant
- Triggers emergency alerts if needed

---

## 📁 Folder Structure

MediMate/ 
├── Agents/ 
│ ├── health_monitor_agent.py 
│ ├── safety_monitor_agent.py 
│ ├── reminder_agent.py 
│ └── coordinator.py 
├── Voice_interface/ 
│ └── assistant.py 
├── main.py 
├── requirements.txt 
└── README.md



## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the program:
python main.py


---

## 📦 Dependencies

- `pyttsx3` (for voice output)
- 'twilio'  (for own sms host server)

---

## 💡 Notes

- All alerts are simulated with fixed input values
- Console will show alerts and reminders
- No real sensors or external APIs are used

---

## 👩‍💻 Use Case

This is a beginner-friendly prototype for learning how to build modular AI-based Python systems with simulated agents.
