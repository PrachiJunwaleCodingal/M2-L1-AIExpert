#ACP-image resizer

import cv2
def main():
    img = 'img.jpg' 
    image = cv2.imread(img)

    sizes = {
        'small': (200, 200),
        'medium': (400, 400),
        'large': (600, 600)
    }

    for n, dim in sizes.items():
        res = cv2.resize(image, dim)
        cv2.imshow(f"{n.capitalize()} Image", res)
        cv2.imwrite(f"input_image_{n}.jpg", res)
        print(f"Image res to {dim[0]}x{dim[1]} px({n})")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

