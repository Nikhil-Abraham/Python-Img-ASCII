import PIL.Image


ASCII_CHARS = ['@','#','$','S','%','?','*','|','+',';',':',',','.']

def resizeImage(image, newWidth=100):
  width, height = image.size
  ratio = height / width
  newHeight = int(newWidth * ratio)
  resizeImage = image.resize((newWidth,newHeight))
  return resizeImage

def grayify(image):
  grayscaleImage = image.convert('L')
  return grayscaleImage

def pixelsToASCII(image):
  pixels = image.getdata()
  characters = "".join([ASCII_CHARS[pixels//25] for pixel in pixels])
  return characters

def main(newWidth=100):
  path = input('Enter valid pathname to image:\n')
  try:
    image = PIL.Image.open(path)
  except:
    print(path,'Is not a valid PathName.\n')
  
  newImageData = pixelsToASCII(grayify(resizeImage(image)))

  pixelCount = len(newImageData)
  asciiImage = '\n'.join(newImageData[i:(i+newWidth)] for i in range(0,pixelCount,newWidth))

  print(asciiImage)

  with open('ascii_image.txt','w') as f:
    f.write(asciiImage)

if __name__ == "__main__":
    main()