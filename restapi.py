#-*-coding:utf-8
import urllib
import requests
from os.path import expanduser

def GetEmotion():
	# API 기본 정보
	subscription_key = "b778bc145b444986810110b7b0a24835"
	assert subscription_key

	face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

	# 이미지 파일 경로
	image_path = "image.jpg"

	# API 키 전송
	headers = {
		'Content-Type': 'application/octet-stream',
		'Ocp-Apim-Subscription-Key': subscription_key}

	# 잡 데이터 제외, 감정 데이터만 받아옴
	params = urllib.urlencode({
		'returnFaceId': 'false',
		'returnFaceLandmarks': 'false',
		'returnRecognitionModel': 'false',
		'returnFaceAttributes': 'emotion'})
	
	
	# 방금 찍은 얼굴 사진을 분석한 감정 데이터를 API 키 값으로 찾아 받아오기	 
	post_url = face_api_url + "%s" % params


	# 동일 이미지 파일
	image_data = open(expanduser(image_path), "rb")
	
	# 감정 데이터 요청
	response = requests.post(
		face_api_url, headers=headers, params=params, data=image_data)
	# 결과 코드 받아와 분석
	response.raise_for_status()
	
	# 분석 값 받아와서 분석 데이터 도출
	analysis = response.json()
	emotions = analysis[0].get(u'faceAttributes').get(u'emotion')

	return emotions
	

if __name__ == "__main__":
	GetEmotion()
