import json

file_path = r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 4\json\sample-data.json"

with open(file_path, encoding="utf-8") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 90)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU'}")
print("-" * 90)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "N/A")
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")
    
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
