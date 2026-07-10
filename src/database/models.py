from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

Base = declarative_base()


class YellowTrip(Base):

    __tablename__ = "yellow_trips"

    id = Column(Integer, primary_key=True)

    vendor_id = Column(Integer)

    pickup_datetime = Column(DateTime)
    dropoff_datetime = Column(DateTime)

    passenger_count = Column(Float)
    trip_distance = Column(Float)
    ratecode_id = Column(Float)

    pulocationid = Column(Integer)
    dolocationid = Column(Integer)

    payment_type = Column(Integer)

    fare_amount = Column(Float)
    total_amount = Column(Float)

    trip_duration_minutes = Column(Float)

    pickup_hour = Column(Integer)
    pickup_day = Column(Integer)
    pickup_month = Column(Integer)
    pickup_weekday = Column(String(20))

    dataset = Column(String(20))

    is_weekend = Column(Boolean)
    rush_hour = Column(Boolean)

    average_speed_mph = Column(Float)

    trip_category = Column(String(20))


class GreenTrip(Base):

    __tablename__ = "green_trips"

    id = Column(Integer, primary_key=True)

    vendor_id = Column(Integer)

    pickup_datetime = Column(DateTime)
    dropoff_datetime = Column(DateTime)

    passenger_count = Column(Float)
    trip_distance = Column(Float)

    pulocationid = Column(Integer)
    dolocationid = Column(Integer)

    payment_type = Column(Float)

    fare_amount = Column(Float)
    total_amount = Column(Float)

    trip_duration_minutes = Column(Float)

    pickup_hour = Column(Integer)
    pickup_day = Column(Integer)
    pickup_month = Column(Integer)
    pickup_weekday = Column(String(20))

    dataset = Column(String(20))

    is_weekend = Column(Boolean)
    rush_hour = Column(Boolean)

    average_speed_mph = Column(Float)

    trip_category = Column(String(20))


class FHVTrip(Base):

    __tablename__ = "fhv_trips"

    id = Column(Integer, primary_key=True)

    dispatching_base_num = Column(String(20))

    pickup_datetime = Column(DateTime)
    dropoff_datetime = Column(DateTime)

    pulocationid = Column(Float)
    dolocationid = Column(Float)

    affiliated_base_number = Column(String(20))

    trip_duration_minutes = Column(Float)

    pickup_hour = Column(Integer)
    pickup_day = Column(Integer)
    pickup_month = Column(Integer)
    pickup_weekday = Column(String(20))

    dataset = Column(String(20))
    is_weekend = Column(Boolean)

    rush_hour = Column(Boolean)