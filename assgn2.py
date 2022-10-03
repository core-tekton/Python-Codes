fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    l = line.split()
    for a in l:
        if a not in lst:
            lst.append(a)
lst.sort()
print(lst)



    def cropImage(self, img):
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _,thresholded = cv2.threshold(grayscale, 0, 255, cv2.THRESH_OTSU)
        #cv2.imwrite("otsu.png", thresholded)
        bbox = cv2.boundingRect(thresholded)
        x, y, w, h = bbox
        #print(bbox)
        croppedImg = img[y:y+h, x:x+w]
        return croppedImg
