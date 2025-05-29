### Event Ticketing CLI App

A simple command-line interface (CLI) application for managing users, events, and ticket purchases using Python and SQLAlchemy.

## Data Model Relationships
This application uses SQLAlchemy ORM with the following entity relationships:

User ↔ Ticket:
One user can purchase many tickets (One-to-Many).
A ticket belongs to one user.

Event ↔ Ticket:
One event can have many tickets (One-to-Many).
A ticket is associated with one event.

These relationships are managed through foreign keys:

Ticket.user_id → User.id

Ticket.event_id → Event.id



## Features

- **User Management**: Add, list, update, and delete users.
- **Event Management**: Create,update and list events.
- **Ticketing System**: Purchase, update, view, cancel tickets.
- **SQLite Database**: Lightweight and easy to set up.

---

## Project Structure

ticketing/
│
├── alembic.ini                
├── main.py                    
├── cli.py                     
├── seed.py                    
├── requirements.txt           
├── README.md                  
├── Pipfile                    
├── Pipfile.lock               
│
├── lib/                       
│   ├── __init__.py            
│   ├── models.py              
│   ├── event_manager.db       
│   └── migrations/            
│       ├── env.py             
│       ├── script.py.mako     
│       └── versions/          




##  Setup Instructions

1. **Clone the project**
   ```bash
   git clone https://git@github.com:Biss1996/ticketing.git
   cd ticketing
2. Create virtual environment.
```bash
pipenv install
pipenv shell

3. Run migrations

```bash
alembic upgrade head

4. Seed the database
```bash
python seed.py

5. Run the app
``bash
python main.py


6. Run the interactive CLI menu
```bash
python cli.py
You’ll see a menu to:
        "1": create_user,
        "2": list_users,
        "3": update_user,
        "4": delete_user,
        "5": create_event,
        "6": list_events,
        "7": update_event,
        "8": add_ticket,
        "9": list_tickets,
        "10": update_ticket,
        "11": cancel_ticket,
        "q": exit


### Models Overview
##User
id: Integer (PK)

username: String

email: String (unique)

##Event
id: Integer (PK)

title: String

date: Date

location: String

category: String (e.g. Concert, Conference)

##Ticket
id: Integer (PK)

user_id: ForeignKey to User

event_id: ForeignKey to Event

status: String (e.g., purchased, cancelled)


## Author
Bismark Bett — @Biss1996

 ## MIT License

Copyright 2025 Bismark Bett

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
