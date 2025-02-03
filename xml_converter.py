import xml.etree.ElementTree as ET

def convert_xml(input_xml):
    root = ET.fromstring(input_xml)
    booking = root.find(".//Booking")

    transfers = ET.Element("transfers", MessageType="Request", FechaCreacion=booking.find("Booking_date").text, Count="1")
    transfer = ET.SubElement(transfers, "transfer")

    ET.SubElement(transfer, "result")
    ET.SubElement(transfer, "client").text = "HER"
    ET.SubElement(transfer, "ttoo").text = booking.find("Company").text
    ET.SubElement(transfer, "flightNumber").text = booking.find("ArrivalFlightNumber").text
    ET.SubElement(transfer, "flightDate").text = booking.find("ArrivalDate").text
    ET.SubElement(transfer, "paxName").text = booking.find("Customer_name").text
    ET.SubElement(transfer, "pickupDate").text = booking.find("DepartureDate").text

    return ET.tostring(transfers, encoding="unicode")

# Δοκιμή
if __name__ == "__main__":
    sample_xml = """<A2BBkConfirmation>
    <Booking ref="H1916939">
    <Booking_date>29/01/2025</Booking_date>
    <Company>RH</Company>
    <Customer_name>Mrs Claire Wood</Customer_name>
    <ArrivalFlightNumber>EZY8215</ArrivalFlightNumber>
    <ArrivalDate>02/05/2025</ArrivalDate>
    <DepartureDate>08/05/2025</DepartureDate>
    </Booking>
    </A2BBkConfirmation>"""

    converted = convert_xml(sample_xml)
    print(converted)
