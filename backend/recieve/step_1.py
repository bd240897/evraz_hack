from kafka import KafkaConsumer
from json import loads, dumps
import re
from backend.recieve.data import datafile_temp, datafile_vibr, datafile_othr

## credentials
host = 'rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091'
topic = 'zsmk-9433-dev-01'
username = '9433_reader'
password = 'eUIpgWu0PWTJaTrjhjQD3.hoyhntiK'

SASL_SSL = "SASL_SSL"
SASL_MECHANISM = "SCRAM-SHA-512"


# credentials

# functions
def update_json_temp(database, category, value, data, message):
    for k in range(len(database)):
        j = 0
        q = 1
        for i in (database[k]):
            index = str(database[k][j][1:-1])
            regexdata = re.search((r'' + (index) + r'\]\": \d+.\d+'), message)
            regexdata2 = re.search(r' \d+.\d+', regexdata[0])
            data["ex" + str(k + 1)]["bearing_" + str(q)][category][value] = regexdata2[0]
            q += 1
            j += 1
            if j == 9: break
    return data


def update_json_vibr(database, category, value, data, message):
    for k in range(len(database)):
        j = 0
        q = 1
        q_list = [1, 2, 7, 8]
        for i in ((database[k])):
            index = str(database[k][j][1:-1])
            regexdata = re.search((r'' + (index) + r'\]\": \d+.\d+'), message)
            regexdata2 = re.search(r' \d+.\d+', regexdata[0])
            data["ex" + str(k + 1)]["bearing_" + str(q_list[j])][category][value] = regexdata2[0]

            q += 1
            j += 1
            if j == 9: break
    return data


def update_json_othr(database, category, value, data, message):
    for k in range(len(database)):
        j = 0
        q = 1
        for i in (database[k]):
            index = str(database[k][j][1:-1])
            regexdata = re.search((r'' + (index) + r'\]\": -?\d+\.\d+'), message)
            # print(index, regexdata)
            regexdata2 = re.search(r' -?\d+\.\d+', regexdata[0])
            data["ex" + str(k + 1)][category][value] = regexdata2[0]

            q += 1
            j += 1
            if j == 9: break
    return data


# functions

# kafka consumer

consumer = KafkaConsumer(topic, bootstrap_servers=host,
                         security_protocol=SASL_SSL,
                         ssl_cafile='backend/recieve/CA.pem',
                         group_id='win_plus_ners',
                         sasl_mechanism=SASL_MECHANISM,
                         sasl_plain_username=username,
                         sasl_plain_password=password,
                         value_deserializer=lambda x: loads(x.decode('utf-8')),
                         auto_offset_reset='earliest',
                         )

# kafka consumer

# https://stackoverflow.com/questions/57290708/setting-python-kafkaproducer-sasl-mechanism-property
# https://pythonpip.ru/osnovy/ispolzovanie-apache-kafka-na-python-primery

empty_json = open("backend/recieve/empty.json", "r")
empty_json = empty_json.read()

data = loads(empty_json)


# main function

def main():
    for message in consumer:
        message = message.value
        m_d = (dumps(message, indent=4))
        # print(dumps(message, indent=4))
        # result = re.search(r'\[0:27\]\s\d+\.\d+',m_d)
        for z in datafile_temp:
            update_json_temp(z[0], z[1], z[2], data, m_d)

        for z in datafile_vibr:
            update_json_vibr(z[0], z[1], z[2], data, m_d)

        for z in datafile_othr:
            update_json_othr(z[0], z[1], z[2], data, m_d)

        return dumps(data)


main()
