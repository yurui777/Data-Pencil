import os
import shutil
src_img='./image_1'
src_xml='./xml_1'
tar_img='./image_2'
tar_xml='./xml_2'
for file in os.listdir(src_xml):
    print(file)
    a=file[:5]
    if a>'01000':
        shutil.copy(os.path.join(src_xml,file), os.path.join(tar_img,file))
        os.unlink(os.path.join(src_xml,file))

