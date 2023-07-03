from jinja2 import Template

aaa_server = {
  "aaa": {
    "new-model": [
    ],
    "group": {
      "server": {
        "tacacsplus": [
          {
            "name": "ACS",
            "server": {
              "APAC": [
                {
                  "name": "SIN_ACS"
                },
                {
                  "name": "PERTH_ACS"
                },
                {
                  "name": "HOU_ACS"
                }
              ],
              "EMEA": [
                {
                  "name": "LON_ACS"
                },
                {
                  "name": "HOU_ACS"
                }
              ],
              "US": [
                {
                  "name": "HOU_ACS"
                },
                {
                  "name": "LON_ACS"
                }
              ]
            },
            "timeout": 10
          }
        ],
        "radius": [
          {
            "name": "AAA",
            "server": {
              "name": [
                {
                  "name": "HOU_RadiusVIP"
                },
                {
                  "name": "LON_RadiusVIP"
                },
                {
                  "name": "SIN_RadiusVIP"
                }
              ]
            }
          }
        ]
      }
    },
    "authentication": {
      "enable": {
        "default": {
          "group": "acs",
          "enable": [
          ]
        }
      },
      "login": [
        {
          "name": "default",
          "a1": {
            "group": "acs"
          },
          "a2": {
            "local": [
            ]
          }
        }
      ]
    },
    "authorization": {
      "commands": [
        {
          "level": 0,
          "list-name": "default",
          "group": "acs",
          "if-authenticated": [
            
          ]
        },
        {
          "level": 1,
          "list-name": "default",
          "group": "acs",
          "if-authenticated": [
            
          ]
        },
        {
          "level": 15,
          "list-name": "default",
          "group": "acs",
          "if-authenticated": [
            
          ]
        }
      ],
      "exec": [
        {
          "name": "default",
          "a1": {
            "group": "acs"
          },
          "a2": {
            "if-authenticated": [
              
            ]
          }
        }
      ]
    },
    "accounting": {
      "DEV": {
        "commands": [
          {
            "level": 0,
            "list-name": "default",
            "action-type": "start-stop",
            "group": "acs"
          },
          {
            "level": 1,
            "list-name": "default",
            "action-type": "start-stop",
            "group": "acs"
          },
          {
            "level": 15,
            "list-name": "default",
            "action-type": "start-stop",
            "group": "acs"
          }
        ],
        "connection": [
          {
            "name": "default",
            "start-stop": {
              "group1": {
                "group": "acs"
              }
            }
          }
        ],
        "exec": [
          {
            "name": "default",
            "start-stop": {
              "group1": {
                "group": "tacacs+"
              }
            }
          }
        ],
        "network": [
          {
            "id": "default",
            "start-stop": {
              "group": "tacacs+"
            }
          }
        ],
        "system": {
          "default": {
            "start-stop": {
              "group": "acs"
            }
          }
        },
        "update": {
          "newinfo": {
          }
        }
      },
      "PROD": {
        "commands": [
          {
            "level": 0,
            "list-name": "default",
            "action-type": "start-stop",
            "group": "acs"
          },
          {
            "level": 1,
            "list-name": "default",
            "action-type": "start-stop",
            "group": "acs"
          },
          {
            "level": 15,
            "list-name": "default",
            "action-type": "start-stop",
            "group": "acs"
          }
        ],
        "connection": [
          {
            "name": "default",
            "start-stop": {
              "group": "acs"
            }
          }
        ],
        "exec": [
          {
            "name": "default",
            "start-stop": {
              "group": "tacacs+"
            }
          }
        ],
        "network": [
          {
            "id": "default",
            "start-stop": {
              "group": "tacacs+"
            }
          }
        ],
        "system": {
          "default": {
            "start-stop": {
              "group": "acs"
            }
          }
        }
      }
    },
    "session-id": "common"
  }
}

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
{% endfor %}
{% else %}
No servers found for the specified region.
{% endif %}

"""

aaa_template = """
{% for group in aaa_server["aaa"]["group"]["server"]["tacacsplus"][0]["name"] %}
aaa group server tacacs+ {{ group }}
 server name {{ group.name }}
{% endfor %}

"""

# Create a Jinja template from the tacacs_template string
template_tacacs = Template(tacacs_template)
template_aaa = Template(aaa_template)

# Define the inventory
inventory = {
    "Device Name": "ASAswppal-C9200.asai.chevrontexaco.net",
    "IP Address": "146.39.38.130",
    "Region": "US"
}

# Retrieve the region from the inventory
region = inventory.get("Region")

# Render the template based on the region
rendered_template_tacacs = template_tacacs.render(tacacs=tacacs, region=region)
rendered_template_aaa = template_aaa.render(aaa_server = aaa_server)

# Print the rendered template
print(rendered_template_tacacs)
print(rendered_template_aaa)


