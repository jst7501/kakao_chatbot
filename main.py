from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
import json

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록


@api.route('/hello')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def post(self, name):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        print(name)
        a = {"version": "2.0",
             "template": {
                 "outputs": [
                     {
                         "simpleText": {
                             "text": "총 2개의 예약 내역이 있습니다. 취소할 예약을 선택해 주세요."
                         }
                     },
                     {
                         "carousel": {
                             "type": "itemCard",
                             "items": [
                                 {
                                     "imageTitle": {
                                         "title": "예약 완료",
                                         "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/wine.jpg"
                                     },
                                     "itemList": [
                                         {
                                             "title": "매장명",
                                             "description": "판교 A스퀘어점"
                                         },
                                         {
                                             "title": "예약 일시",
                                             "description": "2022.12.25, 19:30"
                                         },
                                         {
                                             "title": "예약 인원",
                                             "description": "4명"
                                         },
                                         {
                                             "title": "예약금",
                                             "description": "40,000원 (결제 완료)"
                                         }
                                     ],
                                     "itemListAlignment": "left",
                                     "buttons": [
                                         {
                                             "label": "예약 정보",
                                             "action": "message",
                                             "messageText": "예약 정보"
                                         },
                                         {
                                             "label": "예약 취소",
                                             "action": "message",
                                             "messageText": "예약 취소"
                                         }
                                     ]
                                 },
                                 {
                                     "imageTitle": {
                                         "title": "결제 대기",
                                         "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/pizza.jpg"
                                     },
                                     "itemList": [
                                         {
                                             "title": "매장명",
                                             "description": "정자역점"
                                         },
                                         {
                                             "title": "예약 일시",
                                             "description": "2022.12.25, 19:25"
                                         },
                                         {
                                             "title": "예약 인원",
                                             "description": "3명"
                                         },
                                         {
                                             "title": "예약금",
                                             "description": "30,000원 (결제 대기)"
                                         }
                                     ],
                                     "itemListAlignment": "left",
                                     "buttons": [
                                         {
                                             "label": "예약 취소",
                                             "action": "message",
                                             "messageText": "예약 취소"
                                         },
                                         {
                                             "label": "결제",
                                             "action": "message",
                                             "messageText": "결제"
                                         }
                                     ]
                                 }
                             ]
                         }
                     }
                 ],
                 "quickReplies": [
                     {
                         "messageText": "인기 메뉴",
                         "action": "message",
                         "label": "인기 메뉴"
                     },
                     {
                         "messageText": "최근 주문",
                         "action": "message",
                         "label": "최근 주문"
                     },
                     {
                         "messageText": "장바구니",
                         "action": "message",
                         "label": "장바구니"
                     }
                 ]
             }}

        return a


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
