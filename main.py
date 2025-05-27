from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, User, Event, Ticket

engine = create_engine('sqlite:///lib/event_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

# ========== USER FUNCTIONS ==========

def create_user():
    username = input("Username: ")
    email = input("Email: ")
    
    existing_user = session.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()
    if existing_user:
        print("Error: Username or email already exists.")
        return

    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print(f"User created: {user}")

def list_users():
    users = session.query(User).all()
    for user in users:
        print(user)

def update_user():
    try:
        user_id = int(input("User ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    user = session.get(User, user_id)
    if not user:
        print("User not found")
        return

    username = input(f"New username (current: {user.username}): ") or user.username
    email = input(f"New email (current: {user.email}): ") or user.email

    user.username = username
    user.email = email
    session.commit()
    print(f"Updated user: {user}")

def delete_user():
    try:
        user_id = int(input("User ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    user = session.get(User, user_id)
    if not user:
        print("User not found")
        return

    session.delete(user)
    session.commit()
    print("User deleted.")

# ========== EVENT FUNCTIONS ==========

def create_event():
    title = input("Title: ")
    description = input("Description: ")
    location = input("Location: ")
    category = input("Category: ")
    date_str = input("Date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    event = Event(title=title, description=description, location=location, category=category, date=date)
    session.add(event)
    session.commit()
    print(f"Event created: {event}")

def list_events():
    events = session.query(Event).all()
    for event in events:
        print(event)

def update_event():
    try:
        event_id = int(input("Event ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    event = session.get(Event, event_id)
    if not event:
        print("Event not found.")
        return

    title = input(f"Title (current: {event.title}): ") or event.title
    description = input(f"Description (current: {event.description}): ") or event.description
    category = input(f"Category (current: {event.category}): ") or event.category
    location = input(f"Location (current: {event.location}): ") or event.location
    date_str = input(f"Date (YYYY-MM-DD, current: {event.date}): ") or str(event.date)
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date.")
        return

    event.title = title
    event.description = description
    event.category = category
    event.location = location
    event.date = date

    session.commit()
    print(f"Event updated: {event}")

# ========== TICKET FUNCTIONS ==========

def add_ticket():
    try:
        user_id = int(input("User ID: "))
        event_id = int(input("Event ID: "))
        price = int(input("Price: "))
    except ValueError:
        print("Invalid input.")
        return

    user = session.get(User, user_id)
    event = session.get(Event, event_id)
    if not user or not event:
        print("User or Event not found.")
        return

    status = input("Status (default 'available', options: purchased, confirmed, pending): ") or "available"
    if status not in {"available", "purchased", "confirmed", "pending"}:
        print("Invalid status.")
        return

    ticket = Ticket(user_id=user.id, event_id=event.id, status=status, price=price)
    session.add(ticket)
    session.commit()
    print(f"Ticket added: {ticket}")

def list_tickets():
    tickets = session.query(Ticket).all()
    for ticket in tickets:
        print(ticket)

def update_ticket():
    try:
        ticket_id = int(input("Ticket ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        print("Ticket not found.")
        return

    new_event_id = input("New Event ID (Enter to keep current): ")
    new_status = input("New Status (available/purchased/confirmed/pending): ")
    new_price = input("New Price: ")

    try:
        if new_event_id:
            ticket.event_id = int(new_event_id)
        if new_status and new_status in {"available", "purchased", "confirmed", "pending"}:
            ticket.status = new_status
        if new_price:
            ticket.price = int(new_price)
    except ValueError:
        print("Invalid input.")
        return

    session.commit()
    print(f"Ticket updated: {ticket}")

def cancel_ticket():
    try:
        ticket_id = int(input("Ticket ID to cancel: "))
    except ValueError:
        print("Invalid ID.")
        return

    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        print("Ticket not found.")
        return

    ticket.status = "cancelled"
    session.commit()
    print(f"Ticket cancelled: {ticket}")
