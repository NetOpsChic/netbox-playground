
import config
import pynetbox

# Connect to NetBox
nb = pynetbox.api(config.NETBOX_URL, token=config.API_TOKEN)

def create_site(name, slug):
    site = nb.dcim.sites.create(name=name, slug=slug)
    return site

def create_manufacturer(name, slug):
    manufacturer = nb.dcim.manufacturers.create(name=name, slug=slug)
    return manufacturer

def create_device_type(model, slug, manufacturer_id):
    device_type = nb.dcim.device_types.create(model=model, slug=slug, manufacturer=manufacturer_id)
    return device_type

def create_device_role(name, slug):
    device_role = nb.dcim.device_roles.create(name=name, slug=slug)
    return device_role

def create_device(name, device_type_id, device_role_id, site_id):
    device = nb.dcim.devices.create(
        name=name,
        device_type=device_type_id,
        role=device_role_id,
        site=site_id
    )
    return device

