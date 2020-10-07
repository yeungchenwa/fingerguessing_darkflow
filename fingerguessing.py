from darkflow.net.build import TFNet
import cv2

options = { "model": "cfg/yolov2-voc.cfg", "load": "bin/yolov2-voc_final.weights", "threshold": 0.65, "demo": "camera", "gpuName": "/gpu:0", "gpu": 0.5}

tfnet = TFNet(options)

imgcv = cv2.imread("./sample_img/5.jpg")
result = tfnet.return_predict(imgcv)
print(result)
