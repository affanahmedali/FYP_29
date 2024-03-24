#How to access the model
#Tip: Better to create a virtual envronment
#first install ultralytics module by
#pip install ultralytics==8.0.196

#import YOLO V8
from ultralytics import YOLO
from PIL import Image
import cv2

custom_model = 'YOLOV8_M1\yolov8s.pt'
model = YOLO(custom_model)
print("Model assigned")

#validation
model.val()

# # Predict/Inference
# # accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="YOLOV8_M1/FYP_DATA-1/test/images", show=True) # Display preds. Accepts all YOLO predict arguments

# from PIL
# im1 = Image.open("YOLOV8_M1/FYP_DATA-1/test/images/Ch20_20231204075001_mp4-196_jpg.rf.0742a6829c2ae5480a96ef5b8cce310c.jpg")
# results = model.predict(source=im1, save=True)  # save plotted images

# # from ndarray
# im2 = cv2.imread("YOLOV8_M1/FYP_DATA-1/test/images/Ch20_20231204075001_mp4-197_jpg.rf.83fef80887ca5679a343180fd6de462a.jpg")
# results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels

# # from list of PIL/ndarray
# results = model.predict(source=[im1, im2])



