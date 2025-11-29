import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- 1. Dados Consolidados (2022 a 2025) ---
# Fonte: Relatórios de Acionistas Airbnb (Tabelas Históricas + Recentes)
data = {
    'Periodo': [
        'Q1-22', 'Q2-22', 'Q3-22', 'Q4-22',
        'Q1-23', 'Q2-23', 'Q3-23', 'Q4-23',
        'Q1-24', 'Q2-24', 'Q3-24', 'Q4-24',
        'Q1-25', 'Q2-25', 'Q3-25'
    ],
    'Noites_Milhoes': [
        102.1, 103.7, 99.7, 88.2,   # 2022
        121.1, 115.1, 113.2, 98.8,  # 2023
        132.6, 125.1, 122.8, 111.0, # 2024
        143.1, 134.4, 133.6         # 2025
    ]
}

df = pd.DataFrame(data)
df['Time_Index'] = np.arange(len(df))

# --- 2. Suavização da Curva ---
# Média Móvel de 4 trimestres para eliminar a sazonalidade forte do Airbnb
df['Tendencia'] = df['Noites_Milhoes'].rolling(window=4).mean()
df_clean = df.dropna()

# --- 3. Modelo Logístico (Cálculo do Limite) ---
def modelo_logistico(t, L, k, t0):
    return L / (1 + np.exp(-k * (t - t0)))

# Ajuste da curva aos dados suavizados
try:
    # Bounds ajudam o algoritmo a não se perder
    popt, pcov = curve_fit(modelo_logistico, df_clean['Time_Index'], df_clean['Tendencia'], 
                           p0=[200, 0.1, 10], maxfev=20000)
    L_calc = popt[0]
    msg = f"Limite Matemático (L): {L_calc:.1f} Milhões"
except:
    L_calc = 0
    popt = []
    msg = "Erro no ajuste (Dados insuficientes)"

# --- 4. Gráfico Final ---
plt.figure(figsize=(12, 7))

# Dados Brutos
plt.scatter(df['Time_Index'], df['Noites_Milhoes'], color='lightgray', s=60, label='Reservas Reais (Sazonal)')
plt.plot(df['Time_Index'], df['Noites_Milhoes'], color='lightgray', linestyle='--', alpha=0.5)

# Tendência Real (Suavizada)
plt.plot(df_clean['Time_Index'], df_clean['Tendencia'], 'o-', color='#FF5A5F', linewidth=3, label='Tendência de Crescimento')

# Projeção Matemática
if L_calc > 0:
    t_futuro = np.linspace(0, 25, 100)
    plt.plot(t_futuro, modelo_logistico(t_futuro, *popt), '--', color='#008489', linewidth=2, label='Modelo Logístico (Projeção)')
    plt.axhline(y=L_calc, color='black', linestyle=':', alpha=0.7, label=f'Teto Teórico: {L_calc:.0f}M')

plt.title(f'Airbnb: Análise de Saturação de Mercado (2022-2025)\n{msg}', fontsize=14)
plt.xlabel('Trimestres', fontsize=12)
plt.ylabel('Noites Reservadas (Média Móvel)', fontsize=12)
plt.xticks(df['Time_Index'], df['Periodo'], rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- 1. Dados Consolidados (2022 a 2025) ---
# Fonte: Relatórios de Acionistas Airbnb (Tabelas Históricas + Recentes)
data = {
    'Periodo': [
        'Q1-22', 'Q2-22', 'Q3-22', 'Q4-22',
        'Q1-23', 'Q2-23', 'Q3-23', 'Q4-23',
        'Q1-24', 'Q2-24', 'Q3-24', 'Q4-24',
        'Q1-25', 'Q2-25', 'Q3-25'
    ],
    'Noites_Milhoes': [
        102.1, 103.7, 99.7, 88.2,   # 2022
        121.1, 115.1, 113.2, 98.8,  # 2023
        132.6, 125.1, 122.8, 111.0, # 2024
        143.1, 134.4, 133.6         # 2025
    ]
}

df = pd.DataFrame(data)
df['Time_Index'] = np.arange(len(df))

# --- 2. Suavização da Curva ---
# Média Móvel de 4 trimestres para eliminar a sazonalidade forte do Airbnb
df['Tendencia'] = df['Noites_Milhoes'].rolling(window=4).mean()
df_clean = df.dropna()

# --- 3. Modelo Logístico (Cálculo do Limite) ---
def modelo_logistico(t, L, k, t0):
    return L / (1 + np.exp(-k * (t - t0)))

# Ajuste da curva aos dados suavizados
try:
    # Bounds ajudam o algoritmo a não se perder
    popt, pcov = curve_fit(modelo_logistico, df_clean['Time_Index'], df_clean['Tendencia'], 
                           p0=[200, 0.1, 10], maxfev=20000)
    L_calc = popt[0]
    msg = f"Limite Matemático (L): {L_calc:.1f} Milhões"
except:
    L_calc = 0
    popt = []
    msg = "Erro no ajuste (Dados insuficientes)"

# --- 4. Gráfico Final ---
plt.figure(figsize=(12, 7))

# Dados Brutos
plt.scatter(df['Time_Index'], df['Noites_Milhoes'], color='lightgray', s=60, label='Reservas Reais (Sazonal)')
plt.plot(df['Time_Index'], df['Noites_Milhoes'], color='lightgray', linestyle='--', alpha=0.5)

# Tendência Real (Suavizada)
plt.plot(df_clean['Time_Index'], df_clean['Tendencia'], 'o-', color='#FF5A5F', linewidth=3, label='Tendência de Crescimento')

# Projeção Matemática
if L_calc > 0:
    t_futuro = np.linspace(0, 100000000, 100)
    plt.plot(t_futuro, modelo_logistico(t_futuro, *popt), '--', color='#008489', linewidth=2, label='Modelo Logístico (Projeção)')
    plt.axhline(y=L_calc, color='black', linestyle=':', alpha=0.7, label=f'Teto Teórico: {L_calc:.0f}M')

plt.title(f'Airbnb: Análise de Saturação de Mercado (2022-2025)\n{msg}', fontsize=14)
plt.xlabel('Trimestres', fontsize=12)
plt.ylabel('Noites Reservadas (Média Móvel)', fontsize=12)
plt.xticks(df['Time_Index'], df['Periodo'], rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
plt.show()