import pprint
import numpy as np
__author__ = 'natahlie'



plate_dimensions = raw_input("print height, length, and width ").split(" ")
plate_height = int(plate_dimensions[0])
plate_length = int(plate_dimensions[1])
plate_width = int(plate_dimensions[2])


plate_stack = np.zeros((plate_height, plate_length, plate_width))
blank_line_count  = plate_height + 1

total_expected_line_count = blank_line_count + (plate_height * plate_length) +1
#print blank_line_count
#print total_expected_line_count
plate_stack = [[[0 for _ in xrange(plate_width)] for _ in xrange(plate_length)] for _ in xrange(plate_height)]
#print plate_stack

#get input
i = 0
plate_count = 0
row_count = 0
#print plate_stack
#print plate_length



while(i < total_expected_line_count):
    input_line = raw_input()
    #print input_line + " " + str(len(input_line))

    if len(input_line)== plate_length:
        #print "plate: " + str(plate_count) + " row: " + str(row_count)
        #print input_line
        j = 0
        while(j < plate_length):
            #print str(plate_count-1) + " " + str(row_count) + " " + str(j)

            plate_stack[plate_count-1][row_count][j] = input_line[j]
            j+=1
        row_count+=1
    else:
        row_count = 0
        plate_count+=1
    i+=1


print plate_stack