address = ""
sequence = 0
variable_size_one = 0
variable_size_two = 12
packet_payload = ""
packet_list = []
string_built = ""
import zlib

print("-" * 20)
print("MOCK PACKETS TRANSFER")
print("-" * 20)


message = input("ENTER MESSAGE TO TRANSFER: ")

def trailer(payload_built):
    payload_built = payload_built.encode("utf-8")
    return zlib.crc32(payload_built)

def header(address, x):
    address = "10.0.0.5"
    return f"to={address} seq={x + 1}"

def payload(variable_size_one, variable_size_two, packet_payload):
    packet_payload = message[variable_size_one:variable_size_two]
    variable_size_one = variable_size_two
    variable_size_two += 12
    return packet_payload, variable_size_one, variable_size_two

