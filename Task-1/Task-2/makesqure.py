#Task 1-2
import numpy as np
import cv2
# from google.colab.patches import cv2_imshow #colab cant read cv2.imshow()

def Create_Image(N):
  squre = np.ones((N,N), dtype=np.uint32) * 255   # draw a white page with N*N dimensions

  for row in range(0, N, N // 16): # traverse on the row of matrix (image frame)
      for col in range(0, N, N // 16): # traverse on the column of matrix (image frame)
          """
           traverse at the white page and find location for drawing black box
           for example N = 400 , N//16 -> 25  , so evry black box is 25*25
           Now we have a Traverse like :
           every box -> 25*25

           - box   box   box   box
           -    box   box   box   box
           - box   box   box   box
           -    box   box   box   box

          """
          if (row // (N // 16) + col // (N // 16)) % 2 == 0:
              # draw black box in the squre page
              squre[row:row + N // 16, col:col + N // 16] = 0

  # if replace a Bigger number instead of 16 at N//16 , our black box have smaller size
  # for
  cv2.imshow("squere",squre)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


Num = int(input("please Enter N :"))
Create_Image(Num)
