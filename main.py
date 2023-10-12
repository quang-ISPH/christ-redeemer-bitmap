from PIL import Image


def image_to_pixel_list(image_path, output_file):
    try:
        image = Image.open(image_path)
        width, height = image.size
        pixel_list = []

        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                r, g, b = pixel
                color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
                pixel_list.append([x, y, color_hex])

        with open(output_file, 'w') as file:
            for pixel in pixel_list:
                file.write(f"[{pixel[0]},{pixel[1]},'{pixel[2]}'],")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


image_path = "brazil.png"
output_file = "pixel_list.txt"
image_to_pixel_list(image_path, output_file)
