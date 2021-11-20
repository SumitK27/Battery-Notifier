import psutil
import winsound
import time

try:
    # Run Forever
    while(True):
        battery = psutil.sensors_battery()
        percent = battery.percent
        isCharging = battery.power_plugged

        # Log Battery level
        print("Battery:", percent)

        # If Laptop is charging and battery is fully charged (100%)
        if (percent >= 100 and isCharging):
            print("Fully Charged!!!")
            winsound.Beep(1000, 500)

        # If Laptop is not connected to charger and battery is low (<= 20%)
        if (percent <= 20 and not isCharging):
            print("Battery Low")
            winsound.Beep(600, 300)
            winsound.Beep(600, 300)

        # Wait for 2min
        time.sleep(120)
        continue

# Handle Interrupts
except KeyboardInterrupt:
    print("Exitted")
