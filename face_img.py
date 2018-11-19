
# -*- coding: UTF-8 -*-
import cPickle
import os
import shutil
import cv2
import numpy as np

#图像匹配
class ImgMatch():
    def __init__(self,ImgStr,ImgOrc):
        self.imgDst = cv2.imread(ImgStr)
        self.imgOrc = cv2.imread(ImgOrc)
        self.mothods = cv2.TM_SQDIFF_NORMED
        self.sift = cv2.SIFT()



    def img_match(self):
        #cv2.matchTemplate(self.imgStr,self.imgOrc,self.mothods)
        diff = cv2.subtract(self.imgStr,self.imgOrc)
        return float(np.mean(diff))

    def img_sift(self):
        img_dst = self.imgDst.copy()
        img_orc = self.imgOrc.copy()
        kp1, des1 = self.sift.detectAndCompute(img_dst, None)
        kp2, des2 = self.sift.detectAndCompute(img_orc, None)

        # BFmatcher with default parms
        bf = cv2.BFMatcher(cv2.NORM_L2)
        #print des1, des2
        matches = bf.knnMatch(des1, des2, k=2)
        goodMatch = []
        b_result = False
        for m, n in matches:
            if m.distance < 0.90 * n.distance:
                goodMatch.append(m)
        print len(goodMatch),len(matches)
        if len(goodMatch) > 0.2 * len(matches):
            b_result = True
        else:
            b_result = False
        return b_result

#图像分类
def createDir(path,count):
    dir_name = path + os.sep + str(count)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return dir_name

orc_path = "F:\\Python\\face_detector\\img"
count = 1



if __name__ == "__main__":
    imgs = os.listdir(orc_path)
    for img in imgs:
        if ".jpg" == img[-4:]:
            dst_path = createDir(orc_path,count)
            shutil.copy(orc_path + os.sep + img, dst_path)
            for o_img in imgs[count:]:
                print count
                print img,o_img
                i_img = ImgMatch(orc_path + os.sep + img,orc_path + os.sep + o_img)
                b_result = i_img.img_sift()
                if b_result:
                    shutil.copy(orc_path + os.sep + o_img , dst_path)
            count += 1