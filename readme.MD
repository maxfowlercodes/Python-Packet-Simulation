# Packet Transfer Example

This is a mockup of how packets transfer data across the internet, you enter some text and it will "send" it too the IP adress set.

Packet Header: **'[to=10.0.0.5 seq=1]'**

Packet Payload: **',message to t,'**

Packet trailer: **'[2523470218]'**

Resulting in the full Packet looking as such:
> [to=10.0.0.5 seq=1], message to t, [2523470218]


This style of packet mocks if it could be broken into 12 characters or 3 bits of data in each packet. 
The sequence of each packet is checked, simulating if a packet was missed they would hopefully be rerouted in the correct order or skipped. If this was a real server, a new request could then be made for that specific packet. 



Please note that none of this is real, and there is no additonal imports needed for running this python script.