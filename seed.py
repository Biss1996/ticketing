# seed.py
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, User, Event, Ticket

engine = create_engine('sqlite:///lib/event_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

# Recreate all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

#users
user1 = User(username="Michael", email="Mike@yahoo.com")
user2 = User(username="Nick", email="nick@gmail.com")

event1 = Event(
    title="Tech Expo 2025",
    description="A premier tech event featuring latest innovations.",
    location="Nairobi",
    date=datetime.strptime("2025-06-30", "%Y-%m-%d"),
    category="Technology"
)

event2 = Event(
    title="Coastal Music Fest",
    description="Live music and performances by top artists.",
    location="Mombasa",
    date=datetime.strptime("2025-07-15", "%Y-%m-%d"),
    category="Music"
)

ticket1 = Ticket(user=user1, event=event1, status="confirmed")
ticket2 = Ticket(user=user2, event=event2, status="purchased")

session.add_all([user1, user2, event1, event2, ticket1, ticket2])
session.commit()

print("✅ Database seeded with sample data.")
