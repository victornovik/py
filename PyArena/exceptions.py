def image_info(images: dict):
    if "title" not in images or "id" not in images:
        raise ValueError("Key does not exist")


def route_info(d: dict):
    if "distance" in d and isinstance(d["distance"], int):
        return f"Distance is {d["distance"]}"
    elif "speed" in d and "time" in d:
        return f"Distance is {d["speed"] * d["time"]}"
    else:
        return f"No distance is available"


try:
    raise ValueError("Invalid value")
except Exception as e:
    print("Exception is caught\n\t" + str(e))
else:
    print("All OK")
finally:
    print("Finally")
