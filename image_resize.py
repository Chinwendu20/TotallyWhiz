from PIL import Image
import os
file_path=r'C:\Users\Dumebi\Downloads\Tiff_file'
directory = os.listdir(file_path)
for file in directory:
	if not file.startswith('.'):
		rel_path=os.path.join(file_path,file)
		im=Image.open(rel_path)
		new_image=im.resize((128,128)).rotate(90).convert('RGB').save(r'C:\Users\Dumebi\Pictures\{}.jpeg'.format(file))
		im.close()