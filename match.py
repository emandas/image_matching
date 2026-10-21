import cv2
def match():
    inp1 = input('Enter img1\'s absolute path : '  )
    inp2 = input('Enter img2\'s absolute path : '  )
    
    
    
    img = cv2.imread(inp1,0)
    img2 = cv2.imread(inp2,0)
    img = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)[1]
    img2 = cv2.threshold(img2,150,255,cv2.THRESH_BINARY_INV)[1]
    contours,hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2,hierarchy2 = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    M1  = cv2.moments(contours[1])
    hu1 = cv2.HuMoments(M1)
    print('###First images###')
    print("Moments: ",M1)
    print("Hu: ",hu1)
    print("-"*50)
    M2 = cv2.moments(contours2[1])
    hu2 = cv2.HuMoments(M2)
    print('###Second images###')
    print("Moments2: ",M2)
    print("Hu2: ",hu2)
    print("-"*50)
    i = 0;c=None
    for h in hu1:
        for h2 in hu2:
            if h == h2:
                c = True
                i +=1
                break
            else:
                c = False
    
    match int(i) :
        case 7 :
            print('images match')
        case _ :
            print('images not match')

if __name__ == '__main__': match()
