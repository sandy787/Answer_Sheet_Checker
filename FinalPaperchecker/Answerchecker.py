import cv2
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv2.imread('FinalTest.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)

contours, hierarchy = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
textList = []
for i, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 30 and h > 30:
        box_img = img[y:y+h, x:x+w]
        text = pytesseract.image_to_string(box_img)
        textList.append(text.replace("\n", ""))
textList1 = []
for i in textList:
    abc = float(i)
    textList1.append(abc)
set1 = set(textList1)
stuList = list(set1)


# JANHAVI

initialMks = []
modelList = []
mksList = []
maxList = []

for i in range(0, len(stuList)):
    modelAns = float(input("Enter model answer: "))
    maxDiff = float(input("Enter max. allowable difference: "))
    weightage = float(input("Enter weightage of the question: "))
    modelList.append(modelAns)
    maxList.append(maxDiff)
    mksList.append(weightage)
    if stuList[i] == modelList[i]:
        initialMks.append(mksList[i])
    elif ((modelList[i]-maxList[i]) <= stuList[i] < modelList[i]) or (modelList[i] < stuList[i] <= (modelList[i]-maxList[i])):
        initialMks.append(mksList[i]*0.5)
    else:
        initialMks.append(0)

print('\n')
print("-----------------------------------------")
print(f'Model Answer: {modelList}')
print(f'Students answer: {stuList}')
print(f'Total marks scored: {sum(initialMks)}')
