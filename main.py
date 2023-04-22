import sources

webcam = sources.Camera(id = 0, name = 'Webcam', fps = 15, show_fps = True, size = (340, 240))
phone = sources.Camera(id = 1, name = 'Phone', fps = 30, show_fps = True, size = (854, 480))
sources.connect([webcam, phone])