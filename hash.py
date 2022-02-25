from PIL import Image
import numpy as np

def GetImageHash(image):
    resized = image.resize((8,8))
    gray = resized.convert("L")
    arr = np.array(gray)
    treshold = np.mean(arr)
    hash = [1 if i >= treshold else 0 for i in arr.flatten()]
    return hash

def GetDifferenceCoef(image1, image2):
    hash1 = GetImageHash(image1)
    hash2 = GetImageHash(image2)
    return np.count_nonzero(hash1!=hash2)/len(hash1)

def main():
    directory_name = input("Введите название папки: ")
    image1 = Image.open(f'{directory_name}\\{int(input("Введите номер первой картинки: "))}.png')
    image2 = Image.open(f'{directory_name}\\{int(input("Введите номер второй картинки: "))}.png')
    sim = GetDifferenceCoef(image1,image2)
    print(sim)

if __name__ == "__main__":
    main()
