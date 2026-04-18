# 🥟 EMPANADAS - Implementación Completa

## ✅ ESTADO: COMPLETADO

Se ha implementado la sección de **EMPANADAS** con venta por unidad y spinner +/- por tarjeta.

---

## 📦 Archivo Principal

**`pag_web_2026_completa.html`** ✨ (39 MB)
- Página web completa con Pizzas + Combos + **Empanadas**
- Listo para usar en producción
- Todas las imágenes incrustadas (pizzas + combos + empanadas)

---

## 🎯 ¿Qué Se Implementó?

### 1️⃣ Tercer Botón Selector
```
┌──────────────────┬──────────────────┬──────────────────┐
│ 🍕 Pizza         │ 🎉 Combo         │ 🥟 Empanadas     │
│ Individual       │ (Promoción)      │ ✨ NUEVO         │
└──────────────────┴──────────────────┴──────────────────┘
```

### 2️⃣ Catálogo de Empanadas (Igual a Pizza Individual)
- **Tarjetas:** 260px × auto (idénticas a pizzas)
- **Imágenes:** 160px de alto (misma proporción)
- **Ubicación:** Mismo lugar que "Selecciona tu Sabor de Pizza"
- **Grid:** 3-4 columnas responsive

```
Cuando selecciona "🥟 Empanadas":
┌────────────────────────────────────────────────────┐
│ Selecciona tus Empanadas                           │
├────────────────────────────────────────────────────┤
│                                                    │
│  ┌──────────────┐ ┌──────────────┐               │
│  │   Imagen     │ │   Imagen     │               │
│  │   160px      │ │   160px      │ ...           │
│  │              │ │              │               │
│  │ Hawaiana     │ │Hawaiana Esp. │               │
│  │ Jamón, Piña  │ │ Premium      │               │
│  │ Queso        │ │ +$80         │               │
│  │              │ │              │               │
│  │ $70          │ │              │               │
│  │              │ │              │               │
│  │ [−] 0 [+]    │ │ [−] 0 [+]    │               │
│  └──────────────┘ └──────────────┘               │
│                                                    │
│  [Más empanadas...]                              │
│                                                    │
└────────────────────────────────────────────────────┘
```

### 3️⃣ Sistema de Venta por Unidad
- **Spinner +/- por tarjeta**
- **Sin límite de cantidad**
- **Cada cliente selecciona la cantidad que desea**

```
Para cada empanada:
[−] Cantidad [+]

Ejemplo:
[−] 2 [+] ← Usuario puede tener 2 Hawaianas
[−] 1 [+] ← 1 Hawaiana Especial
[−] 3 [+] ← 3 Carnes Mixtas
```

### 4️⃣ 7 Sabores Disponibles

| # | Nombre | Descripción | Precio |
|----|--------|-------------|--------|
| 1 | **Hawaiana** | Jamón, Piña y Queso — horneada al momento, dulce y deliciosa. | $70 |
| 2 | **Hawaiana Especial** | Jamón, Piña, Queso y Cereza — la versión premium con toque irresistible. | $80 |
| 3 | **Jamón, Queso y Jalapeño** | Jamón, Queso y Jalapeño — clásica y perfecta para botanear. | $70 |
| 4 | **Chorizo, Queso y Jalapeño** | Chorizo, Queso y Jalapeño — sabor intenso con un toque picante. | $70 |
| 5 | **Champiñón, Queso y Jalapeño** | Champiñón, Queso y Jalapeño — opción ligera y llena de sabor. | $70 |
| 6 | **Carnes Mixtas** | Jamón, salchicha, pepperoni y chorizo — la más completa y generosa. | $80 |
| 7 | **4 Ingredientes** | Escoge tus 4 ingredientes favoritos — ¡diseña tu propia empanada! | $80 |

### 5️⃣ Imágenes Reales
- **2 imágenes base64** extraídas del archivo original
- **Alternadas** entre las 7 empanadas
- Imagen 1: Empanadas 1, 3, 5, 7
- Imagen 2: Empanadas 2, 4, 6

### 6️⃣ Resumen del Pedido

```
🥟 EMPANADAS
  • Hawaiana: 2 unidades - $140
  • Carnes Mixtas: 1 unidad - $80
  • Chorizo, Queso y Jalapeño: 3 unidades - $210

🥤 Bebida: Coca Cola 2L (opcional)

🛵 Delivery: Gratis

💰 Total: $430
```

### 7️⃣ Bebida Opcional
- Mismo selector que pizzas
- No es obligatoria
- Precios incluidos en total

---

## 🔄 Flujo Completo

```
Usuario abre página
        ↓
Selecciona "🥟 Empanadas"
        ↓
Ve catálogo de 7 empanadas (como pizzas)
        ↓
Para cada empanada:
  • Ve imagen (160px)
  • Ve nombre y descripción
  • Ve precio unitario
  • Tiene spinner +/- para cantidad
        ↓
Usuario selecciona cantidades:
  2x Hawaiana
  1x Carnes Mixtas
  3x Chorizo, Queso y Jalapeño
        ↓
Resumen actualiza en tiempo real:
  "Hawaiana: 2 unidades - $140"
  "Carnes Mixtas: 1 unidad - $80"
  "Chorizo, Queso y Jalapeño: 3 unidades - $210"
        ↓
(Opcional) Selecciona bebida
        ↓
Completa datos:
  - Nombre
  - Teléfono
  - Dirección
        ↓
Haz click en "📞 CONFIRMAR PEDIDO VÍA WHATSAPP"
        ↓
WhatsApp abre con mensaje:

"Mi pedido es de la página web

🥟 EMPANADAS
  • Hawaiana: 2 unidades - $140
  • Carnes Mixtas: 1 unidad - $80
  • Chorizo, Queso y Jalapeño: 3 unidades - $210
🥤 Bebida: Coca Cola 2L
🛵 Delivery: Gratis
💰 Total: $430

👤 Nombre: Miguel
📱 Teléfono: 1234567890
📍 Dirección: Calle Principal 123
..."
```

---

## 💻 Implementación Técnica

### CSS Agregado
```css
.empanada-counter {
    /* Badge con cantidad en tarjeta */
}
.empanada-counter-controls {
    /* Contenedor de botones +/- */
}
.empanada-counter-btn {
    /* Botones − y + */
}
.empanada-counter-input {
    /* Input de cantidad */
}
```

### JavaScript Nuevo

#### Variables Globales
```javascript
var empanadaFlavors = [...]           // Array de 7 sabores
var empanadaPrices = {...}            // Precios por sabor
var empanadaDescriptions = {...}      // Descripciones
var empanadaImages = {...}            // 2 imágenes base64
var selectedEmpanadas = {}            // {sabor: cantidad}
var selectedEmpanadaBeverage = ''     // Bebida seleccionada
var selectedEmpanadaBeveragePrice = 0 // Precio bebida
```

#### Funciones Nuevas
- `buildEmpanadaCards()` - Genera las 7 tarjetas
- `updateEmpanadaQuantity()` - Suma/resta cantidad
- `setEmpanadaQuantity()` - Establece cantidad exacta
- `resetEmpanadas()` - Limpia selecciones
- `selectDrinkEmpanada()` - Maneja bebidas

#### Funciones Modificadas
- `setOrderType()` - Ahora soporta `'empanadas'`
- `updatePrice()` - Calcula total de empanadas
- `submitOrder()` - Envía empanadas por WhatsApp

---

## 🧪 Pruebas Recomendadas

### ✅ Test 1: Ver Botón y Catálogo
```
1. Abre: pag_web_2026_completa.html
2. Scroll a "🛒 Realiza tu Pedido Online"
3. Haz click en "🥟 Empanadas"
4. Verifica:
   ✓ Se ocultan pizzas y combos
   ✓ Aparecen 7 tarjetas de empanadas
   ✓ Cada tarjeta tiene:
     - Imagen real (160px)
     - Nombre (ej: "Hawaiana")
     - Descripción completa
     - Precio ($70 o $80)
     - Spinner +/- con cantidad
```

### ✅ Test 2: Seleccionar Cantidad
```
1. En la tarjeta de "Hawaiana":
2. Haz click [+] varias veces
3. Verifica:
   ✓ La cantidad sube (0 → 1 → 2 → 3...)
   ✓ El input muestra el número
   ✓ Resumen actualiza en tiempo real
```

### ✅ Test 3: Múltiples Sabores
```
1. Selecciona:
   - 2x Hawaiana
   - 1x Hawaiana Especial
   - 3x Carnes Mixtas
2. Verifica resumen:
   "Hawaiana: 2"
   "Hawaiana Especial: 1"
   "Carnes Mixtas: 3"
3. Verifica total: $140 + $80 + $240 = $460
```

### ✅ Test 4: Bebida
```
1. Con empanadas seleccionadas
2. Abre selector de bebida
3. Selecciona una bebida
4. Verifica:
   ✓ Se agrega al resumen
   ✓ Se agrega el precio
   ✓ Total se recalcula
```

### ✅ Test 5: Envío por WhatsApp
```
1. Con empanadas y bebida seleccionadas
2. Completa datos (nombre, teléfono, dirección)
3. Haz click "📞 CONFIRMAR PEDIDO VÍA WHATSAPP"
4. Verifica mensaje:
   ✓ Incluye todas las empanadas
   ✓ Incluye cantidades correctas
   ✓ Incluye precios correctos
   ✓ Incluye bebida
   ✓ Total correcto
```

### ✅ Test 6: Responsividad
```
Desktop (1920px):  3-4 empanadas por fila ✓
Tablet (768px):    2-3 empanadas por fila ✓
Mobile (375px):    1-2 empanadas por fila ✓
```

---

## 🎨 Características Visuales

### Spinner +/- por Tarjeta
- **Botones rojos** (−) y (+)
- **Input numérico** en el medio
- **Sin límite** de cantidad
- **Hover effect** en botones
- **Actualización en tiempo real** del resumen

### Estructura Idéntica a Pizza Individual
- Misma altura de imagen (160px)
- Mismo ancho de tarjeta (260px)
- Mismo grid (3-4 columnas)
- Mismo color de borde y efectos
- Mismo padding y espacios

### Imágenes Reales
- Extraídas del archivo original
- Alternadas entre 7 empanadas
- Base64 incrustado (sin HTTP requests)
- Carga rápida

---

## 🛠️ Personalización

### Cambiar Precio de una Empanada
```javascript
// En el objeto empanadaPrices:
var empanadaPrices = {
    'Hawaiana': 70,              // Cambiar 70 por otro valor
    'Hawaiana Especial': 80,     // Cambiar 80 por otro valor
    // ...
};
```

### Cambiar Descripción
```javascript
var empanadaDescriptions = {
    'Hawaiana': 'NUEVA DESCRIPCIÓN aquí',
    // ...
};
```

### Agregar Nueva Empanada
```javascript
// 1. Agregar al array de sabores:
var empanadaFlavors = [
    'Hawaiana',
    'Hawaiana Especial',
    // ... más sabores ...
    'Mi Nueva Empanada'  // ← NUEVA
];

// 2. Agregar precio:
var empanadaPrices = {
    // ... precios existentes ...
    'Mi Nueva Empanada': 75  // ← NUEVA
};

// 3. Agregar descripción:
var empanadaDescriptions = {
    // ... descripciones existentes ...
    'Mi Nueva Empanada': 'Descripción de mi empanada'
};
```

La empanada nueva aparecerá automáticamente en el catálogo.

### Cambiar Imágenes
Las 2 imágenes se usan así:
- Empanadas 1, 3, 5, 7 → Imagen 1
- Empanadas 2, 4, 6 → Imagen 2

Para cambiar una imagen, modifica `empanadaImages`:
```javascript
var empanadaImages = {
    'Empanada1': 'data:image/png;base64,...',  // Nueva imagen 1
    'Empanada2': 'data:image/png;base64,...'   // Nueva imagen 2
};
```

---

## 📊 Comparativa Final

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Botones** | 2 | **3** |
| **Productos** | 14 pizzas + 6 combos | **+ 7 empanadas** |
| **Sistema venta** | Pizzas: por tamaño, Combos: fijos | **Empanadas: por unidad** |
| **Tarjetas** | Solo pizzas y combos | **+ Empanadas (260px)** |
| **Total opciones** | 20 | **27** |
| **Imágenes** | Muchas | **+ 2 adicionales** |

---

## 🚀 Cómo Usar

### Paso 1: Abre el archivo
```
Haz doble clic en: pag_web_2026_completa.html
```

### Paso 2: Prueba
```
1. Selecciona "🥟 Empanadas"
2. Selecciona cantidades con spinner +/-
3. Selecciona bebida (opcional)
4. Completa datos
5. Envía por WhatsApp
```

### Paso 3: Deploy
```bash
# Opción A: Reemplazar original
cp pag_web_2026_completa.html pag_web_2026_pizzas_11.html

# Opción B: Mantener como alternativa
# - Usa completa como versión nueva
# - Guarda original como respaldo
```

---

## ✅ Checklist de Validación

- ✅ Botón "🥟 Empanadas" visible
- ✅ 7 empanadas muestran correctamente
- ✅ Imágenes cargan (160px)
- ✅ Spinner +/- funciona sin límite
- ✅ Cantidad se actualiza en input
- ✅ Resumen calcula correctamente
- ✅ Bebida se agrega al total
- ✅ WhatsApp recibe todos los datos
- ✅ Responsive en desktop/tablet/mobile
- ✅ Cambiar entre Pizza/Combo/Empanadas funciona
- ✅ Precios correctos ($70 y $80)

---

## 🎉 ¡LISTO!

Tu página web ahora tiene:

```
🍕 PIZZAS INDIVIDUALES
  • 14 sabores
  • Por tamaño (Mini a Jumbo)
  • Tarjetas grandes (260px)

🎉 COMBOS (PROMOCIONES)
  • 6 opciones
  • Multipizzas con precios especiales
  • Tarjetas compactas

🥟 EMPANADAS ✨ NUEVO
  • 7 sabores
  • Por unidad (cantidad variable)
  • Spinner +/- por tarjeta
  • Misma ubicación que pizzas
```

**Archivo:** `pag_web_2026_completa.html`

¿Necesitas ajustes o cambios adicionales? 🚀
