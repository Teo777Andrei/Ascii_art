#image conversion to .txt file
#steps:
#->1: resize image
#->2: convert image color shades into grey shades only
#->3: create text file using ascii characters suitable for each shade of grey

#import python image processing library
from PIL import Image

#source image
pic_name = "Kratos.jpg"

#open image
image = Image.open(pic_name)

#unpack size of image in width , length variables (pixels)
width , height = image.size

#ratio helpers
addition_width = 1
addition_height = 1


if width > height:
    addition_width = 2
else:
    addition_height = 0.5

#initialise ratio for scaling a new image
ratio=0.3

#resize source image
image=image.resize((int(width*ratio*addition_width),int(height*ratio*addition_height)),Image.NEAREST)
new_width,new_height=image.size



#load each pixel at position (width , lentgth ) into an iterable
pixels = image.load()

#initialise the output text file
out = open("output.txt","w")


#initialise an iterable which will contain the shades of grey represented by integers
grey_shades = []



#character array -> contains characters that will fill the output text file
asc_char="@%#*+=-:. "



#iterate through all pixels by using  two 'for' statements
for h in range(new_height):
    for w in range(new_width):
        #load the R , G ,B integer values that pixel at position (w, h) has into a tuple
        r, g, b = pixels[w, h]
        #define the shade of grey by dividing the sum of R , G , B values  by 3
        grey = (r + g + b) // 3
        #loading into pixels iterable  the shade of grey,
        #(turning into a shade of grey the color of pixel at position w, h in iterable pixels )
        pixels [w , h ]= (grey , grey , grey)
        #appending the shade of grey integer value into the following iterable
        #if it is  defined for the first time
        if grey_shades.count(grey) == 0:
            grey_shades.append(grey)

#algorithm which determines what ascii character is specific to each shade of gray
#in order to fill the output text file
for h in range(new_height):
    for w in range(new_width):
        r ,g , b=pixels[ w, h]
        grey= ( r + g + b)//3
        out.write(asc_char[(len(asc_char)*grey)//256])
    out.write("\n")









