# Análise de Limite de Crescimento: Airbnb (2022-2025)

Este projeto aplica conceitos de **Cálculo I (Limites)** e **Modelagem Matemática** para analisar o crescimento de reservas da Airbnb. O objetivo é identificar se a empresa ainda está em fase de crescimento exponencial ou se já apresenta sinais de saturação de mercado (comportamento logístico).

## 📋 Sobre o Projeto

No mundo real, nada cresce para sempre. Populações biológicas e bases de usuários de empresas tendem a seguir uma **Curva Logística** (em formato de "S").

Neste estudo, utilizamos dados reais dos relatórios financeiros da Airbnb para calcular o **Limite Matemático** ($L$) de reservas trimestrais, respondendo à pergunta:

> *"Se as tendências atuais continuarem, qual é o teto máximo de reservas que o Airbnb atingirá antes de estabilizar?"*

## 🧮 Fundamentação Matemática

A análise baseia-se no conceito de limite no infinito:

$$\lim_{t \to \infty} P(t) = L$$

Onde:

  * **$P(t)$**: População (Número de reservas) em função do tempo.
  * **$L$**: A Capacidade de Carga (o teto máximo do mercado).

A função utilizada para a regressão é a **Função Logística**:
$$P(t) = \frac{L}{1 + e^{-k(t-t_0)}}$$

## 📂 Fonte dos Dados

Os dados foram extraídos manualmente dos **Relatórios Trimestrais de Acionistas (Shareholder Letters)** da Airbnb, cobrindo o período de recuperação pós-pandemia até o presente:

  * [cite\_start]**Período:** 1º Trimestre de 2022 (Q1 22) até o 3º Trimestre de 2025 (Q3 25)[cite: 4849, 5945, 6572, 7203].
  * **Métrica:** *"Nights and Experiences Booked"* (Noites e Experiências Reservadas).
  * **Unidade:** Milhões.

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido em **Python** utilizando as seguintes bibliotecas:

  * **Pandas:** Organização e manipulação temporal dos dados.
  * **NumPy:** Cálculos numéricos e operações de array.
  * **Matplotlib:** Visualização de dados e plotagem da curva.
  * **SciPy (`curve_fit`):** Otimização para encontrar os parâmetros da curva logística ($L, k, t_0$).
  * **SymPy:** Cálculo simbólico do limite exato ($\lim_{t \to \infty}$).

## 🚀 Como Executar

1.  **Instale as dependências:**

    ```bash
    pip install numpy pandas matplotlib scipy sympy
    ```

2.  **Execute o script:**

    ```bash
    python nome_do_arquivo.py
    ```

3.  **O que o código faz:**

      * **Carrega os dados:** Insere os números reais de 2022 a 2025.
      * **Suavização (Média Móvel):** Aplica uma média de 4 períodos para remover a sazonalidade (o Airbnb tem picos naturais no verão e quedas no inverno). Isso revela a tendência real.
      * **Cálculo do Limite:** O algoritmo ajusta a curva logística aos dados suavizados para encontrar o valor de $L$.
      * **Visualização:** Gera um gráfico mostrando os dados históricos, a tendência e a projeção futura até a estabilização.

## 📊 Resultados Observados

Com base nos dados até o **Q3 2025**, o modelo identificou uma desaceleração no ritmo de crescimento anual, sugerindo a transição de uma fase exponencial para uma fase logística.

  * **Comportamento da Curva:** O gráfico projeta uma "parábola invertida" ou achatamento da curva.
  * [cite\_start]**Limite Calculado ($L$):** O modelo estima um teto teórico próximo de **\~161.8 Milhões** de reservas trimestrais[cite: 5707, 6572].

## 📜 Conclusão

A aplicação de Limites permitiu transformar dados brutos de negócios em uma previsão de longo prazo. O estudo sugere que, sem novas inovações disruptivas, o mercado atual da Airbnb tende a se estabilizar, confirmando a teoria de que o crescimento infinito é impossível em sistemas finitos.

-----

**Autor:** Eloá Juliana Lucindo Coradini.
**Data:** Novembro de 2025
