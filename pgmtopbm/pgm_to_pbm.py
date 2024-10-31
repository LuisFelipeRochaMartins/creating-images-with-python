def to_binary(filename: str, inverted: bool = False):
  with open(filename, 'r') as image:
    data = image.readlines()[3:]

  with open('result2.pbm', 'w') as photo:
     create_file_headers(photo)
     file_content(photo, data, inverted)

def create_file_headers(photo):  
    photo.write('P1\n800 800\n') 

def file_content(photo, data, inverted): 
    bits = [to_bin(line, inverted) for line in data if line.strip()]
    for b in bits:
        photo.write(str(b) + "\n") 

def to_bin(data, inverted): 
  if inverted: 
     if int(data) > 128: 
        return 0 
     return 1
  if int(data) <= 128:
     return 0
  return 1

to_binary('resize/reference.pgm', False)