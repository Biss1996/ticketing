# from lib.models import session, Event

# def create_event(title, date, location, category):
#     event = Event(title=title, date=date, location=location, category=category)
#     session.add(event)
#     session.commit()
#     return event

# def get_all_events():
#     return session.query(Event).all()

# def get_event_by_id(event_id):
#     return session.query(Event).filter_by(id=event_id).first()

# def filter_events(date=None, location=None, category=None):
#     query = session.query(Event)
#     if date:
#         query = query.filter_by(date=date)
#     if location:
#         query = query.filter_by(location=location)
#     if category:
#         query = query.filter_by(category=category)
#     return query.all()

# def search_events_by_title(title):
#     return session.query(Event).filter(Event.title.ilike(f"%{title}%")).all()
