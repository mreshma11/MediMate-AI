import time
from Agents.coordinator import Coordinator
from Utils import sensor_simulation
from Voice_interface.assistant import speak

def main():
    print("🩺 Starting MediMate...\n")
    speak("MediMate monitoring started.")

    coordinator = Coordinator()

    for _ in range(3):  #using for loop for demo video in actual scenario will run in while loop at some specific interval of times
        bp = sensor_simulation.simulate_bp()
        movement = sensor_simulation.simulate_movement()

        print(f"\n[Sensor] BP: {bp}, Movement: {movement}")
        speak(f"New readings. Blood pressure is {bp}. Movement status is {movement.replace('_', ' ')}.")

        coordinator.run_checks(bp=bp, movement=movement)

        time.sleep(5) 

    speak("Monitoring cycle complete.")
    print("\n✅ Monitoring finished.")

if __name__ == "__main__":
    main()
