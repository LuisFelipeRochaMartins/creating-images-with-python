def gain_image(filename: str, intensity: float = 1.2):
  with open(filename, 'r') as image:
    data = image.readlines()[3:]

  with open('result.pgm', 'w') as photo:
     create_file_headers(photo)
     file_content(photo, data, intensity)

def create_file_headers(photo):  
    photo.write('P2\n800 800\n256\n') 

def file_content(photo, data, intensity): 
    bits = [gain_scale(line, intensity) for line in data if line.strip()]
    for b in bits:
        photo.write(str(b) + "\n") 

def gain_scale(data, intensity): 
    value = int(int(data.strip()) * intensity)
    if (value > 255): 
       return 255
    return value

gain_image('resize/reference.pgm')