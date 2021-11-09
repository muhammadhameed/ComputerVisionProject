import cv2
import threading


class camThreadOffline(threading.Thread):
    def __init__(self, windowName, camID):
        threading.Thread.__init__(self)
        self.windowName = windowName
        self.camID = camID
    def run(self):
        print("Starting " + self.windowName)
        camPreviewOffline(self.windowName, self.camID)


def camPreviewOffline(windowName, camID):
    cv2.namedWindow(windowName)
    capture1 = cv2.VideoCapture(camID)

    width1 = int(capture1.get(3))
    height1 = int(capture1.get(4))
    size1 = (width1, height1)

    recordingName = 'Stream' + windowName + '.avi'
    optputFile1 = cv2.VideoWriter(
        recordingName, cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)

    if capture1.isOpened():
            ret1, frame1 = capture1.read()
    else:
        ret1 = False

    while ret1:
        ret1, frame1 = capture1.read()

        # sample feed display from camera 1
        cv2.imshow(windowName, frame1)

        # saves the frame from camera 1
        optputFile1.write(frame1)

        # escape key (27) to exit
        if cv2.waitKey(1) == 27:
            break

    capture1.release()
    optputFile1.release()
    cv2.destroyAllWindows()


class camThreadOnline(threading.Thread):
    def __init__(self, windowName, camID):
        threading.Thread.__init__(self)
        self.windowName = windowName
        self.camID = camID
    def run(self):
        print("Starting " + self.windowName)
        camPreviewOnline(self.windowName, self.camID)


def camPreviewOnline(windowName, camID):
    cv2.namedWindow(windowName)
    capture1 = cv2.VideoCapture(camID)

    if capture1.isOpened():
        ret1, frame1 = capture1.read()
    else:
        ret1 = False

    while ret1:
        ret1, frame1 = capture1.read()

        # sample feed display from camera 1
        cv2.imshow(windowName, frame1)

        # escape key (27) to exit
        if cv2.waitKey(1) == 27:
            break

    capture1.release()
    cv2.destroyAllWindows()





def main():
    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())
    
    if(option == 1):   
        thread1 = camThreadOffline("Camera1", 0)
        thread2 = camThreadOffline("Camera2", 'http://10.130.143.127:8080/video')
        thread3 = camThreadOffline("Camera3", 'http://10.130.143.206:8080/video')

        thread1.start()
        thread2.start()
        thread3.start()

    elif(option == 2):
        thread1 = camThreadOnline("Camera1", 0)
        thread2 = camThreadOnline("Camera2", 'http://10.130.143.127:8080/video')
        thread3 = camThreadOnline("Camera3", 'http://10.130.143.206:8080/video')

        thread1.start()
        thread2.start()
        thread3.start()

    else:
        print("Invalid option entered. Exiting...")

main()

# def main():

#     print("Press 1 for pre-recorded videos, 2 for live stream: ")
#     option = int(input())

#     if option == 1:
#         # Record video
#         windowName = "Sample Feed from Camera 1"
#         cv2.namedWindow(windowName)

#         # capture1 = cv2.VideoCapture(0)  # laptop's camera
#         # capture1 = cv2.VideoCapture("http://10.130.143.127:8080/video")   # sample code for mobile camera video capture using IP camera
#         #capture1 = cv2.VideoCapture("http://192.168.43.116:8080/video")
#         l = [0, 'http://10.132.174.97:8080/video']

#         capture2 = cv2.VideoCapture("http://10.132.174.97:8080/video")
        
#         # define size for recorded video frame for video 1
#         width1 = int(capture1.get(3))
#         height1 = int(capture1.get(4))
#         size1 = (width1, height1)


#         # frame of size is being created and stored in .avi file
        # optputFile1 = cv2.VideoWriter(
        #     'Stream1Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)


#         # check if feed exists or not for camera 1
        # if capture1.isOpened():
        #     ret1, frame1 = capture1.read()
        # else:
        #     ret1 = False

        # while ret1:
        #     ret1, frame1 = capture1.read()

        #     # sample feed display from camera 1
        #     cv2.imshow(windowName, frame1)

        #     # saves the frame from camera 1
        #     optputFile1.write(frame1)

        #     # escape key (27) to exit
        #     if cv2.waitKey(1) == 27:
        #         break

        # capture1.release()
        # optputFile1.release()
        # cv2.destroyAllWindows()

#     elif option == 2:
#         # live stream
#         windowName1 = "Live Stream Camera 1"
#         cv2.namedWindow(windowName1)

#         capture1 = cv2.VideoCapture(0)  # laptop's camera

#         if capture1.isOpened():  # check if feed exists or not for camera 1
#             ret1, frame1 = capture1.read()
#         else:
#             ret1 = False

#         while ret1:  # and ret2 and ret3:
#             ret1, frame1 = capture1.read()
#             cv2.imshow(windowName1, frame1)

#             if cv2.waitKey(1) == 27:
#                 break

#         capture1.release()
#         cv2.destroyAllWindows()

    # else:
    #     print("Invalid option entered. Exiting...")


# main()
