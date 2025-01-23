# pip install rembg 
# pip install onnxruntime

from rembg import remove  
from PIL import Image

input_path = './imagens/image.png'
output_path = './imagens/teste1_sem_fundo.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)