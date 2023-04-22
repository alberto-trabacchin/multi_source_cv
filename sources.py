import cv2 as cv
import time
import threading

class Camera(threading.Thread):
    def __init__(self, id, name, fps, size = (720, 1280), show_fps = False) -> None:
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.fps = fps
        self.show_fps = show_fps
        self.size = size
    
    def run(self):
        print(f'Trying to connect {self.name}...')
        cap = cv.VideoCapture(self.id)
        print(f'{self.name} connected.')
        t_read = time.time()
        while True:
            ret, frame = cap.read()
            if ret == False:
                print(f'Error reading frame from {self.name}.')
            frame = cv.resize(frame, self.size)
            if self.show_fps:
                frame = self.print_fps(t_read, frame)
                t_read = time.time()
            cv.imshow(self.name, frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                print(f'{self.name} closed.')
                break
    
    def print_fps(self, t_read, frame):
        t_period = 1 / self.fps
        elaps_time = time.time() - t_read
        t_sleep = t_period - elaps_time
        if t_sleep > 0:
            time.sleep(t_sleep)
        else:
            t_sleep = 0
        fps_real = int(1 / (elaps_time + t_sleep))
        message = f'FPS: {fps_real}'
        cv.putText(frame, message, org = (15, 35), fontFace = cv.FONT_HERSHEY_SIMPLEX,
                   fontScale = 0.6, color = (0, 0, 255), thickness = 2)
        return frame
    
def connect(srcs):
    for s in srcs:
        s.start()