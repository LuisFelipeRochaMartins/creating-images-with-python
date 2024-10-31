from random import randint

def create_rgb_photo(intensity: int = 15): 
  with open(f"ppm_{intensity}.ppm", "w") as photo:
    photo_header(photo, intensity)
    photo.write(photo_content(intensity))

def photo_header(photo, intensity):
    photo.write(f"P3\n100 100\n {intensity}\n")


<<<<<<< HEAD
def photo_content(intensity, scale) -> str: 
=======
def photo_content(intensity): 
>>>>>>> parent of 73a1d5c (created an option to be able to scale the image)
  bytes = ""
  for _ in range(100):
    bytes += " ".join(str(randint(0,intensity)) for _ in range(100 * 3))

  return bytes

create_rgb_photo()