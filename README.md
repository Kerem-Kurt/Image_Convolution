# Image_Convolution
Image convolution and averaging operation with pgm files
<br><br>
(All images are resized for easier understanding)
<br>

<h3> 1- It can do Image convolution with a given filter. </h3>
(In my examples I have vertical, horizontal and gaussian filters)
<br><br>
First Image &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Horizontal Convolution &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Vertical Convolution

![img3](https://user-images.githubusercontent.com/121832450/214450779-cb4def86-b888-43ac-b770-e2a06ccedd3c.jpg) &nbsp; &nbsp; &nbsp; ![img3_horizontal_convolution](https://user-images.githubusercontent.com/121832450/214450789-a86857de-8273-43b4-976a-8e8af474987e.jpg) &nbsp;  &nbsp; &nbsp; ![img3_vertical_convolution](https://user-images.githubusercontent.com/121832450/214450823-08c09790-768a-40f9-8457-c359d010ec9f.jpg)

<br><br>

Second Image &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Horizontal Convolution &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  Vertical Convolution &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Gaussian Convolution

![img4](https://user-images.githubusercontent.com/121832450/214452591-1e812062-b009-4a81-8182-3c765f3f46a4.jpg) &nbsp; &nbsp; &nbsp; ![img4_horizontal_convolution](https://user-images.githubusercontent.com/121832450/214452689-be0c33af-e2e8-42ec-8a5e-fad97b4df96b.jpg) &nbsp; &nbsp; &nbsp; ![img4_vertical_convolution](https://user-images.githubusercontent.com/121832450/214452695-e44e63ab-aeaf-47a6-b9e8-c190d5f0035a.jpg) &nbsp; &nbsp; &nbsp; ![img4_gaussian_convolution](https://user-images.githubusercontent.com/121832450/214452708-8d36aa54-fa57-4de8-b2fd-55c1431d2afb.jpg)

<br><br>

<h3> 2- It can group the areas that are seperated by black color in a pgm file and color every pixel there to the average of the group.  </h3>

(Normally all the colors are the same at the same region (You can check from the output section), but while converting the file to jpg format there were some troubles I didn't understand)

![ex1](https://user-images.githubusercontent.com/121832450/214449414-ad452006-8ca0-4c24-be14-b79e1cd99ec2.jpg) ![ex1_changed](https://user-images.githubusercontent.com/121832450/214449467-5135ded0-96a5-4a30-b33e-c7d3de8e52df.jpg) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ![ex2](https://user-images.githubusercontent.com/121832450/214449503-797ba25e-a981-4abc-992b-67a2674cb215.jpg)    ![ex2_changed](https://user-images.githubusercontent.com/121832450/214449519-93e062c0-f030-4f43-adf2-1e9e4d515a93.jpg)
<br><br><br>
![ex3](https://user-images.githubusercontent.com/121832450/214449543-779bfd78-07f0-47bb-89ad-8607f65415ba.jpg) ![ex3_changed](https://user-images.githubusercontent.com/121832450/214449578-cd67e08e-d91c-4b40-bf20-e7a5c9ef04ee.jpg) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ![ex4](https://user-images.githubusercontent.com/121832450/214449606-75dea032-ac1f-42e3-954d-64b16ef7e3f1.jpg)    ![ex4_changed](https://user-images.githubusercontent.com/121832450/214449628-110ae490-0a48-48b1-87d3-07b268d60a0f.jpg)


