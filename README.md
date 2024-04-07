# 👁️ User Event Tracker

This Python script tracks user login and logout events on machines and generates a report of current users. It's a handy tool for IT and Cybersecurity professionals to automate user event tracking and reporting tasks.

## 👩‍💻 Usage

1. Clone the Repository:

   ```bash
   git clone https://github.com/your-username/user-event-tracker.git
   ```

2. Navigate to the Directory

   ```bash
   cd user-event-tracker
   ```

3. Run the Script

   ```bash
   python user_event_tracker.py
   ```

4. View the Generated Report:

   The script will display a report of current users on machines in the console.

## ✍️ Customization

You can customize the script by modifying the event data in the events list. Each event should be an instance of the Event class with attributes: event_date, event_type, machine_name, and user.

```python
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
```

## ⚙️ Dependencies

This script does not require any external dependencies.

## 📃 License

Licensed under the MIT License, Copyright © 2024
