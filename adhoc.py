from jinja2 import Template

tacacs = {
    "tacacs": {
        "server": {
            "APAC": [
                {
                    "name": "SIN_ACS",
                    "address": {
                        "ipv4": "139.65.139.143"
                    },
                    "timeout": 10,
                    "key": {
                        "encryption": "7",
                        "key": "06031D344F4B1A1606041B08"
                    }
                },
                {
                    "name": "PERTH_ACS",
                    "address": {
                        "ipv4": "146.45.1.85"
                    },
                    "timeout": 10,
                    "key": {
                        "encryption": "7",
                        "key": "06031D344F4B1A1606041B08"
                    }
                },
                {
                    "name": "HOU_ACS",
                    "address": {
                        "ipv4": "139.65.136.58"
                    },
                    "timeout": 10,
                    "key": {
                        "encryption": "7",
                        "key": "06031D344F4B1A1606041B08"
                    }
                }
            ],
            "US": [
                {
                    "name": "HOU_ACS",
                    "address": {
                        "ipv4": "139.65.136.58"
                    },
                    "timeout": 10,
                    "key": {
                        "encryption": "7",
                        "key": "06031D344F4B1A1606041B08"
                    }
                },
                {
                    "name": "LON_ACS",
                    "address": {
                        "ipv4": "139.65.138.26"
                    },
                    "timeout": 10,
                    "key": {
                        "encryption": "7",
                        "key": "06031D344F4B1A1606041B08"
                    }
                }
            ],
            "EMEA": [
                {
                    "name": "LON_ACS",
                    "address": {
                        "ipv4": "139.65.138.26"
                    },
                    "timeout": 10,
                    "key": {
                        "encryption": "7",
                        "key": "06031D344F4B1A1606041B08"
                    }
                },
                {
                    "name": "HOU_ACS",
                    "address": {
                        "ipv4": "139.65.136.58"
                    },
                    "timeout": 10,
                    "key": {
                        "encryption": "7",
                        "key": "06031D344F4B1A1606041B08"
                    }
                }
            ]
        }
    }
}

tacacs_template = """
{% if region == "US" %}
{% for server in tacacs["tacacs"]["server"]["US"] %}
tacacs server {{ server.name }}
 address ipv4 {{ server.address.ipv4 }} 
 key <Shared Secret>
 timeout 10
!
aaa group server tacacs+ TACACS_GROUP
 server name {{ server.name }}
{% endfor %}
{% else %}
No servers found for the specified region.
{% endif %}
"""

# Create a Jinja template from the tacacs_template string
template = Template(tacacs_template)

# Define the inventory
inventory = {
    "Device Name": "ASAswppal-C9200.asai.chevrontexaco.net",
    "IP Address": "146.39.38.130",
    "Region": "US"
}

# Retrieve the region from the inventory
region = inventory.get("Region")

# Render the template based on the region
rendered_template = template.render(tacacs=tacacs, region=region)

# Print the rendered template
print(rendered_template)
