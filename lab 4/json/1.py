import json

with open("c:/Study/pp2/lab_4/json/sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 90)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU'}")
print("-" * 90)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn")
    description = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")
    
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
