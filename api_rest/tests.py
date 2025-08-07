from unittest.mock import patch
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api_rest.views import genai  

class QuestionAnswerAPITests(APITestCase):
    def test_question_answer_success(self):
        url = reverse('question-answer')  
        data = {"question": "Qual é a capital do Brasil?"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("response", response.data)

    def test_question_answer_missing_question(self):
        url = reverse('question-answer')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    @patch("api_rest.views.genai.Client")
    def test_question_answer_internal_error(self, mock_genai_client):
        mock_genai_client.side_effect = Exception("Erro simulado na IA")

        url = reverse('question-answer')
        data = {"question": "Simule uma falha"}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.data)
