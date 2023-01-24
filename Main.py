filename = input()
operation = int(input())


# FUNCTION TO PRINT THE IMAGE
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


handle = open(f"./Images and Fılters/{filename}")

# CONTROLLING FORMAT AND SUCH
format_checker = ""
temp_size_of_image = ""
counter = 0
max_color_value = 0
color_depth = -1
for i in handle:
    counter += 1
    if i.upper().strip() == "P2":
        format_checker = "pgm"
        continue
    elif i.upper().strip() == "P3":
        format_checker = "ppm"
        continue
    if counter == 2:
        temp_size_of_image = i
        continue
    if counter == 3:
        max_color_value = int(i.strip())
    break
if format_checker == "pgm":
    color_depth = 0
elif format_checker == "ppm":
    color_depth = 2

# CREATING EMPTY LIST OF DESIRED FORMAT
size_of_image = temp_size_of_image.strip().split()
image_list = []
for i in range(int(size_of_image[1])):
    image_list.append([])
    for m in range(int(size_of_image[0])):
        if format_checker == "pgm":
            image_list[i].append([[]])
        elif format_checker == "ppm":
            image_list[i].append([[], [], []])

# FILLING THE EMPTY LIST WITH GIVEN IMAGE
temp_number_list = []
for i in handle:
    i = i.strip("\n")
    i = i.strip("\t")
    i = i.strip(" ")
    k = i.split(" ")
    for m in k:
        m = m.split("\t")
        for a in m:
            if a == "":
                continue
            temp_number_list.append(a)
counter = 0
for i in range(int(size_of_image[1])):
    for m in range(int(size_of_image[0])):
        for n in range(color_depth + 1):
            image_list[i][m][n] = temp_number_list[counter]
            counter += 1

# FINDING THE AVERAGE OF A SECTION
average_counter = 0
final_total = 0


def average_finder(y, x):
    global average_counter, final_total
    if x > int(size_of_image[0]) - 1 or x < 0:
        return 0
    elif y > int(size_of_image[1]) - 1 or y < 0:
        return 0
    elif boolean_list[y][x] == [False]:
        return 0
    else:
        boolean_list[y][x] = [False]
        final_total += int(image_list[y][x][0])
        average_counter += 1
        return average_finder(y, x + 1) + average_finder(y, x - 1) + average_finder(y - 1, x) + average_finder(y + 1, x)


# USING THIS AVERAGE TO REFACTOR THE IMAGE
def average_applier(y, x, average):
    if (y, x) in location_of_blacks:
        return
    elif y > int(size_of_image[1]) - 1 or y < 0 or x > int(size_of_image[0]) - 1 or x < 0:
        return
    elif image_list[y][x][0] == average:
        return
    else:
        image_list[y][x][0] = average
        return average_applier(y, x + 1, average), average_applier(y, x - 1, average), \
               average_applier(y - 1, x, average), average_applier(y + 1, x, average)


# MAKING THE CONVOLUTION PATTERN
def convolution(y, x, the_filter):
    global stride
    if x > int(size_of_image[0]) - ((filter_size + 1) / 2):
        return convolution(y + stride, (filter_size - 1) / 2, the_filter)
    elif y > int(size_of_image[1]) - ((filter_size + 1) / 2):
        return image_list
    else:
        conv_red_total = 0
        index_cutter = (filter_size - 1) / 2
        for i in range(filter_size):
            for m in range(filter_size):
                y_axis = i - index_cutter
                x_axis = m - index_cutter
                conv_red_total += int(copied_list[int(y + y_axis)][int(x + x_axis)][0]) * float(the_filter[i][m])
        if conv_red_total > max_color_value:
            image_list[int(y)][int(x)][0] = max_color_value
        elif conv_red_total < 0:
            image_list[int(y)][int(x)][0] = 0
        else:
            image_list[int(y)][int(x)][0] = int(conv_red_total)

        conv_green_total = 0
        index_cutter = (filter_size - 1) / 2
        for i in range(filter_size):
            for m in range(filter_size):
                y_axis = i - index_cutter
                x_axis = m - index_cutter
                conv_green_total += int(copied_list[int(y + y_axis)][int(x + x_axis)][1]) * float(the_filter[i][m])
        if conv_green_total > max_color_value:
            image_list[int(y)][int(x)][1] = max_color_value
        elif conv_green_total < 0:
            image_list[int(y)][int(x)][1] = 0
        else:
            image_list[int(y)][int(x)][1] = int(conv_green_total)

        conv_blue_total = 0
        index_cutter = (filter_size - 1) / 2
        for i in range(filter_size):
            for m in range(filter_size):
                y_axis = i - index_cutter
                x_axis = m - index_cutter
                conv_blue_total += int(copied_list[int(y + y_axis)][int(x + x_axis)][2]) * float(the_filter[i][m])
        if conv_blue_total > max_color_value:
            image_list[int(y)][int(x)][2] = max_color_value
        elif conv_blue_total < 0:
            image_list[int(y)][int(x)][2] = 0
        else:
            image_list[int(y)][int(x)][2] = int(conv_blue_total)

        return convolution(y, x + stride, the_filter)


if operation == 1:
    # CREATING BOOLEAN LIST TO CHECK UNIQUENESS OF VALUES
    boolean_list = []
    for i in range(int(size_of_image[1])):
        boolean_list.append([])
        for m in range(int(size_of_image[0])):
            boolean_list[i].append([True])

    # TURNING ZEROS TO FALSE
    location_of_blacks = []
    for i in range(int(size_of_image[0])):
        for m in range(int(size_of_image[1])):
            if image_list[i][m][0] == "0":
                location_of_blacks.append((i, m))
                boolean_list[i][m] = [False]

    # APPLYING THE AVERAGE
    for i in range(int(size_of_image[0])):
        for m in range(int(size_of_image[1])):
            average_finder(i, m)
            if average_counter != 0:
                average_for_section = int(final_total / average_counter)
                average_applier(i, m, average_for_section)
            final_total = 0
            average_counter = 0

    img_printer(image_list)


elif operation == 2:
    filter_name = input()
    stride = int(input())

    # UNDERSTANDING THE FILTER
    filter_list = []
    handle = open(f"./Images and Fılters/{filter_name}")
    for i in handle:
        i = i.strip("\n")
        c = i.split(" ")
        filter_list.append(c)
    filter_size = len(filter_list)

    # COPYING THE IMAGE LIST
    copied_list = []
    for i in range(len(image_list)):
        temp_list = []
        for m in range(len(image_list[i])):
            tempry_list = []
            for n in image_list[i][m]:
                tempry_list.append(n)
            temp_list.append(tempry_list)
        copied_list.append(temp_list)

    convolution(int((filter_size - 1) / 2), int((filter_size - 1) / 2), filter_list)

    # CREATING THE FINAL LIST
    final_conv_list = []
    for i in range(int((filter_size - 1) / 2), int(len(image_list) - (filter_size - 1) / 2), stride):
        temp_list = []
        for m in range(int((filter_size - 1) / 2), int(len(image_list) - (filter_size - 1) / 2), stride):
            tempry_list = []
            for n in range(3):
                tempry_list.append(image_list[i][m][n])
            temp_list.append(tempry_list)
        final_conv_list.append(temp_list)

    # PRINTING THE FINAL IMAGE
    img_printer(final_conv_list)
