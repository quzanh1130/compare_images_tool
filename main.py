
import rename as re
import separate_folder as sp
import compare_image as cp
import queue

# source address
sr = r"D:\Jobs\ResearchPaper\Dataset\result\Q1\gt/"
# sr = "D:\data/catalog_1.catalog"

# detination address
hr = r"D:\Jobs\ResearchPaper\Dataset\result\Q1\result/"

# file name to save the result of psnr and ssim
filename = 'D:\Jobs\ResearchPaper\Dataset/result\Q1\data/result.txt'
# false to not save and true to save
mode = False

if __name__ == '__main__':
    # sp.separate_folder(sr,hr);
    # sp.separate_text(sr,filename)
    # re.rename(sr,1)
    # re.rename(hr,1)
    cp.compute_avarage(sr,hr,filename,mode)
    # cp.calculate_average(filename)

