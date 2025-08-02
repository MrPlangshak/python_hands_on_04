"""
Task 2: Airport Luggage Tracker
At Jos Airport, the luggage department tracked passengers and their luggage weights:

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

- you need to map each user to its corresponding luggage weight value.
Before the flight took off:
- A late passenger "Daisy" checked in with 20kg of luggage.
- Bob’s luggage went missing.
- The staff prepared a daily report before resetting for the next flight.
"""

luggage = [("Alice", 23), ("Bob", 18), ("Charlie", 25)]

mapped_luggage = dict(luggage)
print("Initial Luggage Record:", mapped_luggage)

mapped_luggage["Daisy"] = 20
print("After Adding Daisy:", mapped_luggage)

mapped_luggage.pop("Bob")
print("After Removing Bob:", mapped_luggage)

daily_report = mapped_luggage.copy()
print("Daily Report:", daily_report)

