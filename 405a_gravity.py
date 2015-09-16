'''
Natahlie Beavers
natahliebeavers@gmail.com

'''

column_size = raw_input()
input_nums = raw_input()
#print type(input_nums)
input_list = input_nums.split(' ')

#print input_list

temp_no = 0

for i in range(0, int(column_size)):
    for j in range(0, int(column_size)-1):
        if(int(input_list[j])>int(input_list[j+1])):
            temp = int(input_list[j])
            input_list[j] = str(input_list[j+1])
            input_list[j+1] = str(temp)

print " ".join(input_list)
