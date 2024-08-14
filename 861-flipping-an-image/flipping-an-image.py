class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for img in image:
            img.reverse()
            for i  in range(len(img)):
                if img[i]==0:
                    img[i]=1
                elif img[i] ==1:
                    img[i]=0
        return image