#-*-encoding:utf-8
import cv2
import cognitive_face as CF
import restapi


# API 기본 정보 입력
KEY = 'b778bc145b444986810110b7b0a24835'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)


# 카메라로 얼구 ㄹ촬영
def capture():
	# 카메라 캡처
	vidcap = cv2.VideoCapture(0)

	# 이미지 캡처 성공여부, 이미지 저장
	success, image = vidcap.read()
	print(success)
	
	# 이미지 파일 저장
	cv2.imwrite('image.jpg', image)
	
	# 카메라 종료
	vidcap.release()

	return success

# 캡처한 이미지 API에 전송
def post():
	img_path = 'image.jpg'
	result = CF.face.detect(img_path)
	print "faces : " + str(len(result))
	return len(result)

# 감정 데이터 출력
def printResult():
	# 감정 데이터 받아오기
	emotion_list = restapi.GetEmotion()

	emotion_str = ''
	for key in emotion_list.keys():
		emotion_str += key + " : " + str(emotion_list[key]) + "\n"
	print(emotion_str)
	return emotion_str


def play():
	result_str = ''
	if capture() == True:
		# 캡처 성공시 이미지 전송
		faces = post()
		# 얼굴 정보가 1개일 때만 실행
		if faces == 1:
			result_str = printResult()
		elif faces == 0:
			print("No detected. Try Again.")
		else:
			print("Many people. Do One person.")
	else:
		# 캡처 실패
		print("Camera Error")
	
	print('faceapi end')
	return result_str

if __name__ == '__main__':
	play()
