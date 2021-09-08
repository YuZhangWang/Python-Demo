import cv2
import json
import face_recognition
import numpy as np
from django.core import serializers
from django.db.migrations.operations import models
from django.http import JsonResponse


# 创建人脸检测级联分类器对象实例
face_cascade = cv2.CascadeClassifier("cascades\\haarcascade_frontalface_default.xml")


# 使用ORM
# all()返回的是QuerySet 数据类型；values()返回的是ValuesQuerySet 数据类型
def changeToJSON(photoData):
    image = face_recognition.load_image_file(photoData)
    face_encoding = face_recognition.face_encodings(image)[0]
    stringInfo = face_encoding.tostring()
    return stringInfo


