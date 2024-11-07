import cv2
import numpy as np
import os

def get_user_input():
    while True:
        # Get user input for the image file path
        image_path = input("Enter the path to your image: ")

        # Check if the file exists
        if not os.path.isfile(image_path):
            print("File does not exist. Please try again.")
            continue

        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print("Could not open or find the image. Please try again.")
        else:
            break

    return image

def resize_image(image):
    width = int(input("Enter the width to resize: "))
    height = int(input("Enter the height to resize: "))
    resized_image = cv2.resize(image, (width, height))
    return resized_image

def rotate_image(image):
    angle = float(input("Enter the angle to rotate (in degrees): "))
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

def translate_image(image):
    tx = int(input("Enter the number of pixels to shift right: "))
    ty = int(input("Enter the number of pixels to shift down: "))
    (h, w) = image.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, M, (w, h))
    return translated_image

def normalize_image(image):
    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    return normalized_image

def edge_detection(image):
    lower_threshold = int(input("Enter the lower threshold for Canny edge detection: "))
    upper_threshold = int(input("Enter the upper threshold for Canny edge detection: "))
    edges = cv2.Canny(image, lower_threshold, upper_threshold)
    return edges

def blur_image(image):
    kernel_size = int(input("Enter the size of the Gaussian kernel (odd number): "))
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blurred_image

def morphological_operations(image):
    kernel_size = int(input("Enter the size of the kernel (odd number): "))
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    morphed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return morphed_image

def main():
    # Get the user input
    image = get_user_input()

    while True:
        print("\nChoose an operation:")
        print("1. Resize")
        print("2. Rotate")
        print("3. Translate")
        print("4. Normalize")
        print("5. Edge Detection")
        print("6. Blur")
        print("7. Morphological Operations")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            result = resize_image(image)
            cv2.imshow('Resized Image', result)
        elif choice == '2':
            result = rotate_image(image)
            cv2.imshow('Rotated Image', result)
        elif choice == '3':
            result = translate_image(image)
            cv2.imshow('Translated Image', result)
        elif choice == '4':
            result = normalize_image(image)
            cv2.imshow('Normalized Image', result)
        elif choice == '5':
            result = edge_detection(image)
            cv2.imshow('Edge Detection', result)
        elif choice == '6':
            result = blur_image(image)
            cv2.imshow('Blurred Image', result)
        elif choice == '7':
            result = morphological_operations(image)
            cv2.imshow('Morphological Operation', result)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
