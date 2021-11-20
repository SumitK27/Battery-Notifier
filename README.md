# **Battery Notifier** <!-- omit in toc -->

1. [**Description**](#description)
2. [**Packages Used**](#packages-used)
3. [**How to Use**](#how-to-use)
   1. [**Without Installing Python**](#without-installing-python)
   2. [**With Python Installed**](#with-python-installed)
   3. [**To Run Automatically on every boot**](#to-run-automatically-on-every-boot)
4. [**Testing**](#testing)

## **Description**

A CLI based battery notify tool to avoid over or under charge of your system's battery.

## **Packages Used**

-   `psutil` for getting battery stats.
-   `winsound` to produce beep sound from Windows system.
-   `time` to await the execution.

## **How to Use**

Clone the repository.

### **Without Installing Python**

1. Go to `dist` directory.
2. Run `batteryNotifier.exe`.
3. Done. It will run in the background.

### **With Python Installed**

1.  Navigate to this directory.
2.  Open `battery-util.cmd`.
3.  Done. It will open a terminal and log battery percentage.

### **To Run Automatically on every boot**

1. Create a shortcut of the `batteryNotifier.exe` or `battery-util.cmd` (Based on the above use cases)
2. Navigate to `AppData` by pressing `Win` + `R`.
3. Type `%appdata%`.
4. Go to `Microsoft/Windows/Start Menu/Programs/Startup`.
5. Paste the created shortcut there and reboot your system.

## **Testing**

-   You should hear a single beep when battery is fully charged and charger is still plugged in.
-   When charger is not connected and battery is below 20% you shall be notified with two beep sounds.
