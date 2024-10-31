from random import randint

def create_rgb_photo(intensity: int = 15, scale: int = 1): 
  with open(f"ppm_{intensity}.ppm", "w") as photo:
    photo_header(photo, intensity)
    photo.write(photo_content(intensity, scale))

def photo_header(photo, intensity):
    photo.write(f"P3\n100 100\n {intensity}\n")


def photo_content(intensity, scale) -> str: 
  bytes = ""
  for _ in range(100):
    bytes += " ".join(str(randint(0,intensity)) for _ in range(100 * 3 * scale))

  return bytes

create_rgb_photo(255, 10)