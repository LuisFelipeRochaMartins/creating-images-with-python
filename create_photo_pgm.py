from random import randint

def create_photo(): 
  with open("pgm.pgm", "w") as photo:
    write_photo_config(photo)
    photo.write(write_photo_content())


def write_photo_config(photo): 
  photo.write("P2\n100 100\n15\n")


def write_photo_content() -> str:
  bytes = ""
  for _ in range(100):
    bytes += " ".join(str(randint(0, 15)) for _ in range(100))
    bytes += "\n"

  return bytes

create_photo()