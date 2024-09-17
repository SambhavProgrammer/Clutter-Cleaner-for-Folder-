import glob
import os 


file = os.listdir("C:\\Users\\it\\OneDrive\\Documents\\Python Projects\\Clutter Cleaner\\cpng")

def jpg():

    jpg_files = glob.glob("C:\\Users\\it\\OneDrive\\Documents\\Python Projects\\Clutter Cleaner\\cpng\\*.jpg")


    for index, file_path in enumerate(jpg_files):
        new_name = f"C:\\Users\\it\\OneDrive\\Documents\\Python Projects\\Clutter Cleaner\\cpng\\{index + 1}.jpg"
        os.rename(file_path, new_name)

    if (not os.path.exists(new_name)):
        os.rename(file_path, new_name)
    else:
        pass
jpg()

def png():
    png_files2 = glob.glob("C:\\Users\\it\\OneDrive\\Documents\\Python Projects\\Clutter Cleaner\\cpng\\*.png")
    
    for index2, file_path2 in enumerate(png_files2):
        new_name2 = f"C:\\Users\\it\\OneDrive\\Documents\\Python Projects\\Clutter Cleaner\\cpng\\{index2 + 1}.png"
        
        os.rename(file_path2, new_name2)

        if (not os.path.exists(new_name2)):
            os.rename(file_path2, new_name2)
        else:
            pass
png()   

def pdf():
    pdf_files2 = glob.glob("C:\\Users\\it\\OneDrive\\Documents\\Python Projects\\Clutter Cleaner\\cpng\\*.pdf")
    
    for index3, file_path3 in enumerate(pdf_files2):
        new_name3 = f"C:\\Users\\it\\OneDrive\\Documents\\Python Projects\\Clutter Cleaner\\cpng\\{index3 + 1}.png"
        
        os.rename(file_path3, new_name3)
pdf()