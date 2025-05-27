# from lib.models import session, Ticket, User, Event

# def purchase_ticket(user_id, event_id):
#     ticket = Ticket(user_id=user_id, event_id=event_id)
#     session.add(ticket)
#     session.commit()
#     return ticket

# def get_all_tickets():
#     return session.query(Ticket).all()

# def get_ticket_by_id(ticket_id):
#     return session.query(Ticket).filter_by(id=ticket_id).first()

# def get_user_tickets(user_id):
#     return session.query(Ticket).filter_by(user_id=user_id).all()

# def cancel_ticket(ticket_id):
#     ticket = get_ticket_by_id(ticket_id)
#     if ticket:
#         session.delete(ticket)
#         session.commit()
#     return ticket
