def gray_scale():
    with open('resize/reference.pgm', 'r') as image:
        data = image.readlines()[1:]
        
    with open('result.pgm', 'w') as photo:
        create_file_headers(photo)
        file_content(photo, data)

def create_file_headers(photo): 
    photo.write('P2\n800 800\n32\n') 

def file_content(photo, data): 
    bits = list(map(convert_scale, data))
    for b in bits:
        photo.write(str(b) + "\n")

def convert_scale(data): 
    return int(int(data.strip()) / 8)

gray_scale()
