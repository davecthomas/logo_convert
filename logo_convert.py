from PIL import Image, ImageDraw, ImageOps
import os
import glob


def convert_image(input_image, output_image, output_size=(96, 96), border=4):
    # Calculate the maximum diameter available for the image inside the circle
    max_diameter = output_size[0] - 2 * border

    # Open the input image
    img = Image.open(input_image).convert("RGBA")

    # Calculate the larger dimension (width or height)
    img_w, img_h = img.size
    larger_dimension = max(img_w, img_h)

    # Scale the image so that the larger dimension is 8 pixels narrower than the max diameter
    scale = (max_diameter - 8) / larger_dimension

    # Resize the image proportionally
    new_size = (int(img_w * scale), int(img_h * scale))
    img = img.resize(new_size, Image.Resampling.LANCZOS)

    # Create a final image with a transparent background
    final_img = Image.new("RGBA", output_size,
                          (255, 255, 255, 0))  # Transparent

    # Calculate position to paste the resized image on the final image
    paste_position = ((output_size[0] - new_size[0]) //
                      2, (output_size[1] - new_size[1]) // 2)
    final_img.paste(img, paste_position, img)

    # Create a circular mask at the output size
    mask = Image.new("L", output_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(
        (border, border, output_size[0] - border, output_size[1] - border), fill=255)

    # Apply the circular mask to the final image
    final_img.putalpha(mask)

    # Draw a white border around the circle
    draw = ImageDraw.Draw(final_img)
    draw.ellipse((border, border, output_size[0] - border,
                 output_size[1] - border), outline="white", width=border)

    # Save the final image
    img_format = output_image.split('.')[-1].upper()
    final_img.save(output_image, format=img_format)


def process_images_in_directory():
    # Get a list of all .png and .jpg files in the current directory
    image_files = glob.glob("*.png") + glob.glob("*.jpg")

    # Process each image
    for input_image in image_files:
        # Create the output filename by adding "_circular" before the file extension
        base, ext = os.path.splitext(input_image)
        output_image = f"{base}_circular{ext}"

        # Convert the image
        convert_image(input_image, output_image)
        print(f"Image converted and saved to {output_image}")


# Run the processing function
process_images_in_directory()
