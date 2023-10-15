import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim


def to_grey(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def compare_mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def write_to_file(file_name, data):
    try:
        if not os.path.isfile(file_name):
            with open(file_name, 'w') as file:
                file.write(data + '\n')
        else:
            with open(file_name, 'a') as file:
                file.write(data + '\n')
        print("Data written to the file successfully.")
    except IOError:
        print("An error occurred while writing to the file.")

def calculate_average(file_name):
    total_column1 = 0.0
    total_column2 = 0.0
    count = 0

    with open(file_name, 'r') as file:
        for line in file:
            values = line.split()
            column1 = float(values[0])
            column2 = float(values[1])

            total_column1 += column1
            total_column2 += column2
            count += 1

    average_column1 = total_column1 / count
    average_column2 = total_column2 / count

    print("Average column 1:", average_column1)
    print("Average column 2:", average_column2)


def compute_avarage(sr , hr, filename, mode):
    sr_dir = os.listdir(sr)
    hr_dir = os.listdir(hr)
    psnr = 0.0
    ssim = 0.0
    mse = 0.0
    n = 0
    for hr_image in hr_dir:
        for sr_image in sr_dir:
            if sr_image == hr_image:
                if (sr_image[-3:]) != 'jpg':
                    continue

                imageA = cv2.imread(str(sr) + sr_image)
                imageB = cv2.imread(str(hr) + hr_image)

                compute_ssim = compare_ssim(to_grey(imageA), to_grey(imageB))
                compute_psnr = cv2.PSNR(imageA, imageB)
                compute_mse = compare_mse(to_grey(imageA),to_grey(imageB))

                psnr += compute_psnr
                ssim += compute_ssim
                mse += compute_mse
                n += 1
                if n%100 == 0:
                    print("finish compute avarage [%d/%d]" % (n, len(hr_dir)))
    if n == 0:
        print("Cannot find images")
    else:
        psnr = psnr / n
        ssim = ssim / n
        # mse = mse / n
        print("Average psnr = ", psnr)
        print("Average ssim = ", ssim)
        # print("average mse = ", mse)

    result = str(psnr) + ' ' + str(ssim)

    if mode == True:
        write_to_file(filename, result)
