# 📋 ANÁLISIS ESTRUCTURADO - García's Pizzas Web

**Fecha:** Abril 19, 2026  
**Sitio:** garciaspizzas.com  
**Ubicación:** Jilotepec, Estado de México

---

## 🎯 ESTRUCTURA GENERAL DE LA PÁGINA

### Archivos Principales:
```
📁 Pagina WEB OK Garcias/
├── index.html (3 MB) — Página principal
├── privacidad.html — Política de privacidad
├── terminos.html — Términos y condiciones
├── README.md — Descripción general
├── CNAME — Configuración de dominio
├── 📁 images/ — Carpeta con imágenes (WebP)
└── Documentos de soporte (docx)
```

---

## 🏗️ SECCIONES DE LA PÁGINA WEB (por orden)

### 1️⃣ **NAVBAR (Barra de Navegación)**
- **Ubicación:** Fija en la parte superior
- **Elementos:**
  - Logo con nombre "García's Pizzas" (amarillo)
  - Enlaces de navegación
  - Botón CTA rojo
- **Colores:** Negro (#110500) + Rojo (#ed1f25)
- **Fuente:** Oswald (encabezados)

**Posibles modificaciones:**
- [ ] Cambiar logo o tamaño
- [ ] Agregar/quitar enlaces de menú
- [ ] Modificar texto del botón CTA
- [ ] Cambiar colores de hover

---

### 2️⃣ **VIDEO BANNER + HERO SECTION**
- **Tipo:** Video de fondo de 16:9
- **Contenido:**
  - Título principal: "García's Pizzas" (con palabras en rojo y naranja)
  - Subtítulo: "Con el Sello que Nos Caracteriza"
  - Badge amarillo
  - Botones de acción
  - Animación de pizza flotante (lado derecho)
  - Fondo con degradado radial

**Posibles modificaciones:**
- [ ] Cambiar video de fondo
- [ ] Editar texto del héroe
- [ ] Agregar/quitar botones
- [ ] Cambiar animación de pizza
- [ ] Ajustar textos de la promoción

---

### 3️⃣ **STATS BAR (Barra de Estadísticas)**
- **Fondo:** Rojo (#ed1f25)
- **Contenido:** 4 estadísticas con números y etiquetas
  - Ej: "14+ Especialidades", "6 Tamaños", etc.

**Posibles modificaciones:**
- [ ] Actualizar números
- [ ] Cambiar etiquetas
- [ ] Agregar/quitar estadísticas

---

### 4️⃣ **SECCIÓN DE CARACTERÍSTICAS**
- **Fondo:** Negro oscuro (#0d0300)
- **Layout:** Grid de tarjetas (4 por fila)
- **Contenido:** Características con iconos, títulos y descripciones

**Características actuales:**
- Pizzas Artesanales
- Ingredientes Frescos
- Envío Rápido
- Atención al Cliente

**Posibles modificaciones:**
- [ ] Agregar/eliminar características
- [ ] Cambiar iconos (emojis)
- [ ] Editar textos descriptivos
- [ ] Cambiar número de columnas

---

### 5️⃣ **MENÚ - SELECCIÓN DE TAMAÑOS**
- **Fondo:** Crema (#fff8f0)
- **Contenido:** 
  - Título: "Elige tu Tamaño"
  - Grid de botones/opciones de tamaños
  - 6 tamaños: Personal, Pequeña, Mediana, Grande, Familiar, Extra

**Posibles modificaciones:**
- [ ] Cambiar número de tamaños
- [ ] Modificar nombres de tamaños
- [ ] Editar precios o descripciones
- [ ] Cambiar estilos visuales

---

### 6️⃣ **PIZZAS - CATÁLOGO DE PRODUCTOS**
- **Fondo:** Crema (#fff8f0)
- **Layout:** Grid de tarjetas (3-4 por fila en desktop)
- **Contenido por tarjeta:**
  - Imagen de la pizza
  - Nombre (fuente Bangers - cursiva)
  - Descripción
  - Precio
  - Botón "Ordenar"
  - Badge rojo (etiqueta especial)

**Pizzas actuales:**
- Hawaiana, Pepperoni, Carnes, Vegetariana, Especial, etc.

**Posibles modificaciones:**
- [ ] Agregar nuevas pizzas
- [ ] Cambiar nombre/descripción
- [ ] Actualizar precios
- [ ] Cambiar imágenes
- [ ] Editar etiquetas (badges)

---

### 7️⃣ **EMPANADAS**
- **Sistema:** Similar al de pizzas pero con controles de cantidad
- **Funcionalidad JavaScript:**
  - Botones +/- para cantidad
  - Cálculo automático de precio
  - Envío a WhatsApp con detalles

**Posibles modificaciones:**
- [ ] Agregar/eliminar empanadas
- [ ] Cambiar nombres y descripciones
- [ ] Ajustar precios
- [ ] Cambiar imágenes

---

### 8️⃣ **CAROUSEL DE ESPECIALIDADES**
- **Tipo:** Carrusel automático de imágenes
- **Imágenes:** 15 imágenes WebP
- **Comportamiento:**
  - Rota cada 5 segundos
  - Se puede pausar al pasar mouse
  - Click en imagen scrollea a selección de tamaños

**Imágenes actuales:**
- image_04.webp a image_29.webp

**Posibles modificaciones:**
- [ ] Cambiar imágenes del carrusel
- [ ] Ajustar velocidad (5000ms = 5 seg)
- [ ] Cambiar comportamiento al click

---

### 9️⃣ **COMBOS**
- **Fondo:** Negro (#1e0800)
- **Layout:** Grid de tarjetas de combos
- **Contenido por combo:**
  - Número grande (decorativo)
  - Título (amarillo)
  - Lista de ítems incluidos
  - Precio (rojo grande)
  - Botón "Ordenar"

**Combos actuales:**
- Combo 1-4 con diferentes productos

**Posibles modificaciones:**
- [ ] Agregar/eliminar combos
- [ ] Cambiar nombre y descripción
- [ ] Actualizar precio
- [ ] Cambiar items incluidos

---

### 🔟 **SECCIÓN DE DELIVERY**
- **Contenido:** Información de envíos
- **Datos mostrados:**
  - Zonas de cobertura
  - Tiempo estimado (35-45 min)
  - Monto mínimo ($120)
  - Costo del envío (gratis a partir de $120)

**Posibles modificaciones:**
- [ ] Cambiar información de entrega
- [ ] Actualizar zonas de cobertura
- [ ] Modificar tiempos estimados
- [ ] Cambiar montos mínimos

---

### 1️⃣1️⃣ **FORMULARIO DE PEDIDO**
- **ID:** purchaseForm
- **Contenido:**
  - Selector de tipo de pedido (Pizza/Combo/Empanada)
  - Formulario para datos del cliente
  - Integración WhatsApp

**Posibles modificaciones:**
- [ ] Cambiar campos del formulario
- [ ] Ajustar mensaje de WhatsApp
- [ ] Modificar número de WhatsApp (actualmente: 5215659941905)

---

### 1️⃣2️⃣ **FOOTER**
- **Contenido:**
  - Información de contacto
  - Horarios
  - Redes sociales
  - Links legales
  - Ubicación

**Posibles modificaciones:**
- [ ] Actualizar teléfono/WhatsApp
- [ ] Cambiar horarios
- [ ] Actualizar redes sociales
- [ ] Modificar dirección

---

## 🎨 PALETA DE COLORES ACTUAL

```css
--rojo: #ed1f25              /* Rojo principal (García's) */
--rojo-dark: #b01519         /* Rojo oscuro (hover) */
--amarillo: #faec00          /* Amarillo llamativo */
--naranja: #f6a419           /* Naranja acento */
--negro: #110500             /* Negro profundo */
--negro2: #1e0800            /* Negro secundario */
--crema: #fff8f0             /* Fondo crema claro */
```

**Posibles modificaciones:**
- [ ] Cambiar colores principales
- [ ] Ajustar tonos
- [ ] Crear tema alternativo

---

## 📝 TIPOGRAFÍAS UTILIZADAS

```css
--ff-d: 'Bangers' (cursiva)        /* Títulos principales */
--ff-h: 'Oswald' (sans-serif)      /* Encabezados */
--ff-b: 'Nunito' (sans-serif)      /* Body/párrafos */
```

**Posibles modificaciones:**
- [ ] Cambiar fuentes
- [ ] Ajustar tamaños de letra
- [ ] Modificar pesos (weights)

---

## 🔧 FUNCIONALIDADES JAVASCRIPT

### Funciones principales:
1. **Carrusel de especialidades** - Rotación automática
2. **Controles de cantidad** - Sumar/restar empanadas
3. **Cálculo de precios** - Actualiza en tiempo real
4. **Integración WhatsApp** - Abre chat con mensaje pre-llenado
5. **Scroll suave** - Navegación fluida entre secciones

**Posibles modificaciones:**
- [ ] Cambiar lógica de carrousel
- [ ] Modificar cálculo de precios
- [ ] Ajustar formato de mensaje WhatsApp
- [ ] Agregar nuevas funcionalidades

---

## 📊 ARCHIVOS ADJUNTOS Y REFERENCIAS

### Documentos de soporte:
- **Documentacion_Tecnica_Garcias_Pizzas.docx** - Documentación técnica
- **Guia_Seguridad_y_Mantenimiento.docx** - Guía de seguridad

### Imágenes:
- **Carpeta `/images/`** - Contiene todas las imágenes WebP
  - Fotos de pizzas
  - Imágenes del carrusel
  - Logo

---

## 🚀 RECOMENDACIONES DE MEJORA

### Prioridad Alta:
- [ ] Optimizar tamaño de archivo (actualmente 3 MB)
- [ ] Revisar carga de imágenes WebP
- [ ] Probar funcionalidad de WhatsApp en móvil
- [ ] Validar formularios antes de enviar

### Prioridad Media:
- [ ] Agregar más pizzas al catálogo
- [ ] Actualizar fotos de productos
- [ ] Mejorar descripciones de productos
- [ ] Agregar reseñas/testimonios

### Prioridad Baja:
- [ ] Agregar animaciones adicionales
- [ ] Crear versión dark mode
- [ ] Agregar chat en vivo
- [ ] Integrar sistema de reservas

---

## 📋 PRÓXIMOS PASOS

¿En qué sección te gustaría empezar a modificar?

1. **Contenido básico** (textos, nombres, precios)
2. **Imágenes** (cambiar fotos de productos)
3. **Colores y diseño** (paleta visual)
4. **Funcionalidad** (comportamiento JavaScript)
5. **Formulario de pedido** (cambiar campos)

**Escribe el número de la sección que quieres modificar o cuéntame qué específico quieres cambiar.**

---

*Análisis generado: 19 de Abril, 2026*
