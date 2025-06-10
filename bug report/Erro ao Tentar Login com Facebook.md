# Erro 403 ao tentar login via Facebook

## Ambiente

- **Plataforma:** Web
- **Navegador:** Google Chrome
- **Data/Hora da ocorrência:** 09/06/2025 22:50

---

## Passos para reproduzir

1. Acesse o site **Advantage Online Shopping**.
2. Clique no ícone de login.
3. Selecione a opção **"Sign in with Facebook"**.

---

## Resultado Atual

- Uma requisição `facebookLogin` é enviada via API.
- O servidor retorna a seguinte resposta:

```json
{
  "success": false,
  "reason": "403 FORBIDDEN Sorry, connecting to Facebook is currently unavailable. Please try again later."
}
```

- O login não é efetuado e nenhuma mensagem visível é apresentada ao usuário final.

---

## Resultado Esperado

- O sistema deve redirecionar corretamente para o fluxo de login do Facebook.
- Caso a integração esteja indisponível, apresentar uma mensagem clara e amigável ao usuário.

---

## Evidência

![Evidência do erro 403 ao tentar login com Facebook](![image](https://github.com/user-attachments/assets/756b0607-00c7-4aad-a57f-f88ee6f11565)
)

---

## Gravidade

**Alta** – A indisponibilidade do login social pode impactar significativamente a experiência dos usuários que utilizam o Facebook para autenticação.

---

## Recomendações

- Validar se a integração com a API do Facebook está ativa e corretamente configurada.

