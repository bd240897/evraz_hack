from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Float, Double, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Exhauster(Base):
    __tablename__ = "exhauster"
    id = mapped_column(Integer, primary_key=True)
    bearings: Mapped[List["Bearing"]] = relationship(back_populates="exhauster")
    colder = relationship("Colder", back_populates="exhauster")
    gas_collector = relationship("GasCollector", back_populates="exhauster")
    valve_position = relationship("ValvePosition", back_populates="exhauster")
    main_drive = relationship("MainDrive", back_populates="exhauster")
    oil_system = relationship("OilSystem", back_populates="exhauster")
    work = mapped_column(String(30))


class Colder(Base):
    __tablename__ = "colder"
    id = mapped_column(Integer, primary_key=True)
    colder_liquids: Mapped[List["ColderLiquid"]] = relationship(back_populates="colder")
    exhauster_id = mapped_column(ForeignKey("exhauster.id"))
    exhauster = relationship("Exhauster", back_populates="colder")


class ColderLiquid(Base):
    __tablename__ = "colder"
    id = mapped_column(Integer, primary_key=True)
    type = mapped_column(String(30))
    temp_after = mapped_column(Float)
    temp_before = mapped_column(Float)
    colder = relationship("Colder", back_populates="colder_liquids")


class GasCollector(Base):
    __tablename__ = "gas_collector"
    id = mapped_column(Integer, primary_key=True)
    temp_before = mapped_column(Float)
    undpress_before = mapped_column(Float)
    exhauster = relationship("Exhauster", back_populates="gas_collector")


class ValvePosition(Base):
    __tablename__ = "valve_position"
    id = mapped_column(Integer, primary_key=True)
    gas_valve_closed = mapped_column(String(30))
    gas_valve_open = mapped_column(String(30))
    gas_valve_position = mapped_column(String(30))
    exhauster = relationship("Exhauster", back_populates="valve_position")


class MainDrive(Base):
    __tablename__ = "main_drive"
    id = mapped_column(Integer, primary_key=True)
    rotor_current = mapped_column(String(30))
    rotor_voltage = mapped_column(String(30))
    stator_current = mapped_column(String(30))
    stator_voltage = mapped_column(String(30))
    exhauster = relationship("Exhauster", back_populates="main_drive")


class OilSystem(Base):
    __tablename__ = "oil_system"
    id = mapped_column(Integer, primary_key=True)
    oil_level = mapped_column(String(30))
    oil_pressure = mapped_column(String(30))
    exhauster = relationship("Exhauster", back_populates="oil_system")


class Bearing(Base):
    __tablename__ = "bearing"
    id = mapped_column(Integer, primary_key=True)
    status = mapped_column(String(30))
    value = mapped_column(Float)
    bearing_id = mapped_column(ForeignKey("bearing.id"))
    temperature = relationship("Temperature", back_populates="temperature")
    vibration_status = mapped_column(String(30))
    vibrations: Mapped[List["Vibration"]] = relationship(back_populates="bearing")
    exhauster_id = mapped_column(ForeignKey("exhauster.id"))
    exhauster = relationship("Exhauster", back_populates="bearings")


class Vibration(Base):
    __tablename__ = "vibratios"
    id = mapped_column(Integer, primary_key=True)
    type = mapped_column(String(30))
    status = mapped_column(String(30))
    value = mapped_column(Float)
    bearing_id = mapped_column(ForeignKey("bearing.id"))
    bearing = relationship("Bearing", back_populates="vibrations")
    timestamp = mapped_column(DateTime)


class Temperature(Base):
    __tablename__ = "temperature"
    id = mapped_column(Integer, primary_key=True)
    status = mapped_column(String(30))
    value = mapped_column(Float)
    bearing_id = mapped_column(ForeignKey("bearing.id"))
    bearing = relationship("Bearing", back_populates="temperature")
    timestamp = mapped_column(DateTime)


SQLALCHEMY_DATABASE_URL = "sqlite:///./db.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)
