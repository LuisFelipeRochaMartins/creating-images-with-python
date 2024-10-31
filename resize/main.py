def load_pgm_image(filename):
    with open(filename, 'r') as f:
        header = f.readline().strip() 
        if header != 'P2':
            raise ValueError("File is not in PGM P2 format")
        
        dimensions_line = f.readline().strip()
        while dimensions_line.startswith("#"):
            dimensions_line = f.readline().strip()

        width, height = map(int, dimensions_line.split())
        max_gray_value = int(f.readline().strip())  

        pixels = []
        for y in range(height):
            row = []
            for x in range(width):
                intensity = int(f.readline().strip())
                row.append(intensity)
            pixels.append(row)

    return pixels, width, height

def save_pgm_image(image, filename):
    height = len(image)
    width = len(image[0])
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")  

        for row in image:
            for intensity in row:
                f.write(f"{intensity}\n")

def bicubic_interpolation(x, y, image):
    nearest_x = int(round(x))
    nearest_y = int(round(y))

    nearest_x = max(0, min(nearest_x, len(image[0]) - 1))
    nearest_y = max(0, min(nearest_y, len(image) - 1))
    
    return image[nearest_y][nearest_x] 

def resize_image_bicubic(image, new_width, new_height):
    original_height = len(image)
    original_width = len(image[0])
    
    new_image = [[0 for _ in range(new_width)] for _ in range(new_height)]
    
    x_scale = original_width / new_width
    y_scale = original_height / new_height
    
    for y in range(new_height):
        for x in range(new_width):
            original_x = x * x_scale
            original_y = y * y_scale
            
            new_image[y][x] = int(bicubic_interpolation(original_x, original_y, image))
    
    return new_image

def main(input_file):
    original_image, original_width, original_height = load_pgm_image(input_file)

    sizes = {
        '10x_smaller': (original_width // 10, original_height // 10),
        '480x320': (480, 320),
        '720p': (1280, 720),
        '1080p': (1920, 1080),
        '4k': (3840, 2160)
    }

    for label, (new_width, new_height) in sizes.items():
        resized_image = resize_image_bicubic(original_image, new_width, new_height)
        output_file = f"resized_image_{label}.pgm"
        save_pgm_image(resized_image, output_file)
        print(f"Image resized and saved as '{output_file}'")

if __name__ == "__main__":
    main('reference.pgm')
