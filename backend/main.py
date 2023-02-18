from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Float, Double
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Bearing(Base):
    __tablename__ = "bearing"
    id = mapped_column(Integer, primary_key=True)
    status = mapped_column(String(30))
    value = mapped_column(Float)
    bearing_id = mapped_column(ForeignKey("bearing.id"))
    temperature = relationship("Temperature", back_populates="temperature")
    vibration_status = mapped_column(String(30))
    vibrations: Mapped[List["Vibration"]] = relationship(back_populates="bearing")


class Vibration(Base):
    __tablename__ = "vibratios"
    id = mapped_column(Integer, primary_key=True)
    type = mapped_column(String(30))
    status = mapped_column(String(30))
    value = mapped_column(Float)
    bearing_id = mapped_column(ForeignKey("bearing.id"))
    bearing = relationship("Bearing", back_populates="vibrations")


class Temperature(Base):
    __tablename__ = "temperature"
    id = mapped_column(Integer, primary_key=True)
    status = mapped_column(String(30))
    value = mapped_column(Float)
    bearing_id = mapped_column(ForeignKey("bearing.id"))
    bearing = relationship("Bearing", back_populates="temperature")


SQLALCHEMY_DATABASE_URL = "sqlite:///./db.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
    age = Column(Integer, )


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)
