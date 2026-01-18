# Poofy 📍

**Simulating random GPS locations made easy.**

Poofy is a simple, plug-and-play iOS utility for developers and testers who need to generate random GPX files for location simulation. It allows you to define a center point and a radius, and it will generate a valid GPX file with a random coordinate inside that zone.

## 🚀 Features

*   **Plug & Play**: Easy configuration. No complex setup involved.
*   **Customizable**: Set your own center latitude, longitude, and radius.
*   **Auto-Generation**: Creates `.gpx` files instantly ready for Xcode simulation.
*   **Clean**: Automatically manages old files (cleanup button included).

## 🛠️ Quick Start Guide

### Prerequisites
*   Mac with Xcode installed.
*   iPhone (optional, can run on Simulator).

### 1. Download the Project
Clone this repository to your local machine:
```bash
git clone https://github.com/bamboozledkitty/poofy.git
```

### 2. Configure Your Location
You don't need to know Swift to use this app!
1.  Open the `Poofy.xcodeproj` file in Xcode.
2.  In the project navigator (left sidebar), find the file named `Configuration.swift`.
3.  Edit the values to your desired location:
    ```swift
    // Example: Setting location to New York City
    static let centerLatitude: Double = 40.7128
    static let centerLongitude: Double = -74.0060
    static let radiusInMeters: Double = 100
    ```

### 3. Run the App
1.  Connect your iPhone or select a Simulator from the top bar in Xcode.
2.  Press the **Play** button (or `Cmd + R`).
3.  The app will launch and show your configured center point.
4.  Tap **Generate New Location**.

### 4. How to Use the Generated File
Once the app confirms a file is generated, follow these steps to use it:

1.  **Locate the File**:
    *   Open the **Files** app on your iPhone (or Simulator).
    *   Navigate to **On My iPhone** > **Poofy**.
    *   You will see files named like `RandomLocation_123456.gpx`.

2.  **Transfer to Mac** (if using a real phone):
    *   Long press the file -> **Share** -> **AirDrop** to your Mac.

3.  **Simulate in Xcode**:
    *   Run the app in Xcode.
    *   In the bottom debug bar, look for the **Location Arrow** icon (📍).
    *   Click it and select **Add GPX File...**.
    *   Choose the `.gpx` file you just grabbed.
    *   The location on your device/simulator will instantly jump to the random coordinate!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
