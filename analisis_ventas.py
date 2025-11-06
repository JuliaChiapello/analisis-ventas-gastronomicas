import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuración general de gráficos
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("coolwarm")

# === 1. CARGA DE DATOS ===
df = pd.read_csv("ventas.csv")

# === 2. LIMPIEZA DE DATOS ===
# Normalizar nombres de columnas y valores (el CSV de ejemplo tiene espacios)
df.columns = df.columns.str.strip()
# Quitar espacios en strings de producto y categoria
df['producto'] = df['producto'].astype(str).str.strip()
df['categoria'] = df['categoria'].astype(str).str.strip()
df['fecha'] = pd.to_datetime(df['fecha'])
# Asegurarnos que precio y cantidad sean numéricos
df['precio'] = pd.to_numeric(df['precio'], errors='coerce').fillna(0)
df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce').fillna(0)
df['ingreso_total'] = df['precio'] * df['cantidad']

# === 3. ANÁLISIS EXPLORATORIO ===
print("=== Primeras filas del dataset ===")
print(df.head(), "\n")

print("=== Información general ===")
print(df.info(), "\n")

print("=== Resumen estadístico ===")
print(df.describe(), "\n")

# === 4. INSIGHTS PRINCIPALES (cálculos) ===
ventas_por_producto = df.groupby('producto')['ingreso_total'].sum().sort_values(ascending=False)
ventas_por_dia = df.groupby('fecha')['ingreso_total'].sum().sort_index()
producto_mas_vendido = ventas_por_producto.idxmax()
total_ingresos = df['ingreso_total'].sum()

# Promedio de ingreso por categoria (asegurarnos que exista la columna)
if 'categoria' in df.columns:
    promedio_categoria = df.groupby('categoria')['ingreso_total'].mean().sort_values(ascending=False)
else:
    promedio_categoria = pd.Series(dtype=float)

print(f"Ingreso total del período: ${total_ingresos:,.2f}")
print(f"Producto más rentable: {producto_mas_vendido}")
print(f"Día con mayor venta: {ventas_por_dia.idxmax().date()}\n")

# === VISUALIZACIÓN  ===
# --- Configuración general ---
sns.set(style="whitegrid", font_scale=1.1)

# Figura grande con espacio vertical
fig, axes = plt.subplots(3, 1, figsize=(16, 24))

# --- Título general ---
fig.suptitle(
    "Análisis de Ventas Gastronómicas",
    fontsize=22,
    fontweight='bold',
    color='#2c3e50',
    y=0.97  # bajamos un poco para dejar más aire arriba
)

# --- 1. Ingresos por producto ---
sns.barplot(x=ventas_por_producto.index, y=ventas_por_producto.values, palette="Blues_d", ax=axes[0])
axes[0].set_title("Ingresos totales por producto", fontsize=14, loc='left', pad=10, color='#34495e')  
axes[0].set_xlabel("")
axes[0].set_ylabel("Ingresos (ARS)")
axes[0].tick_params(axis='x', rotation=0)  # etiquetas rectas

# --- 2. Tendencia diaria de ingresos ---
sns.lineplot(x=ventas_por_dia.index, y=ventas_por_dia.values, marker='o', color='#e67e22', linewidth=2, ax=axes[1])
axes[1].set_title("Tendencia diaria de ingresos", fontsize=14, loc='left', pad=10, color='#34495e')
axes[1].set_xlabel("Fecha")
axes[1].set_ylabel("Ingresos (ARS)")
axes[1].grid(alpha=0.3)
axes[1].tick_params(axis='x', rotation=0)

# --- 3. Promedio de ingresos por categoría ---
sns.barplot(x=promedio_categoria.index, y=promedio_categoria.values, palette="Greens_d", ax=axes[2])
axes[2].set_title("Promedio de ingresos por categoría", fontsize=14, loc='left', pad=10, color='#34495e')
axes[2].set_xlabel("")
axes[2].set_ylabel("Promedio (ARS)")
axes[2].tick_params(axis='x', rotation=0)

# --- Ajustes de espaciado ---
plt.subplots_adjust(
    top=0.88,     # más espacio entre el título general y el primer gráfico
    hspace=0.70,  # separación equilibrada entre gráficos
    bottom=0.06
)

# Guardar la figura completa
plt.savefig("dashboard_ventas.png", dpi=300, bbox_inches='tight')

plt.show()
