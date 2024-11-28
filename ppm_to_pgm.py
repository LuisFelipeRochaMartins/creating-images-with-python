def process_ppm_to_grayscale_and_average(input_file, output_gray_file, output_average_file):
    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()] 
        
        if lines[0] != 'P3':
            raise ValueError("O arquivo de entrada não está no formato PPM P3.")
        
        dimensions_index = 1
        while lines[dimensions_index].startswith('#'):  
            dimensions_index += 1

        dimensions = lines[dimensions_index]
        width, height = map(int, dimensions.split())
        max_val = int(lines[dimensions_index + 1])
        
        if max_val != 255:
            raise ValueError("O valor máximo do PPM não é 255.")
        
        pixel_data = ' '.join(lines[dimensions_index + 2:]).split()
        if len(pixel_data) != width * height * 3:
            raise ValueError("Número de valores RGB não corresponde às dimensões especificadas.")
        
        pixels = [int(value) for value in pixel_data]

        rgb_triplets = [pixels[i:i+3] for i in range(0, len(pixels), 3)]

        gray_pixels = [
            int(sum(rgb) / 3) for rgb in rgb_triplets
        ]

        average_pixels = [
            [int(sum(rgb) / 3)] * 3 for rgb in rgb_triplets
        ]

        with open(output_gray_file, 'w') as f:
            f.write("P2\n")
            f.write(f"{width} {height}\n")
            f.write(f"{max_val}\n")
            for i in range(0, len(gray_pixels), width):
                f.write(" ".join(map(str, gray_pixels[i:i + width])) + "\n")

        print(f"Imagem em escala de cinza salva como: {output_gray_file}")

        with open(output_average_file, 'w') as f:
            f.write("P3\n")
            f.write(f"{width} {height}\n")
            f.write(f"{max_val}\n")
            for triplet in average_pixels:
                f.write(" ".join(map(str, triplet)) + "\n")

        print(f"Imagem com média dos valores RGB salva como: {output_average_file}")

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


input_ppm = "Fig4.ppm"
output_p2 = "Fig4_grayscale.pgm"
output_p3 = "Fig4_average.ppm"

process_ppm_to_grayscale_and_average(input_ppm, output_p2, output_p3)
