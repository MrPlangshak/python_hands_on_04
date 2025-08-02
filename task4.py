"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

# print(participants_snapshot)
# print(participants)

# Initial dictionary of participants
participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}
print(participants)
# A "Guest" participant named "Daisy" joined
participants["Guest"] = "Daisy"
print("After adding Guest:", participants)

# The "Student" participant canceled their registration
participants.pop("Student")
print("After removing Student:", participants)

# Organizers created a record for the day
record = participants.copy()
print("Record for the day:", record)

# Remove the most recently added participant ("Guest") from the live system
participants.pop("Guest")
print("After removing most recent participant:", participants)

