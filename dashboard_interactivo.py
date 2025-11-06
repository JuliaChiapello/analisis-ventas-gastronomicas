# === DASHBOARD INTERACTIVO DE VENTAS ===
# Autor: Julia Chiapello
# Descripción: Análisis interactivo de ventas gastronómicas con Plotly

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

# --- Cargar datos ---
df = pd.read_csv("ventas.csv", parse_dates=["fecha"])

# --- Limpieza básica ---
df["producto"] = df["producto"].str.strip()
df["categoria"] = df["categoria"].str.strip()

# --- Crear columna de ingresos ---
df["ingresos"] = df["precio"] * df["cantidad"]

# --- 1️⃣ Ingresos totales por producto ---
ventas_producto = df.groupby("producto")["ingresos"].sum().reset_index()

fig1 = px.bar(
    ventas_producto,
    x="producto",
    y="ingresos",
    color="producto",
    title="💰 Ingresos totales por producto",
    text_auto=".2s"
)

# --- 2️⃣ Tendencia de ingresos diarios ---
ventas_diarias = df.groupby("fecha")["ingresos"].sum().reset_index()

fig2 = px.line(
    ventas_diarias,
    x="fecha",
    y="ingresos",
    markers=True,
    title="📈 Tendencia diaria de ingresos"
)
fig2.update_traces(line_color="orange", line_width=3)

# --- 3️⃣ Promedio de ingresos por categoría ---
promedio_categoria = df.groupby("categoria")["ingresos"].mean().reset_index()

fig3 = px.bar(
    promedio_categoria,
    x="categoria",
    y="ingresos",
    color="categoria",
    title="📊 Promedio de ingresos por categoría",
    text_auto=".2s"
)

# --- Combinar todos los gráficos en un solo dashboard ---
from plotly import graph_objects as go

dashboard = make_subplots(
    rows=3, cols=1,
    subplot_titles=(
        "💰 Ingresos totales por producto",
        "📈 Tendencia diaria de ingresos",
        "📊 Promedio de ingresos por categoría"
    )
)

# Agregar trazas desde cada figura
for trace in fig1.data:
    dashboard.add_trace(trace, row=1, col=1)

for trace in fig2.data:
    dashboard.add_trace(trace, row=2, col=1)

for trace in fig3.data:
    dashboard.add_trace(trace, row=3, col=1)

# --- Ajustar diseño general ---
dashboard.update_layout(
    height=1200,
    width=1100,
    title_text="Análisis Interactivo de Ventas Gastronómicas 🍽️",
    title_font=dict(size=24, color="#333"),
    template="plotly_white",
    showlegend=False
)

# --- Mostrar en navegador ---
dashboard.show()
