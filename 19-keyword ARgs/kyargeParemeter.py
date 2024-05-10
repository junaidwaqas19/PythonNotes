def describe_fish(fish_name,**kwargs):
        color =kwargs.get("color","unkonw color")
        habitat = kwargs.get("habitat","unkonw habitat")
        fins = kwargs.get("fins",0)
        description = f"A {fish_name} is an {color} fish that inhabits {habitat}."\
                      f"It has {fins} fins"
        return description

result = describe_fish("gold_fish",color="orange",habitat="aquriam",fins=3)
print(result)