tesseract_path = ''
tesseract_config = ('-l eng --oem 1 --psm 3') #Page Segmentation Mode (psm)

def getTable(img, Min_Yaxis_Bias=True, show=True, *args, **kwargs):
        if type(img) == str:
                img = cv2.imread(img)
                elif type(img) == np.ndarray or type(img) == list:
            img = np.array(img)
        else:
            raise TypeError('expected required argument to be a str to path or a list or numpy.ndarray, but pass {}'.format(type(img)))
        ret, thresh_value = cv2.threshold(self.img,
                                         self.greyscale_threshold,
                                         255,
                                         cv2.THRESH_BINARY_INV)

        thresh_value = cv2.bitwise_not(thresh_value) 

        edges = cv2.Canny(thresh_value,
                          self.canny_threshold1,
                          self.canny_threshold2,
                          apertureSize=3)

        lines = cv2.HoughLinesP(edges,
                                rho=1,
                                theta=np.pi/180,
                                threshold=self.HoughLinesP_threshold,
                                 minLineLength=self.HoughLinesP_minLineLength,
                                maxLineGap=self.HoughLinesP_maxLineGap)
        _lines = []
        _img = self.img.copy()
        for line in lines:
            for x in line:
                x1 = x[0]
                y1 = x[1]
                x2 = x[2]
                y2 = x[3]
                if x1 == x2:
                    _lines.append(x)
                    cv2.line(_img,(x1,y1),(x2,y2),(0,0,255),2)

    #     image = self.img.copy()
        x1 = min([i[0] for i in _lines])
        x2 = max([i[2] for i in _lines])

        if Min_Yaxis_Bias:
            y1 = min([i[1] for i in _lines])
            y2 = max([i[3] for i in _lines])
        else:
            y1 = max([i[1] for i in _lines])
            y2 = min([i[3] for i in _lines])

        if y1 > y2:
            y2, y1 = y1, y2
        if x1 > x2:
            x2, x1 = x1, x2

        table = _img[y1:y2,x1:x2]

        if show:
            cv2.imshow("extracted table", table)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else: 
            return table
        self.lines = np.array(_lines)
        self.table = table
        self.y1 = y1
        self.y2 = y2
