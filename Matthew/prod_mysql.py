from kafka import KafkaProducer;
from csv import DictReader;
import json;
import time
import io;
from avro.io import DatumWriter, BinaryEncoder
import avro.schema

schemaID = 100003;

data = json.load(open('cred.json'))
bootstrap_servers = data['bootstrap_servers'];
sasl_plain_username = data['Api key'];
sasl_plain_password = data['Api secret'];

schema = avro.schema.parse(open("./schema.avsc").read())
writer = DatumWriter(schema)


def encode(value):
    bytes_writer = io.BytesIO()
    encoder = BinaryEncoder(bytes_writer)
    writer.write(value, encoder)
    return schemaID.to_bytes(5, 'big') + bytes_writer.getvalue()


with open('gps.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        print(row)
value = {row, 'modified': int(1000 * time.time())};
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, security_protocol='SASL_SSL', sasl_mechanism='PLAIN', \
                         sasl_plain_username=sasl_plain_username, sasl_plain_password=sasl_plain_password,
                         value_serializer=lambda m: encode(m))
producer.send('ToMySQL', value);
producer.close();
