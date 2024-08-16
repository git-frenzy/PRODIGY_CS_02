# pip install pillow numpy

from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    #open the image
    image = Image.open(input_image_path)
    image_np = np.array(image)
    

    encrypted_image_np = (image_np + key) % 256
    
    #save the image
    encrypted_image = Image.fromarray(encrypted_image_np.astype(np.uint8))
    encrypted_image.save(output_image_path)
    print(f"Encrypted image saved at {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # open encrypted image
    encrypted_image = Image.open(input_image_path)
    encrypted_image_np = np.array(encrypted_image)
    
    # Decrypt the image
    decrypted_image_np = (encrypted_image_np - key) % 256
    
    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_image_np.astype(np.uint8))
    decrypted_image.save(output_image_path)
    print(f"Decrypted image saved at {output_image_path}")

#example
input_image_path = "input_image.jpg"
encrypted_image_path = "encrypted_image.jpg"
decrypted_image_path = "decrypted_image.jpg"
key = 50  # Example key value


encrypt_image(input_image_path, encrypted_image_path, key)


decrypt_image(encrypted_image_path, decrypted_image_path, key)
