def read_pgm(filename):
    with open(filename, 'r') as file:
        assert file.readline().strip() == 'P2', "Arquivo PGM inválido!"
        
        line = file.readline().strip()
        while line.startswith('#'):
            line = file.readline().strip()
        
        if 'x' in line:
            width, height = map(int, line.split('x'))
        else:
            width, height = map(int, line.split())
        
        max_gray = int(file.readline().strip())
        
        pixels = []
        for line in file:
            pixels.extend(map(int, line.split()))
        
        image = [pixels[i * width:(i + 1) * width] for i in range(height)]
        return image, width, height, max_gray
    
def write_pgm(file_path, image, max_gray):
  height = len(image)
  width = len(image[0])

  with open(file_path, 'w') as file:
      file.write("P2\n")
      file.write(f"{width} {height}\n")
      file.write(f"{max_gray}\n")
      for row in image:
          file.write(' '.join(map(str, row)) + '\n')

def resize_image(image, old_width, old_height, new_width, new_height):
    resized_image = []
    x_ratio = old_width / new_width
    y_ratio = old_height / new_height

    for new_y in range(new_height):
        row = []
        for new_x in range(new_width):
            # Mapeamento do novo pixel para o pixel original mais próximo
            old_x = int(new_x * x_ratio)
            old_y = int(new_y * y_ratio)
            row.append(image[old_y][old_x])
        resized_image.append(row)

    return resized_image

input_file = "resize/reference.pgm"
output_files = [
    ("output_10x_smaller.pgm", 48, 32),
    ("output_480x320.pgm", 480, 320),
    ("output_720p.pgm", 1280, 720),
    ("output_1080p.pgm", 1920, 1080),
    ("output_4k.pgm", 3840, 2160),
    ("output_8k.pgm", 7680, 4320),
]

image, width, height, max_gray = read_pgm(input_file)

for output_file, new_width, new_height in output_files:
    resized_image = resize_image(image, width, height, new_width, new_height)
    write_pgm(output_file, resized_image, max_gray)

print("Redimensionamento concluído!")