'''
Created on Jan 18, 2016

@author: mike
'''

if __name__ == '__main__':
    # Write code using find() and string slicing to extract the number at the end of the line below. 
    #Convert the extracted value to a floating point number and print it out.
    text = "X-DSPAM-Confidence:    0.8475";
    zeroPos = text.find(':')
    num = float(text[zeroPos+1:])
    print num