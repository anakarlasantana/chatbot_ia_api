# Teste Técnico - Desenvolvedor Backend JR - Petlove 🐶

Este projeto consiste na criação de uma API com integração a um modelo de IA generativa (Google Gemini) para servir como **assistente de vendas** para um e-commerce.

---

## ⚙️ Tecnologias utilizadas

- Python 3.13
- Django 5.2.5
- Django REST Framework
- Google Gemini API (IA generativa)
- DRF Spectacular (documentação com Swagger/Redoc)
- Testes com DRF `APITestCase`
- Logs e tempo de execução com `logging`
- Observabilidade básica com logs estruturados

---

## 📌 Funcionalidade da API

A API recebe uma pergunta do usuário relacionada ao e-commerce (ex: tipos de ração, cuidados com pets, etc.), envia para o modelo de IA da Google (Gemini) e retorna a resposta gerada, formatada para leitura.

---

## 🔗 Endpoint

- **URL:** `POST /api/question-and-answer`
- **Content-Type:** `application/json`

### 📥 Exemplo de requisição:

```json
{
  "question": "Qual a melhor ração para golden?"
}
```

### 📤 Exemplo de resposta esperada:

```json
{
  "response": "A melhor ração para o seu Golden será aquela que o mantém com boa energia, peso ideal, fezes firmes, pelagem brilhante e boa saúde geral. Escolher a ração certa é um investimento na saúde e longevidade do seu Golden Retriever!"
}
```

---

## 🔒 Validação e Tratamento

- Retorna `400` se a pergunta estiver ausente.
- Retorna `500` se houver erro de comunicação com a IA.

---

## 📄 Documentação Interativa

- Swagger UI: [http://localhost:8000/api/docs/swagger-ui/](http://localhost:8000/api/docs/swagger-ui/)
- Redoc: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- Schema JSON: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

---

## 🧪 Testes

Os testes foram criados com `APITestCase` e incluem:

- Requisição válida com pergunta
- Requisição inválida sem pergunta
- Simulação de erro mockado

Para executar os testes:

```bash
python manage.py test
```

---

## 🛰️ Observabilidade

O projeto implementa **observabilidade básica** com:

- Logs de entrada e saída via `logging`
- Tempo de resposta calculado com `time.time()`
- Tratamento de exceções com `logger.exception`

> Ferramentas como Sentry ou Datadog podem ser adicionadas com uma linha de código extra para captura de exceções.

---

## 🚀 Como rodar o projeto localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/chatbot-petlove-api.git
   cd chatbot-petlove-api
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   venv\Scripts\activate     
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo .env com base no .env.sample:
   ```python
   GEMINI_API_KEY = "sua-chave-aqui"
   ```
   - Para criar sua API_KEY é só acessar o botão 'Gerar uma chave da API Gemini' nesse endereço: https://ai.google.dev/gemini-api/docs?hl=pt-br

5. Rode as migrações para criar o banco de dados:
   ```bash
   python manage.py migrate
   ```

6. execute o servidor local:
   ```bash
   python manage.py runserver
   ```

7. Teste a API:
Você pode testar o endpoint da API usando ferramentas como **Insomnia**, **Postman** ou **Thunder Client**:
   ```bash
   POST http://localhost:8000/api/question-and-answer
   ```
---

## ✅ Requisitos de Entrega do Projeto
- [x] 1. Criar API
- [x] 2. Integrar com a IA
- [x] 3. Endpoint da API
- [x] 4. Projeto no GitHub

## ✨ Funcionalidades Extras
- [x] Testes automatizados
- [x] Logs e observabilidade
- [x] Documentação
- [x] Resposta formatada e limpa

---

Feito com ❤️ por Ana Karla Santana