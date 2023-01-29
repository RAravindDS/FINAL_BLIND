import gdown, os

os.system("git clone https://github.com/HassanBinHaroon/object_detection-PLUS-distance_estimation-v1.git")
os.chdir("object_detection-PLUS-distance_estimation-v1/object-detector")
os.system("python setup.py")
id = "https://drive.google.com/drive/folders/10jpVGSHGILDt85QGf5KwHji0sUjZXbWR"
gdown.download_folder(id, quiet=True, use_cookies=False)
