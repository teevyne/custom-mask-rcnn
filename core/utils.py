from PIL import Image
import io

def process_image(original_image):
    # Your machine learning/image processing logic here
    # Example: Resize the image
    img = Image.open(original_image)
    img_resized = img.resize((300, 300))
    
    # Save the processed image
    processed_image_path = 'processed/' + original_image.name
    img_resized.save(processed_image_path)
    
    return processed_image_path