from random import randint

def create_photo(): 
  with open("pbm.pbm", "w") as photo: 
    write_photo_config(photo)
    photo.write(write_photo_content())

    return photo

def write_photo_config(photo):
  photo.write("P1\n100 100\n")


def write_photo_content() :
  bytes = ""
  for _ in range(10): 
    bits = " ".join(" ".join(str(randint(0,1)) * 10 for _ in range(10)))
    for _ in range(10):
        bytes += bits + "\n"

  return bytes

create_photo()
print(randint(0, 1))