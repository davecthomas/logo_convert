from PIL import Image, ImageDraw, ImageOps
import os
import glob


def convert_image(input_image, output_image, output_size=(96, 96), border=4):
    # Scale factor for rendering at higher resolution
    scale_factor = 4
    scaled_size = (output_size[0] * scale_factor,
                   output_size[1] * scale_factor)
    inner_diameter = scaled_size[0] - 2 * border * scale_factor

    # Open the input image
    img = Image.open(input_image).convert("RGBA")

    # Resize the image to fit within the inner circle while maintaining aspect ratio
    img.thumbnail((inner_diameter, inner_diameter), Image.Resampling.LANCZOS)

    # Create a circular mask at the higher resolution
    mask = Image.new("L", (inner_diameter, inner_diameter), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, inner_diameter, inner_diameter), fill=255)

    # Calculate the position to paste the image on the mask to center it
    paste_position = (
        (inner_diameter - img.size[0]) // 2,
        (inner_diameter - img.size[1]) // 2
    )

    # Apply the mask to the image
    circular_img = Image.new(
        "RGBA", (inner_diameter, inner_diameter), (255, 255, 255, 0))
    circular_img.paste(img, paste_position, img)
    circular_img = Image.composite(
        circular_img, Image.new("RGBA", circular_img.size), mask)

    # Create a new image with a transparent background to add the border
    final_img = Image.new("RGBA", scaled_size, (255, 255, 255, 0))
    final_img.paste(circular_img, (border * scale_factor,
                    border * scale_factor), circular_img)

    # Draw a white circle to act as the outer border
    draw = ImageDraw.Draw(final_img)
    draw.ellipse((0, 0) + scaled_size, outline="white",
                 width=border * scale_factor)

    # Downscale the final image to the desired size
    final_img = final_img.resize(output_size, Image.Resampling.LANCZOS)

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
