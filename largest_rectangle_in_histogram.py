'''area of largest rectangle in a given histogram,
the hostogram presented as a list of integers.'''

def max_rect_in_histogram(given_list):
    
    if not given_list: #the list should be nonempty.
        return 0
    else:
        right_width_list=[]
        left_width_list=[]
        '''starting at each vertical bar, 
        look both ways till you reach a maximum rectangle'''
        for i in range(len(given_list)):
            j=0
            while i+j<=len(given_list)-1 and given_list[i+j]>=given_list[i]:
                j=j+1
            right_width_list.append(i+j-1)
            j=0
            while i-j>=0 and given_list[i-j]>=given_list[i]:
                j=j+1
            left_width_list.append(i-j+1)
        widths=[right_width_list[i]-left_width_list[i]+1 for i in range(len(given_list))]
        areas=[given_list[i]*widths[i] for i in range(len(given_list))]
        #print(widths)
        #print(areas)
        return max(areas)