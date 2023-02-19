import json
from datetime import datetime
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped

from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from backend.recieve.step_1 import main as step


Base = declarative_base()


class Exhauster(Base):
    __tablename__ = "exhauster"
    id = Column(Integer, primary_key=True, index=True)
    bearings = relationship("Bearing", back_populates="exhauster")
    colder = relationship("Colder", back_populates="exhauster")
    gas_collector = relationship("GasCollector", back_populates="exhauster")
    valve_position = relationship("ValvePosition", back_populates="exhauster")
    main_drive = relationship("MainDrive", back_populates="exhauster")
    oil_system = relationship("OilSystem", back_populates="exhauster")
    work = Column(String(30))


class Colder(Base):
    __tablename__ = "colder"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    colder_liquids = relationship("ColderLiquid", back_populates="colder")
    exhauster_id = Column(Integer, ForeignKey("exhauster.id"))
    exhauster = relationship("Exhauster", back_populates="colder")


# TODO back_populates поменять backref

class ColderLiquid(Base):
    __tablename__ = "colder_liquid"
    id = Column(Integer, primary_key=True)
    type = Column(String(30))
    temp_after = Column(Float)
    temp_before = Column(Float)
    colder = relationship("Colder", back_populates="colder_liquids")


class GasCollector(Base):
    __tablename__ = "gas_collector"
    id = Column(Integer, primary_key=True)
    temp_before = Column(Float)
    undpress_before = Column(Float)
    exhauster_id = Column(ForeignKey("exhauster.id"))
    exhauster = relationship("Exhauster", back_populates="gas_collector")


class ValvePosition(Base):
    __tablename__ = "valve_position"
    id = Column(Integer, primary_key=True)
    gas_valve_closed = Column(String(30))
    gas_valve_open = Column(String(30))
    gas_valve_position = Column(String(30))
    exhauster_id = Column(ForeignKey("exhauster.id"))
    exhauster = relationship("Exhauster", back_populates="valve_position")


class MainDrive(Base):
    __tablename__ = "main_drive"
    id = Column(Integer, primary_key=True)
    rotor_current = Column(String(30))
    rotor_voltage = Column(String(30))
    stator_current = Column(String(30))
    stator_voltage = Column(String(30))
    exhauster_id = Column(ForeignKey("exhauster.id"))
    exhauster = relationship("Exhauster", back_populates="main_drive")


class OilSystem(Base):
    __tablename__ = "oil_system"
    id = Column(Integer, primary_key=True)
    oil_level = Column(String(30))
    oil_pressure = Column(String(30))
    exhauster_id = Column(ForeignKey("exhauster.id"))
    exhauster = relationship("Exhauster", back_populates="oil_system")


class Bearing(Base):
    __tablename__ = "bearing"
    id = Column(Integer, primary_key=True)
    status = Column(String(30))
    value = Column(Float)
    bearing_id = Column(ForeignKey("bearing.id"))
    temperature = relationship("Temperature", back_populates="temperature")
    vibration_status = Column(String(30))
    vibrations = relationship("Vibration", back_populates="bearing")
    exhauster_id = Column(ForeignKey("exhauster.id"))
    exhauster = relationship("Exhauster", back_populates="bearings")


class Vibration(Base):
    __tablename__ = "vibrations"
    id = Column(Integer, primary_key=True)
    type = Column(String(30))
    status = Column(String(30))
    value = Column(Float)
    bearing_id = Column(ForeignKey("bearing.id"))
    bearing = relationship("Bearing", back_populates="vibrations")
    timestamp = Column(DateTime)


class Temperature(Base):
    __tablename__ = "temperature"
    id = Column(Integer, primary_key=True)
    status = Column(String(30))
    value = Column(Float)
    bearing_id = Column(ForeignKey("bearing.id"))
    bearing = relationship("Bearing", back_populates="temperature")
    timestamp = Column(DateTime)


SQLALCHEMY_DATABASE_URL = "sqlite:///./db.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()
app = FastAPI()

# @app.get("/")
# def read_root():
#     html_content = "<h2>Hello METANIT.COM!</h2>"
#     return HTMLResponse(content=html_content)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


# @app.get("/")
# async def get():
#     people = db.query(Exhauster).all()
#     for p in people:
#         print(f"{p.id}")
#     return HTMLResponse(html)


# @app.post("/")
# async def post():
#     pass
# #get data from kafka


# async def collect_last_data():
#     people = db.query(Exhauster).all()
#     for p in people:
#         print(f"{p.id}")


@app.get("/get-first-screen")
def first_screen():
    js = json.loads(step())
    for k, v in js.items():
        # print(v)
        for k1, v1 in v.items():
            # print(v1)
            for k2, v2 in v1.items():
                if k2 == 'temperature':
                    # print('temp')
                    # print(js[k][k1][k2])
                    js[k][k1][k2]['flag'] = 'norm'
                    if js[k][k1][k2]['value'] >= js[k][k1][k2]['temp_w_max'] or js[k][k1][k2]['value'] <= js[k][k1][k2]['temp_w_min']:
                        js[k][k1][k2]['flag'] = 'warning'
                    if js[k][k1][k2]['value'] >= js[k][k1][k2]['temp_a_max'] or js[k][k1][k2]['value'] <= js[k][k1][k2]['temp_a_min']:
                        js[k][k1][k2]['flag'] = 'alarm'
                    del js[k][k1][k2]['temp_w_max']
                    del js[k][k1][k2]['temp_w_min']
                    del js[k][k1][k2]['temp_a_max']
                    del js[k][k1][k2]['temp_a_min']

                elif k2 == 'vibration_axial':
                    # print('vibration_axial')
                    # print(js[k][k1][k2])
                    js[k][k1][k2]['flag'] = 'norm'
                    if js[k][k1][k2]['value'] >= js[k][k1][k2]['vibration_a_w_max'] or js[k][k1][k2]['value'] <= js[k][k1][k2][
                        'vibration_a_w_min']:
                        js[k][k1][k2]['flag'] = 'warning'
                    if js[k][k1][k2]['value'] >= js[k][k1][k2]['vibration_a_a_max'] or js[k][k1][k2]['value'] <= js[k][k1][k2][
                        'vibration_a_a_min']:
                        js[k][k1][k2]['flag'] = 'alarm'
                    del js[k][k1][k2]['vibration_a_w_max']
                    del js[k][k1][k2]['vibration_a_w_min']
                    del js[k][k1][k2]['vibration_a_a_max']
                    del js[k][k1][k2]['vibration_a_a_min']
                elif k2 == 'vibration_horizontal':
                    # print('vibration_horizontal')
                    # print(js[k][k1][k2])
                    js[k][k1][k2]['flag'] = 'norm'
                    if js[k][k1][k2]['value'] >= js[k][k1][k2]['vibration_h_w_max'] or js[k][k1][k2]['value'] <= \
                            js[k][k1][k2][
                                'vibration_h_w_min']:
                        js[k][k1][k2]['flag'] = 'warning'
                    if js[k][k1][k2]['value'] >= js[k][k1][k2]['vibration_h_a_max'] or js[k][k1][k2]['value'] <= \
                            js[k][k1][k2][
                                'vibration_h_a_min']:
                        js[k][k1][k2]['flag'] = 'alarm'
                    del js[k][k1][k2]['vibration_h_w_max']
                    del js[k][k1][k2]['vibration_h_w_min']
                    del js[k][k1][k2]['vibration_h_a_max']
                    del js[k][k1][k2]['vibration_h_a_min']
                elif k2 == 'vibration_vertical':
                    # print('vibration_vertical')
                    # print(js[k][k1][k2])
                    js[k][k1][k2]['flag'] = 'norm'
                    if js[k][k1][k2]['value'] >= js[k][k1][k2]['vibration_v_w_max'] or js[k][k1][k2]['value'] <= \
                            js[k][k1][k2][
                                'vibration_v_w_min']:
                        js[k][k1][k2]['flag'] = 'warning'
                    if js[k][k1][k2]['value'] >= js[k][k1][k2]['vibration_v_a_max'] or js[k][k1][k2]['value'] <= \
                            js[k][k1][k2][
                                'vibration_v_a_min']:
                        js[k][k1][k2]['flag'] = 'alarm'
                    del js[k][k1][k2]['vibration_v_w_max']
                    del js[k][k1][k2]['vibration_v_w_min']
                    del js[k][k1][k2]['vibration_v_a_max']
                    del js[k][k1][k2]['vibration_v_a_min']
    result = {"exausters": []}
    i = 0
    for k, v in js.items():
        # print(k)
        # i = int(k[2:])
        timestampStr = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
        result['exausters'].append({"id": i, "bearings": [], "work": 0, "time": timestampStr})
        for k1, v1 in v.items():
            # print(k1)
            if k1[0] == 'b':
                # print(result['exausters'][i-1]['bearings'])
                j = int(k1[8:])
                # print(j)
                result['exausters'][i - 1]['bearings'].append({"id": j})

            for k2, v2 in v1.items():
                if k1[0] == 'b' and k2[0] == 'v':
                    result['exausters'][i - 1]['bearings'][j-1]['vibration'] = 'well'
                elif k1[0] == 'b' and k2[0] == 't':
                    result['exausters'][i - 1]['bearings'][j - 1]["temperature"] = 'well'
                print(k2)
                print(v2)
                # pass
        i += 1

    return JSONResponse(content=result)


@app.get("/get-second-screen/{exhauster_id}")
async def second_screen(exhauster_id):
    result = step()
    dictData = json.loads(result)
    dictData = dictData[''.join(('ex', str(exhauster_id)))]
    js = dictData
    for k1, v1 in js.items():
        # print(v1)
        for k2, v2 in v1.items():
            if k2 == 'temperature':
                print('temp')
                print(js[k1][k2])
                js[k1][k2]['flag'] = 'norm'
                if js[k1][k2]['value'] >= js[k1][k2]['temp_w_max'] or js[k1][k2]['value'] <= js[k1][k2][
                    'temp_w_min']:
                    js[k1][k2]['flag'] = 'warning'
                if js[k1][k2]['value'] >= js[k1][k2]['temp_a_max'] or js[k1][k2]['value'] <= js[k1][k2][
                    'temp_a_min']:
                    js[k1][k2]['flag'] = 'alarm'
                del js[k1][k2]['temp_w_max']
                del js[k1][k2]['temp_w_min']
                del js[k1][k2]['temp_a_max']
                del js[k1][k2]['temp_a_min']

            elif k2 == 'vibration_axial':
                print('vibration_axial')
                print(js[k1][k2])
                js[k1][k2]['flag'] = 'norm'
                if js[k1][k2]['value'] >= js[k1][k2]['vibration_a_w_max'] or js[k1][k2]['value'] <= \
                        js[k1][k2][
                            'vibration_a_w_min']:
                    js[k1][k2]['flag'] = 'warning'
                if js[k1][k2]['value'] >= js[k1][k2]['vibration_a_a_max'] or js[k1][k2]['value'] <= \
                        js[k1][k2][
                            'vibration_a_a_min']:
                    js[k1][k2]['flag'] = 'alarm'
                del js[k1][k2]['vibration_a_w_max']
                del js[k1][k2]['vibration_a_w_min']
                del js[k1][k2]['vibration_a_a_max']
                del js[k1][k2]['vibration_a_a_min']
            elif k2 == 'vibration_horizontal':
                print('vibration_horizontal')
                print(js[k1][k2])
                js[k1][k2]['flag'] = 'norm'
                if js[k1][k2]['value'] >= js[k1][k2]['vibration_h_w_max'] or js[k1][k2]['value'] <= \
                        js[k1][k2][
                            'vibration_h_w_min']:
                    js[k1][k2]['flag'] = 'warning'
                if js[k1][k2]['value'] >= js[k1][k2]['vibration_h_a_max'] or js[k1][k2]['value'] <= \
                        js[k1][k2][
                            'vibration_h_a_min']:
                    js[k1][k2]['flag'] = 'alarm'
                del js[k1][k2]['vibration_h_w_max']
                del js[k1][k2]['vibration_h_w_min']
                del js[k1][k2]['vibration_h_a_max']
                del js[k1][k2]['vibration_h_a_min']
            elif k2 == 'vibration_vertical':
                print('vibration_vertical')
                print(js[k1][k2])
                js[k1][k2]['flag'] = 'norm'
                if js[k1][k2]['value'] >= js[k1][k2]['vibration_v_w_max'] or js[k1][k2]['value'] <= \
                        js[k1][k2][
                            'vibration_v_w_min']:
                    js[k1][k2]['flag'] = 'warning'
                if js[k1][k2]['value'] >= js[k1][k2]['vibration_v_a_max'] or js[k1][k2]['value'] <= \
                        js[k1][k2][
                            'vibration_v_a_min']:
                    js[k1][k2]['flag'] = 'alarm'
                del js[k1][k2]['vibration_v_w_max']
                del js[k1][k2]['vibration_v_w_min']
                del js[k1][k2]['vibration_v_a_max']
                del js[k1][k2]['vibration_v_a_min']
    return JSONResponse(content=js)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
