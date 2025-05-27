from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# Base class
Base = declarative_base()


engine = create_engine('sqlite:///lib/event_manager.db')  
Session = sessionmaker(bind=engine)
session = Session()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    tickets = relationship("Ticket", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        tickets_info = [
            f"Ticket(id={t.id}, event_title={t.event.title}, status={t.status})"
            for t in self.tickets
        ]
        return (
            f"<User(id={self.id}, username={self.username}, email={self.email}, "
            f"tickets=[{', '.join(tickets_info)}])>"
        )


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    category = Column(String, nullable=False)  
    tickets = relationship("Ticket", back_populates="event", cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"<Event(id={self.id}, title={self.title}, description={self.description}, date={self.date}, "
            f"location={self.location}, category={self.category})>"
        )


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    price = Column(Integer, nullable=False, default=0)

    status = Column(String, nullable=False, default='available')  # Validate in logic layer

    user = relationship("User", back_populates="tickets")
    event = relationship("Event", back_populates="tickets")

    def __repr__(self):
        return (
            f"<Ticket(id={self.id}, user_id={self.user_id}, "
            f"event_id={self.event_id}, status={self.status})>"
        )
