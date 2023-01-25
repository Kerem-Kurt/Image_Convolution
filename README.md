# Image_Convolution
Image convolution and averaging operation with pgm files

This software can do 2 things:

1- It can group the areas that are seperated by black color in a pgm file and color every pixel there to the average of the group.

(Normally all the colors are the same at the same region (You can check from the output section), but while converting the file to jpg format there were some troubles I didn't understand)

![ex1](https://user-images.githubusercontent.com/121832450/214449414-ad452006-8ca0-4c24-be14-b79e1cd99ec2.jpg) ![ex1_changed](https://user-images.githubusercontent.com/121832450/214449467-5135ded0-96a5-4a30-b33e-c7d3de8e52df.jpg) ______________ ![ex2](https://user-images.githubusercontent.com/121832450/214449503-797ba25e-a981-4abc-992b-67a2674cb215.jpg)    ![ex2_changed](https://user-images.githubusercontent.com/121832450/214449519-93e062c0-f030-4f43-adf2-1e9e4d515a93.jpg)

![ex3](https://user-images.githubusercontent.com/121832450/214449543-779bfd78-07f0-47bb-89ad-8607f65415ba.jpg) ![ex3_changed](https://user-images.githubusercontent.com/121832450/214449578-cd67e08e-d91c-4b40-bf20-e7a5c9ef04ee.jpg) ______________ ![ex4](https://user-images.githubusercontent.com/121832450/214449606-75dea032-ac1f-42e3-954d-64b16ef7e3f1.jpg)    ![ex4_changed](https://user-images.githubusercontent.com/121832450/214449628-110ae490-0a48-48b1-87d3-07b268d60a0f.jpg)

2- It can do Image convolution with a given filter.(In my examples I have vertical, horizontal and gaussian filters)

First Image:![img3](https://user-images.githubusercontent.com/121832450/214450648-2d312cbf-2600-4e8b-85ac-af13d0b95c81.jpg)

Horizontal Convolution:![img3_horizontal_convolution](https://user-images.githubusercontent.com/121832450/214450674-d77cf867-0d71-4b48-bacf-c984991f5628.jpg) 

Vertical Convolution: ![img3_vertical_convolution](https://user-images.githubusercontent.com/121832450/214450702-2f2db5c7-9795-48ec-a05d-7deef6297acf.jpg)

