
# 💼 Controle de Aumento e Redução Salarial

> 🇧🇷 Um programa em Python para calcular aumentos e reduções salariais de forma simples, prática e com formatação brasileira.  
> 🇺🇸 A Python program to calculate salary increases and reductions with Brazilian currency formatting.

## 🧠 Objetivo

O objetivo deste projeto é criar um sistema simples de controle salarial para funcionários. Ele permite calcular aumentos e reduções de salário com base em uma porcentagem informada pelo usuário, aceitando valores monetários no formato brasileiro (com vírgula como separador decimal e ponto como separador de milhar). O programa também formata todos os valores de saída de forma clara e padronizada.

## 🎯 Funcionalidades

- 📋 Menu interativo com duas opções:
  - `1` Aumento de salário
  - `2` Redução de salário
- 💰 Entrada de salário no formato brasileiro, como `1.320,98`
- 📉 Entrada de porcentagens com vírgula decimal, como `10,5`
- 🧮 Cálculo automático do valor de aumento ou redução
- 💵 Exibição do novo salário formatado corretamente
- 🖨️ Detalhamento completo na saída para clareza do usuário

## ▶️ Como usar

1. **Clone o repositório para sua máquina:**

   ```bash
   git clone https://github.com/BrunoRodrigues27/Aumento_reducao_salario.git
   cd Projeto_aumento_reducao_salario
   ```

2. **Certifique-se de que o Python 3 está instalado.**

3. **Execute o script no terminal ou no PyCharm**  
   Digite o seguinte comando:

   ```bash
   python main.py
   ```

   Ou, no PyCharm, apenas clique em **Run** no arquivo `main.py`.

4. **Siga as instruções do menu:**  
   Você verá um menu como este:

   ```
   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
   |                  Controle do Funcionário                  |
   |-----------------------------------------------------------|
   | 1 - Aumento de Salário                                    |
   | 2 - Redução de Salário                                    |
   |-----------------------------------------------------------|
   ```

   Digite:
   - `1` para **Aumento de Salário**
   - `2` para **Redução de Salário**

5. **Preencha as informações:**  
   - Nome do funcionário
   - Salário antigo (ex: `2.345,80`) — no **formato brasileiro** com vírgula
   - Porcentagem do aumento ou redução (ex: `12,5`)

6. **Veja o resultado formatado com todos os detalhes:**  
   O programa exibirá os valores calculados e formatados corretamente com `R$`, vírgula decimal, e ponto de milhar.

## 📌 Exemplo de execução real

```text
C:\Users\Bruno\PycharmProjects\Projeto_aumento_reducao_salario\.venv\Scripts\python.exe C:\Users\Bruno\PycharmProjects\Projeto_aumento_reducao_salario\main.py 

|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                  Controle do Funcionário                  |
|-----------------------------------------------------------|
| 1 - Aumento de Salário                                    |
| 2 - Redução de Salário                                    |
|-----------------------------------------------------------|
| Escolha: 1
|-----------------------------------------------------------|
| Nome do funcionário: João da Silva Oliveira dos Santos
|-----------------------------------------------------------|
|             informações pessoais do funcionário           |
|-----------------------------------------------------------|
| Funcionário: João da Silva Oliveira dos Santos
|-----------------------------------------------------------|
|-----------------------------------------------------------|
|                  Menu de aumento salarial                 |
|-----------------------------------------------------------|
| Salário antigo: R$2.345,80
| Porcentagem do aumento: 12,5
|-----------------------------------------------------------|
|-----------------------------------------------------------|
|                    Detalhes pós aumento                   |
|-----------------------------------------------------------|
| Salário antigo: R$2.345,80
| Porcentagem do aumento: 12,5%
| Valor do aumento: R$293,23
| Salário novo: R$2.639,03
|___________________________________________________________|
```

## 🛠️ Tecnologias usadas

- Python 3.x
- Funções (`def`) para organização do código
- Módulo `time` com `sleep()` para criar pausas suaves
- Conversão de strings para `float` com `replace()`
- Formatação de strings com `format()` para exibir valores em reais
- Lógica condicional com `if`, `elif` e `return`

## 📂 Estrutura do projeto

```
Projeto_aumento_reducao_salario/
│
├── main.py                # Código-fonte principal
├── README.md              # Este arquivo de documentação
└── .venv/                 # Ambiente virtual Python (opcional)
```

## 🌍 Suporte ao formato brasileiro

Este programa aceita entrada e saída de valores no **formato monetário brasileiro**, ou seja:
- Separador de milhar: ponto `.` → Ex: `1.234,56`
- Separador decimal: vírgula `,`
- Aceita porcentagens com vírgula (ex: `7,5`) e também com ponto (ex: `7.5`)

Todos os valores são convertidos para `float` internamente, processados, e depois reformatados para o padrão BR na saída com `R$` e dois dígitos decimais.

## 🧑‍💻 Autor

Feito por **Bruno Rodrigues**  

```
## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
