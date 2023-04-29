# ~/slackbot/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from slacker import Slacker

# 봇 토큰 추가
bot_token = 'xoxb-'

# Create your views here.
class Attend(APIView):
    def post(self, request):
        """
        슬랙에서 채팅 이벤트가 있을 때 호출하는 API
        :param request:
        :return:
        """

        # 요청이 어떻게 들어오나 찍어보기
        print(request.body)

        # body에서 challenge 필드만 빼오기
        challenge = request.data.get('challenge')

        user = request.data.get('event').get('user')
        text = request.data.get('event').get('text')
        print("사용자 :", user, "| 메시지 :", text)

        if user == 'U01C9LJS1PF':
            print("봇 메시지")
        else:
            # 토큰으로 slacker를 만들어줍니다.
            slack = Slacker(bot_token)
            # 요기가 메시지 보내는 부분
            slack.chat.post_message('#일반', f'ToDoList:{text}', as_user=None)

        # 응답 데이터로 { challenge : challenge } 주기
        return Response(status=200, data=dict(challenge=challenge))
