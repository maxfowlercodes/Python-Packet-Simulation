address = ""
sequence = 0
variable_size_one = 0
variable_size_two = 12
packet_payload = ""
packet_list = []
string_built = ""
sequence_saved = []
packet_amounts = 0
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

def send_packet(header_built, payload_built, trailer_built):
    return (f"[{header_built}], {payload_built}, [{trailer_built}]")

def reconstruction(packet, string_built):
    if packet[4:12] == "10.0.0.5":
        seq = packet[17:18]
        if string_built[32:33] == " ":
            string_built = string_built + packet[21:33]
        else:
            string_built = string_built + packet[21:34]
        return string_built


for x in range(round(len(message)/12) + 1):
    header_built = header(address, x)
    payload_built, variable_size_one, variable_size_two = payload(variable_size_one, variable_size_two, packet_payload)
    trailer_built = trailer(payload_built)
    packet = send_packet(header_built, payload_built, trailer_built)
    packet_list.append(packet)
    packet_amounts = packet_amounts + 1
    print(packet)
    sequence_saved.append(packet[17:18])
    string_built = reconstruction(packet, string_built)


string_built = string_built.replace(",", "")
length_payload = (len(payload_built) - 1)
length_payload = 11 - length_payload
string_built = string_built[:-length_payload]

if packet_amounts != len(sequence_saved):
        print(f"Missing {packet_amounts - sequence_saved} packets")


print("-" * 20)
print("MESSAGE DECODED")
print("-" * 20)
print(string_built)