
from helpers import *

# Example usage:
if __name__ == "__main__":
    site = create_site("Data Center", "data-center")
    print("Created site:", site)

    manufacturer = create_manufacturer("Cisco", "cisco")
    print("Created manufacturer:", manufacturer)
    
    device_type = create_device_type("Cisco XXX", "cisco-xxx", manufacturer['id'])
    print("Created device type:", device_type)
    
    device_role = create_device_role("Switch", "switch")
    print("Created device role:", device_role)
    
    device = create_device("Switch-1", device_type['id'], device_role['id'], site['id'])
    print("Created device:", device)
