import yaml

with open("steps/meber_invite.yml") as f:
    print(yaml.safe_load(f))
a = 123
print(f"{a}")
