from random import randint

def create_photo(): 
  with open("pgm.pgm", "w") as photo:
    write_photo_config(photo)
    photo.write(write_photo_content())

    return photo 


def write_photo_config(photo): 
  photo.write("P2\n")
  photo.write("100 100\n")
  photo.write("15\n")

  return photo


def write_photo_content():
  bytes = ""
  for _ in range(100):
    bytes += " ".join(str(randint(0, 15)) for _ in range(100))
    bytes += "\n"

  return bytes

create_photo()