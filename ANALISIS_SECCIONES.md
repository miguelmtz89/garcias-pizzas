# 📊 ANÁLISIS COMPLETO - Garcia's Pizzas Website

---

## 🏗️ ESTRUCTURA GENERAL DE LA PÁGINA

Tu sitio web tiene **9 secciones principales** + elementos técnicos (meta, scripts, CSS)

---

## 📍 SECCIONES DETALLADAS

### 1️⃣ **HEAD / METADATOS** (Líneas 1-18)
**Ubicación:** Arriba de todo en el HTML  
**Contenido:**
- Título: "Garcia's Pizzas — Con el Sello que Nos Caracteriza"
- Descripción SEO
- Keywords para buscadores
- Meta tags y Open Graph
- Fuentes de Google (Bangers, Oswald, Nunito)
- Schema JSON para restaurantes
- Teléfono: (761) 688 1727

**Elementos modificables:**
- Título de la página
- Descripción meta
- Keywords
- Nombre del negocio
- Redes sociales (Facebook, Instagram)

---

### 2️⃣ **SECCIÓN HERO** (Línea 879-910)
**ID:** `#inicio`  
**Clase:** `.hero`  
**Contenido:**
- Imagen/fondo heroico
- Título: "La Mejor Pizza de la Ciudad"
- Con span rojo (r) y naranja (o)
- Botón "Pedir Ahora" (rojo)

**Elementos modificables:**
- Texto principal
- Colores del texto resaltado
- Botones de CTA
- Fondo/imagen

---

### 3️⃣ **EL SELLO GARCIA** (Línea 911-926)
**Clase:** `.feat-bg`  
**Contenido:**
- Título: "El Sello Garcia"
- Características (probablemente):
  - Ingredientes frescos
  - Horno de leña
  - Receta familiar
  - Envío rápido

**Elementos modificables:**
- Título
- Descripciones de características
- Iconos/imágenes
- Textos de beneficios

---

### 4️⃣ **CONOCE NUESTRAS PIZZAS - CAROUSEL** (Línea 927-956)
**ID:** `#nuestras-especialidades`  
**Clase:** `.spec-carousel-bg`  
**Contenido:**
- Carrusel automático de pizzas
- Botones prev/next (❮ ❯)
- Se pausa al pasar el ratón
- Imágenes de pizzas especiales

**Elementos modificables:**
- Título
- Imágenes del carrusel
- Velocidad de rotación
- Pizzas mostradas

**JavaScript:**
- `pauseCarousel()` - pausa al hover
- `resumeCarousel()` - reanuda
- `prevCarousel()` / `nextCarousel()` - navegación

---

### 5️⃣ **TAMAÑOS Y PRECIOS - ABAJO DEL CAROUSEL** ⭐ (Línea 942-952)
**ID:** None  
**Clase:** `.size-box`  
**Contenido:**
- Título: "TAMAÑOS Y PRECIOS"
- 6 tamaños:
  - Mini: 4 rebanadas - $80
  - Chica: 6 rebanadas - $110
  - Mediana: 8 rebanadas - $140
  - Grande: 10 rebanadas - $170
  - Familiar: 12 rebanadas - $210
  - Jumbo: 16 rebanadas - $240
- Nota: Queso extra y ingrediente extra ($15)

**Estatus:** ✅ Aquí está (abajo del carousel)

---

### 6️⃣ **NUESTRAS ESPECIALIDADES / REALIZA TU PEDIDO** (Línea 957-1400)
**ID:** `#menu`  
**Clase:** `.menu-bg`  
**Subtítulo:** "Nuestras especialidades"  
**Título:** "Selecciona tu Pizza"  
**Nota:** "(PIDE TU PIZZA ONLINE te llega mas rapido)"

#### **Componentes dentro:**

#### 📋 **A) BARRA DE PROGRESO** (Línea 967-993)
- 6 pasos:
  1. **Tipo** - ¿Qué deseas? (Pizza/Combo/Empanadas)
  2. **Selección** - Selecciona sabor
  3. **Sabor** - Información del sabor
  4. **Bebida** - Añade bebida
  5. **Datos** - Nombre, teléfono, dirección
  6. **Confirmar** - Resumen y envío

#### 🍕 **B) SELECTOR DE TIPO DE PEDIDO** (Línea 1001-1010)
- **Pizza** (por defecto)
- **Combos** (1 Familiar + 1 Mediana, etc.)
- **Empanadas** (scroll a sección)

#### 💰 **C) AREA DE COMBOS** (Línea 1013-1115)
**ID:** `#comboSelectArea`  
- Combo 1: 1 Familiar (12 reb.) + 1 Mediana (8 reb.) = $330
- Combo 2: 1 Jumbo (16 reb.) + 1 Mediana (8 reb.) = $350
- Combo 3: 2 Familiares (12 reb. c/u) = $390
- Combo 4: 2 Jumbos (16 reb. c/u) = $440
- Selectores para sabores de cada pizza del combo

#### 📏 **D) SELECTOR DE TAMAÑO** (Línea 1116-1126)
**ID:** `#sizeRow`  
**Elemento:** `<select id="sizeSelect">`  
**Opciones (hardcodeadas):**
- Mini (4 rebanadas) - $80
- Chica (6 rebanadas) - $110
- Mediana (8 rebanadas) - $140
- Grande (10 rebanadas) - $170
- Familiar (12 rebanadas) - $210
- Jumbo (16 rebanadas) - $240

**Función:** `updatePrice()` - actualiza cálculo

#### 🍕 **E) SELECTOR DE SABOR/PIZZA** (Línea 1132-1278)
**ID:** `#pizzaFlavorRow`  
**Contenedor:** `#pizzaSelection`  
**Pizzas disponibles:**
1. Pepperoni - $0 extra
2. Hawaiana - $0 extra
3. Vegetariana - $0 extra
4. Carnívora - $20 extra
5. Suprema - $25 extra
6. BBQ - $20 extra
7. Cuatro Quesos - $15 extra
8. Al Pastor - $20 extra
9. Española - $15 extra
10. Mexicana - $20 extra
11. De la Casa - $30 extra
12. Premium Mix - $35 extra
13. Atun - $20 extra
14. Champiñones - $10 extra

#### 🥤 **F) SELECTOR DE BEBIDAS** (Línea 1279-1330)
**Para Pizzas (ID: `#drinkRowPizza`):**
- Sin bebida (seleccionado por defecto)
- Jarritos 2L - $45
- Coca-Cola 3L - $65

**Para Combos (ID: `#drinkRowCombo`):**
- Similar con opciones de bebidas

#### 📝 **G) FORMULARIO DE DATOS** (Línea 1331-1348)
- **Nombre** (ID: `#nameInput`) - Ej: "Juan García"
- **Teléfono** (ID: `#phoneInput`) - Ej: "7616881727"
- **Dirección** (ID: `#addressInput`) - Calle, número, referencias

#### 📦 **H) RESUMEN DEL PEDIDO** (Línea 1349-1378)
**ID:** `#orderSummary`  
**Elementos:**
- Combo seleccionado
- Sabores (si aplica)
- Tamaño
- Pizza
- Bebida
- Costo de delivery
- **TOTAL**

#### ✅ **I) MODAL DE CONFIRMACIÓN** (Línea 1387-1399)
**ID:** `#confirmationModal`  
- Muestra resumen final
- Opción de enviar por WhatsApp

---

### 7️⃣ **NUESTRAS EMPANADAS** (Línea 1401-1580)
**ID:** `#empanadas`  
**Clase:** `.emp-bg`  
**Subtítulo:** "También tenemos 🍟"  
**Título:** "Nuestras Empanadas"  

**Contenido:**
- Tarjetas de empanadas (pizza-card)
- Contador de cantidad (aumentar/disminuir)
- Precio unitario
- Botón "Pedir" (rojo)
- Enlace directo a WhatsApp

**Empanadas (probablemente):**
- De queso
- De carne
- De pollo
- De verduras
- Etc.

**Elementos modificables:**
- Nombres de empanadas
- Precios unitarios
- Imágenes
- Descripciones

**JavaScript:**
- `increaseQty()` - aumentar cantidad
- `decreaseQty()` - disminuir cantidad
- `updateEmpanadaPrice()` - actualizar precio
- `orderWithQty()` - enviar a WhatsApp

---

### 8️⃣ **NUESTROS COMBOS** (Línea 1582-1613)
**ID:** `#combos`  
**Clase:** `.combos-bg`  
**Título:** "Nuestros Combos"  

**Contenido:**
- Tarjetas de combos (combo-card)
- Cada combo muestra:
  - Número (Combo 1, 2, 3, 4)
  - Descripción (pizzas incluidas y cantidades)
  - Imagen
  - Precio
  - Botón "Pedir este combo" (verde WhatsApp)

**Combos:**
- Combo 1: 1 Familiar + 1 Mediana = $330 + bebida
- Combo 2: 1 Jumbo + 1 Mediana = $350 + bebida
- Combo 3: 2 Familiares = $390 + bebida
- Combo 4: 2 Jumbos = $440 + bebida

**Elementos modificables:**
- Nombre/descripción de combos
- Precios
- Imágenes
- Bebidas incluidas

**Banner Delivery:**
- "Delivery a toda la ciudad"
- "Sin costo extra!"

---

### 9️⃣ **CONTACTO & HORARIOS** (Línea 1616-1638)
**ID:** `#contacto`  
**Clase:** `.con-bg`  
**Título:** "Contacto & Horarios"  

**Contenido (probablemente):**
- Teléfono: (761) 688 1727
- Horarios: Lunes a domingo 11:00 AM - 9:00 PM
- Email
- Ubicación
- Redes sociales (Facebook, Instagram)

**Elementos modificables:**
- Teléfono
- Horarios
- Correo
- Links de redes sociales

---

### 🔟 **UBICACIÓN / MAPA** (Línea 1639-fin)
**ID:** `#ubicacion`  
**Clase:** `.map-bg`  
**Título:** "Encuentranos Facilmente"  

**Contenido:**
- Mapa incrustado (probablemente Google Maps)
- Dirección: "Andres Molina Enriquez 121, Jilotepec de Molina Enriquez, Estado de Mexico, 54240"

**Elementos modificables:**
- Coordenadas del mapa
- Dirección mostrada
- Descripción de ubicación

---

## 🎨 ELEMENTOS GLOBALES / CSS

### Colores principales:
- **Rojo:** `--rojo` (#ed1f25 aprox.)
- **Naranja:** `--naranja`
- **Negro:** `--negro`
- **Grises:** Varios tonos

### Tipografía:
- **Display/Títulos:** Bangers, Oswald
- **Cuerpo:** Nunito
- **Otros:** Oswald (para headers)

### Clases reutilizables:
- `.size-box` - Contenedor de tamaños
- `.size-grid` - Grid de tamaños
- `.pizza-card` - Tarjeta de producto
- `.btn-red` - Botón rojo
- `.btn-wa` - Botón WhatsApp (verde)
- `.carousel-*` - Carrusel
- `.form-*` - Elementos de formulario

---

## ⚙️ FUNCIONALIDADES JAVASCRIPT

### Carrusel:
- `pauseCarousel()` / `resumeCarousel()` / `prevCarousel()` / `nextCarousel()`

### Formulario de pedido:
- `setOrderType(type)` - Selecciona tipo de pedido
- `selectCombo()` - Selecciona combo
- `updatePrice()` - Actualiza precio total
- `nextStep(step)` - Navega entre pasos
- `selectDrink()` - Selecciona bebida
- `submitForm()` - Envía pedido

### Empanadas:
- `increaseQty()` / `decreaseQty()` - Cantidad
- `updateEmpanadaPrice()` - Precio
- `orderWithQty()` - Envío WhatsApp

### Combos:
- `goToComboOrder()` - Navega a formulario
- `selectCombo()` - Selecciona combo

### Utilidades:
- `goToSizeSection()` - Scroll a selector de tamaño

---

## 🔗 INTEGRACIONES EXTERNAS

### WhatsApp:
- API de WhatsApp para mensajes
- Número: +52 1 5659941905 (para empanadas)
- URLs dinámicas con encodeURIComponent()

### Google Maps:
- Mapa incrustado en sección de ubicación

### Google Fonts:
- Bangers (títulos creativos)
- Oswald (headers modernos)
- Nunito (cuerpo legible)

### Redes Sociales:
- Facebook: facebook.com/garcias.pizzas
- Instagram: instagram.com/garcias_pizza_jilo/

---

## 📝 NOTAS TÉCNICAS

1. **Responsividad:** Media queries en CSS (móvil, tablet, desktop)
2. **Accesibilidad:** Schema JSON para restaurantes
3. **SEO:** Meta tags completas, keywords
4. **Performance:** Imágenes probablemente en WebP
5. **Interactividad:** JavaScript vanilla (sin frameworks)

---

## ✨ CAMBIOS RECIENTES (QUE HEMOS HECHO)

1. ✅ Eliminamos el texto "Haz clic en una pizza para ver tamaños y precios"
2. ✅ Agregamos sección de "TAMAÑOS Y PRECIOS" abajo del carousel
3. ✅ Eliminamos sección de "TAMAÑOS Y PRECIOS" de "Nuestras especialidades"

---

## 🎯 SIGUIENTES PASOS

Ahora puedes elegir qué sección modificar:

- **Cambiar textos** (títulos, descripciones)
- **Actualizar precios** (pizzas, combos, empanadas)
- **Modificar colores** (tema)
- **Agregar/quitar pizzas** (sabores)
- **Cambiar horarios/contacto**
- **Actualizar redes sociales**
- **Modificar imágenes**
- **Cambiar estructura** (layout de secciones)

¿Cuál sección te gustaría modificar primero?
