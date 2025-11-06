# 🧾 Análisis de Ventas Gastronómicas con Python

## 📖 Descripción del proyecto
Este proyecto tiene como objetivo analizar los datos de ventas de un restaurante para obtener información útil sobre el rendimiento de productos, categorías y días de mayor actividad comercial.

El análisis fue desarrollado íntegramente en **Python**, utilizando librerías como **Pandas**, **Matplotlib** y **Seaborn**.  
Se parte de un archivo CSV con los registros diarios de ventas que incluyen fecha, producto, categoría, precio y cantidad.

A partir de esos datos se generan métricas e informes visuales que permiten responder preguntas como:
- ¿Qué productos son los más rentables?
- ¿Qué días se vende más?
- ¿Cuál es el promedio de ingresos por categoría?

---

## ⚙️ Tecnologías utilizadas
- **Python 3.x**
- **Pandas** → Limpieza, transformación y manipulación de datos  
- **NumPy** → Operaciones matemáticas y manejo eficiente de arreglos  
- **Matplotlib** → Creación de gráficos base y visualizaciones personalizadas  
- **Seaborn** →  Mejora estética y visualización estadística avanzada
- **Plotly** →  Creación de dashboards y gráficos interactivos para explorar los datos dinámicamente 

---

## 🧩 Estructura del proyecto

analisis_ventas_gastronomicas/
|---ventas.csv # Datos de ejemplo
|---analisis_ventas.py # Script principal del análisis
|---dashboard_interactivo.py #Script que muestra dashboard interactivo
|---README.md # Documentación del proyecto


---

## 🚀 Ejecución del proyecto
1. Clonar o descargar los archivos en una carpeta local.  
2. Instalar las librerías necesarias (si no las tenés):
   ```bash

   pip install pandas matplotlib seaborn numpy plotly

3. Ejecutar el script:

python analisis_ventas.py

4. Se mostrarán gráficos e información detallada en consola:

    - Producto más rentable
    - Día con mayores ingresos
    - Tendencia de ventas diarias

📊 Resultados esperados

Al ejecutar el análisis se generan visualizaciones que ayudan a comprender mejor el comportamiento de las ventas:
* Gráfico de ingresos por producto
* Tendencia de ingresos diarios
* Promedio de ingresos por categoría

Estas visualizaciones permiten detectar patrones de consumo y optimizar estrategias de venta.

<img width="4056" height="6697" alt="dashboard_ventas" src="https://github.com/user-attachments/assets/0089cdac-bccd-43f0-b33d-913968581eb3" />

<img width="1100" height="1200" alt="newplot" src="https://github.com/user-attachments/assets/67a11130-cb7c-4751-b135-c6b594f1c5eb" />

💡 Habilidades demostradas

* Análisis y limpieza de datos con Pandas
* Generación de insights y métricas descriptivas
* Creación de visualizaciones con Matplotlib y Seaborn
* Comunicación clara de resultados (Data Storytelling)

## 🔍 Insights del análisis de ventas

1. Ingresos totales por producto

El Sándwich de Jamón lidera en ingresos totales, consolidándose como el producto más rentable del menú.
El Café, aunque tiene un precio más bajo, logra una excelente performance gracias a su alta frecuencia de venta, contribuyendo significativamente al flujo de ingresos diarios.
Las Medialunas muestran un rendimiento estable, pero con margen de mejora. Podrían potenciarse mediante estrategias de venta cruzada, como combos o descuentos en horarios matutinos.

2. Tendencia diaria de ingresos

Se observa un crecimiento sostenido de los ingresos a lo largo de los días, alcanzando su punto máximo hacia el final del período analizado.
Este aumento sugiere una mayor afluencia de clientes hacia el fin de semana, posiblemente vinculada a hábitos de consumo o mayor tiempo de ocio.
Mantener un registro continuo de estas tendencias permitiría anticipar la demanda y optimizar la gestión de stock y personal en los días de mayor actividad.

3. Promedio de ingresos por categoría

La categoría Comidas presenta el mayor ingreso promedio, impulsada por el alto valor del Sándwich de Jamón.
Bebidas mantiene un promedio sólido y constante, lo que la posiciona como una fuente confiable de ingresos recurrentes.
Panadería, en cambio, tiene el menor promedio, indicando una oportunidad de crecimiento a través de ajustes de precio o estrategias promocionales.
En conjunto, los datos reflejan una estructura de ventas equilibrada, pero con espacio para incrementar la rentabilidad total mediante decisiones informadas.

## Conclusiones y próximos pasos

El análisis permitió identificar patrones clave en las ventas, destacando los productos más rentables y las categorías con mejor desempeño. Estos hallazgos ofrecen una base sólida para optimizar estrategias comerciales, ajustar precios y diseñar promociones más efectivas.
Como próximos pasos, se recomienda:

Ampliar el período de análisis para observar tendencias estacionales.
Incorporar variables adicionales como métodos de pago, horarios de mayor venta o ubicación.
Desarrollar un tablero de control más avanzado que integre métricas en tiempo real.

En conjunto, este proyecto demuestra cómo el uso de Python y el análisis de datos puede transformar la información en decisiones estratégicas y mejorar la rentabilidad de un negocio gastronómico.

## 🌎 Sales Analysis Insights (English Version)

1. Total Revenue by Product

The Ham Sandwich leads total revenue, making it the most profitable item on the menu.
Coffee, despite its lower price, performs very well thanks to its high sales frequency, providing steady daily income.
Croissants (Medialunas) show stable results but still have room for growth. Cross-selling strategies or breakfast combo offers could boost their performance.

2. Daily Revenue Trend

There is a consistent upward trend in revenue over the days, reaching its peak toward the end of the analyzed period.
This pattern suggests higher customer activity during weekends, possibly related to leisure habits or social gatherings.
Continuously monitoring these trends would help forecast demand and optimize stock and staff allocation on high-traffic days.

3. Average Revenue by Category

The Food category has the highest average revenue, driven mainly by the high value of the Ham Sandwich.
Beverages maintain a steady average, representing a reliable source of recurring income.
The Bakery category shows the lowest average, highlighting an opportunity to improve through pricing or promotional strategies.
Overall, the data reflects a balanced sales structure, with clear potential to enhance profitability through data-driven decisions.

## Conclusions and Next Steps

The analysis revealed key sales patterns, highlighting the most profitable products and the best-performing categories. These insights provide a strong foundation to optimize sales strategies, adjust pricing, and design more effective promotions.
Next steps could include:

Expanding the analysis period to identify seasonal trends.
Adding new variables such as payment methods, peak hours, or location data.
Building a more advanced dashboard that integrates real-time metrics.

Overall, this project demonstrates how Python and data analysis can turn raw information into actionable insights and enhance the profitability of a restaurant business.

## 👩‍💻 Autor

Julia Chiapello
Python Developer | Data Analyst | Backend Developer
📍 Córdoba, Argentina
✉️ julia.chiapello.it@gmail.com

Proyecto realizado como parte de mi portfolio profesional para mostrar mis habilidades en análisis de datos y visualización con Python.
