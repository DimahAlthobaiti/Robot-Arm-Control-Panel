# Robot Arm Control Panel

This Django web application allows you to control and manage the poses of a 6-DOF robot arm using motor sliders (Motor 1 to Motor 6). It includes saving, loading, resetting, and executing movements through a user-friendly interface.

## Features

- Slider-based control for 6 motors (0° to 180°)
- Save motor positions as reusable poses
- Load any pose into the sliders
- Run a pose to activate motors (status tracked)
- Simple page to view latest run (S1 90, S2 120, ...)

## Database Models

- `Pose`: Stores saved motor positions (motor1–motor6)
- `Run`: Stores the last executed motor values with `status`

## Pages

- `/`: Main control panel with sliders and pose table
- `/run/`: Simple page showing the latest run values

## How to run
###1. You need to install folder RobotArm 
###2. Make a database on your Pgadmin 
###3. Add your database info in settings.py where there is a small DATABASE info I did put note there.
###4. Make migrate and migration runs.
###5. You're good to go. 

## Mobile Access 

To access from your phone:
- Make sure PC and phone are on same Wi-Fi
- Run server with:
python manage.py runserver <your-ip>:8000
- Visit `http://<your-ip>:8000` on your phone

- ## Pictures
- 
![Pic2iphoneAccess](https://github.com/user-attachments/assets/9ccf28c8-9caf-4510-9546-0ee937998ebf)
![RuniphoneAccess](https://github.com/user-attachments/assets/dfd0e584-68f0-4c66-bf2e-106a089c1859)
