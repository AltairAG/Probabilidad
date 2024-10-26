# Instalar ggplot2 si no está instalado
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}

# Cargar la librería necesaria
library(ggplot2)

# Leer el archivo CSV (asegúrate de que la ruta es correcta)
datos <- read.csv("conteoPR.csv")

# Generar el histograma con ajustes en el eje Y
ggplot(datos, aes(x = reorder(Palabra_Reservada, -Frecuencia), y = Frecuencia)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Frecuencia de Palabras Reservadas en el Archivo", 
       x = "Palabra Reservada", 
       y = "Frecuencia") +
  scale_y_continuous(breaks = seq(0, max(datos$Frecuencia), by = 50)) + # Cambiar intervalos a 50
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
