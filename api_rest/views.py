from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from google import genai
from django.conf import settings
import logging
import time

logger = logging.getLogger(__name__)

class QuestionAnswerAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        question = request.data.get("question")
        if not question:
            return Response({"error": "Parâmetro 'question' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        logger.info(f"Nova requisição recebida. Pergunta: {question}")

        try:
            start_time = time.time()
            
            client = genai.Client(api_key=settings.GEMINI_API_KEY)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )

            elapsed_time = round(time.time() - start_time, 3)

            clean_text = response.text.replace('\n\n', ' ').replace('\n', ' ').replace('*', '').strip()
            logger.info(f"Resposta gerada em {elapsed_time}s: {clean_text[:100]}...")
            return Response({"response": clean_text})

        except Exception as e:
            logger.exception("Erro ao processar a requisição")

            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
