# 📝 Código Modificado - Opción B

## 1️⃣ CSS AGREGADO

### Ubicación en archivo original
Se insertó **antes de `</style>`** (línea ~26993)

```css
/* ─────────────────────────────────────────────────── */
/* TARJETAS COMPACTAS PARA SELECCIÓN DE SABORES COMBO */
/* ─────────────────────────────────────────────────── */

.combo-pizza-card {
    background: #fff;
    border-radius: 10px;
    overflow: hidden;
    border: 2px solid #ddd;
    cursor: pointer;
    transition: .25s;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.combo-pizza-card:hover {
    border-color: var(--rojo);                    /* Borde rojo al hover */
    box-shadow: 0 6px 16px rgba(0,0,0,.12);      /* Sombra más profunda */
    transform: translateY(-3px);                  /* Se eleva 3px */
}

.combo-pizza-card.selected {
    border-color: var(--rojo);                    /* Borde rojo */
    background: #fff0f0;                          /* Fondo rosado */
    box-shadow: 0 0 12px rgba(237,31,37,0.35);   /* Sombra roja intensa */
}

/* Contenedor de imagen */
.combo-pizza-card-img {
    width: 100%;
    height: 100px;                                /* Altura fija 100px */
    overflow: hidden;
    background: #f5f5f5;
    position: relative;
}

.combo-pizza-card-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;                            /* Crop la imagen manteniendo aspecto */
}

/* Contenedor de contenido */
.combo-pizza-card-content {
    padding: 8px;
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #fff;
}

/* Nombre de la pizza */
.combo-pizza-card-name {
    font-family: var(--ff-h);
    font-size: 12px;
    font-weight: 700;
    color: var(--negro);
    text-transform: uppercase;
    letter-spacing: .5px;
    margin-bottom: 4px;
    line-height: 1.2;
}

/* Descripción */
.combo-pizza-card-desc {
    font-size: 10px;
    color: #666;
    line-height: 1.2;
    flex: 1;                                      /* Expande si hay espacio */
}

/* Grid de sabores */
.combo-flavor-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(135px, 1fr));  /* 3-4 cols */
    gap: .8rem;
    margin-top: .8rem;
    margin-bottom: 1.2rem;
}

/* Etiqueta "Pizza N — Selecciona Sabor" */
.combo-flavor-label-box {
    font-family: var(--ff-h);
    font-size: 13px;
    font-weight: 700;
    color: var(--negro);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: .6rem;
    padding: .5rem;
    background: rgba(237,31,37,.08);             /* Fondo rojo tenue */
    border-radius: 6px;
    border-left: 4px solid var(--rojo);          /* Raya roja a la izquierda */
}
```

---

## 2️⃣ FUNCIÓN JAVASCRIPT PRINCIPAL - ANTES

### Ubicación
Línea 1014-1045 en el archivo original

```javascript
// ❌ VERSIÓN ANTIGUA (DROPDOWNS)
function buildFlavorSelects(count) {
    var container = document.getElementById('comboFlavorSelects');
    container.innerHTML = '';
    for (var i = 0; i < count; i++) {
        var row = document.createElement('div');
        row.className = 'combo-flavor-row';
        var lbl = document.createElement('label');
        lbl.textContent = 'Pizza ' + (i + 1) + ' — Sabor';
        
        // ← CREABA UN <select> DROPDOWN
        var sel = document.createElement('select');
        sel.className = 'form-select';
        sel.setAttribute('data-idx', i);
        sel.onchange = function(){ updateComboFlavor(this); };
        var opt0 = document.createElement('option');
        opt0.value = '';
        opt0.textContent = '-- Elige un sabor --';
        sel.appendChild(opt0);
        
        // Agregar todos los sabores al dropdown
        for (var j = 0; j < pizzaFlavors.length; j++) {
            var opt = document.createElement('option');
            opt.value = pizzaFlavors[j];
            opt.textContent = pizzaFlavors[j];
            sel.appendChild(opt);
        }
        row.appendChild(lbl);
        row.appendChild(sel);
        container.appendChild(row);
    }
    comboFlavors = new Array(count).fill('');
}
```

**Problemas:**
- ❌ No mostraba imágenes
- ❌ No mostraba descripciones
- ❌ UX pobre en mobile
- ❌ Poco intuitivo

---

## 2️⃣ FUNCIÓN JAVASCRIPT PRINCIPAL - DESPUÉS

### Ubicación
Reemplaza la anterior (línea 1014-1045)

```javascript
// ✅ VERSIÓN NUEVA (TARJETAS COMPACTAS)
function buildFlavorSelects(count) {
    var container = document.getElementById('comboFlavorSelects');
    container.innerHTML = '';
    
    // Para cada pizza en el combo
    for (var i = 0; i < count; i++) {
        // Crear etiqueta con número de pizza
        var flavorLabel = document.createElement('div');
        flavorLabel.className = 'combo-flavor-label-box';
        flavorLabel.textContent = '🍕 Pizza ' + (i + 1) + ' — Selecciona Sabor';
        container.appendChild(flavorLabel);
        
        // Crear grid para mostrar tarjetas
        var grid = document.createElement('div');
        grid.className = 'combo-flavor-grid';
        grid.setAttribute('data-pizza-idx', i);
        
        // Para cada sabor disponible, crear una tarjeta
        for (var j = 0; j < pizzaFlavors.length; j++) {
            // Contenedor principal de la tarjeta
            var card = document.createElement('div');
            card.className = 'combo-pizza-card';
            card.setAttribute('data-flavor', pizzaFlavors[j]);
            card.setAttribute('data-idx', i);
            card.onclick = function(){ selectComboFlavor(this); };  // ← NUEVO HANDLER
            
            // Contenedor de imagen
            var imgDiv = document.createElement('div');
            imgDiv.className = 'combo-pizza-card-img';
            
            // Imagen de la pizza
            var img = document.createElement('img');
            img.src = getPizzaImage(pizzaFlavors[j]);  // ← OBTIENE IMAGEN BASE64
            imgDiv.appendChild(img);
            
            // Contenedor de contenido (nombre + descripción)
            var content = document.createElement('div');
            content.className = 'combo-pizza-card-content';
            
            // Nombre de la pizza
            var name = document.createElement('div');
            name.className = 'combo-pizza-card-name';
            name.textContent = pizzaFlavors[j];
            
            // Descripción
            var desc = document.createElement('div');
            desc.className = 'combo-pizza-card-desc';
            desc.textContent = pizzaDescriptions[pizzaFlavors[j]] || '';  // ← OBTIENE DESCRIPCIÓN
            
            // Armar la estructura HTML
            content.appendChild(name);
            content.appendChild(desc);
            
            card.appendChild(imgDiv);
            card.appendChild(content);
            grid.appendChild(card);
        }
        
        container.appendChild(grid);
    }
    
    // Inicializar array de sabores seleccionados
    comboFlavors = new Array(count).fill('');
}
```

**Mejoras:**
- ✅ Muestra imágenes de cada pizza
- ✅ Muestra descripción de cada pizza
- ✅ Grid responsive (3-4 columnas)
- ✅ Intuitivo y visualmente atractivo
- ✅ Mejor UX en mobile (tarjetas tappables)

---

## 3️⃣ NUEVA FUNCIÓN - selectComboFlavor()

### Ubicación
Se inserta **inmediatamente después de `buildFlavorSelects()`**

```javascript
// ✅ NUEVA FUNCIÓN - Maneja clicks en tarjetas
function selectComboFlavor(cardElement) {
    // Obtener índice de pizza (0, 1, 2...)
    var idx = parseInt(cardElement.getAttribute('data-idx'));
    
    // Obtener sabor seleccionado (nombre de la pizza)
    var flavor = cardElement.getAttribute('data-flavor');
    
    // Obtener el grid padre (todas las tarjetas de esta pizza)
    var grid = cardElement.parentElement;
    
    // Remover clase 'selected' de TODAS las tarjetas del grid
    grid.querySelectorAll('.combo-pizza-card').forEach(function(c) {
        c.classList.remove('selected');
    });
    
    // Agregar clase 'selected' solo a la tarjeta clickeada
    cardElement.classList.add('selected');
    
    // Guardar el sabor seleccionado en el array
    comboFlavors[idx] = flavor;
    
    // Actualizar el resumen de precio
    updatePrice();
}
```

**Flujo:**
1. Usuario clickea una tarjeta
2. Se obtiene qué pizza es y qué sabor
3. Se remueve `.selected` de todas las tarjetas del grid
4. Se agrega `.selected` a la tarjeta clickeada (color rojo)
5. Se actualiza el array `comboFlavors[]`
6. Se actualiza el resumen en tiempo real

---

## 4️⃣ NUEVA FUNCIÓN - getPizzaImage()

### Ubicación
Se inserta después de `selectComboFlavor()`

```javascript
// ✅ NUEVA FUNCIÓN - Obtiene la imagen base64 de una pizza
function getPizzaImage(flavorName) {
    // Si existe la imagen en el objeto pizzaImages, devolverla
    if (pizzaImages[flavorName]) {
        return pizzaImages[flavorName];
    }
    
    // Si no existe, devolver un placeholder gris
    return 'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Crect fill=%22%23f5f5f5%22 width=%22100%22 height=%22100%22/%3E%3C/svg%3E';
}
```

---

## 5️⃣ OBJETOS DE DATOS GLOBALES

### Ubicación
Se insertan después de `var pizzaFlavors = [...]` (línea 942)

```javascript
// ✅ DESCRIPCIONES DE CADA PIZZA
var pizzaDescriptions = {
    "Pepperoni": "Pepperoni premium sobre salsa de tomate y queso mozzarella fundido",
    "Margarita": "Solo extra queso — pura cremosidad derretida en cada rebanada",
    "Mesa Luna": "Chorizo y Pepperoni — combinación perfecta para amantes de la carne",
    "Hawaiana": "Jamón y piña fresca — el clásico dulce-salado que conquista paladares",
    "Hawaiana Especial": "Jamón, piña y cereza — versión premium con toque dulce irresistible (+$10)",
    "Carnes Mixtas": "Jamón, salchicha, pepperoni y chorizo — para quienes no pueden elegir",
    "Casino": "Pepperoni, champiñón, piña y jalapeño — atrevida, diferente y deliciosa",
    "De la Casa": "Jamón, champiñones, chorizo y jalapeño — nuestra receta estrella García",
    "Charra": "Chorizo, frijoles, salchicha y jalapeño — 100% sabor y tradición mexicana",
    "Mexicana": "Chorizo, jitomate, cebolla y jalapeño — el alma de México en cada mordida",
    "Cuatro Estaciones": "Jamón, champiñones, piña y salchicha — un tour gastronómico en una rebanada",
    "Jardinera": "Champiñones, pimiento, cebolla y jitomate — fresca y saludable",
    "Tri Bambini": "Jamón, queso y piña en forma de pizza infantil — perfecta para los pequeños",
    "Crea tu Pizza": "Elige tus ingredientes y crea tu propia pizza personalizada"
};

// ✅ IMÁGENES BASE64 DE CADA PIZZA
var pizzaImages = {
    "Pepperoni": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAgAOIg4jAAD/...(63,355 caracteres)...",
    "Margarita": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAgAOIg4jAAD/...(51,207 caracteres)...",
    "Mesa Luna": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAgAOIg4jAAD/...(56,551 caracteres)...",
    // ... (14 imágenes en total)
    "Crea tu Pizza": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAgAOIg4jAAD/...(60,051 caracteres)..."
};
```

---

## 6️⃣ CAMBIOS EN FUNCIÓN EXISTENTE - updatePrice()

### ¿Se modificó?
**NO.** La función `updatePrice()` sigue funcionando igual porque:

```javascript
// El resumen sigue obteniendo los sabores del mismo array
var flavorTexts = comboFlavors.filter(function(f){ return f !== ''; });
document.getElementById('summarySabores').textContent = flavorTexts.length > 0
    ? flavorTexts.join(', ')
    : '—';
```

El cambio es transparente: `comboFlavors[]` sigue teniendo los mismos datos, solo que ahora se llenan con clicks en tarjetas en lugar de cambios en dropdowns.

---

## 7️⃣ CAMBIOS EN FUNCIÓN EXISTENTE - submitOrder()

### ¿Se modificó?
**NO.** La función `submitOrder()` sigue funcionando igual porque:

```javascript
// El mensaje se arma de la misma manera
for (var i = 0; i < comboFlavors.length; i++) {
    flavorLines += '\n   • Pizza ' + (i + 1) + ': ' + comboFlavors[i];
}
```

El cambio es transparente: los datos en `comboFlavors[]` se obtienen de la misma forma.

---

## 📊 Resumen de Cambios

| Elemento | Antes | Después | Cambio |
|----------|-------|---------|--------|
| `<select>` dropdowns | ✓ | ✗ | Removido |
| Tarjetas visuales | ✗ | ✓ | Agregado |
| CSS nuevo | ✗ | ✓ | +1320 chars |
| `buildFlavorSelects()` | 32 líneas | 66 líneas | Reescrito |
| `selectComboFlavor()` | No existía | ✓ | Nuevo |
| `getPizzaImage()` | No existía | ✓ | Nuevo |
| Objetos de datos | ✗ | ✓ | Agregado |
| Funciones existentes | ✓ | ✓ | Sin cambios |

---

## 🔄 Flujo Completo Comparativo

### ANTES (Dropdowns)
```
Usuario selecciona Combo
        ↓
buildFlavorSelects() crea 3 <select>
        ↓
Usuario abre dropdown y selecciona opción
        ↓
Evento onchange en el <select>
        ↓
updateComboFlavor() lee select.value
        ↓
comboFlavors[idx] = valor
        ↓
updatePrice()
```

### DESPUÉS (Tarjetas)
```
Usuario selecciona Combo
        ↓
buildFlavorSelects() crea grid de tarjetas
        ↓
Usuario clickea una tarjeta
        ↓
Evento onclick en la tarjeta
        ↓
selectComboFlavor() lee data-flavor
        ↓
comboFlavors[idx] = sabor  ← MISMO RESULTADO
        ↓
updatePrice()
```

El resultado final es **idéntico**, solo que la experiencia visual es mucho mejor.

---

## 💡 Notas Importantes

### ✅ Mantenible
- Fácil agregar nuevas pizzas (3 lugares: `pizzaFlavors`, `pizzaDescriptions`, `pizzaImages`)
- Código bien estructurado
- Comentarios explicativos

### ⚡ Performante
- Grid CSS es eficiente
- Event delegation sin problemas
- Imágenes base64 (sin HTTP requests)
- Sin librerías externas

### 🔐 Compatible
- ES5 JavaScript (funciona en todos los navegadores)
- CSS Grid (IE 10+)
- Data URIs (universal)

### 🎨 Personalizable
- Cambiar colores: editar `:root` CSS
- Cambiar tamaño tarjetas: editar `minmax(135px, 1fr)`
- Cambiar altura imagen: editar `height: 100px`
- Cambiar numero de columnas: editar `grid-template-columns`

---

## 🚀 Para Implementar

1. Abre el archivo **`pag_web_2026_pizzas_modified.html`**
2. Prueba en navegador
3. Si te gusta, reemplaza el original:
   ```bash
   cp pag_web_2026_pizzas_modified.html pag_web_2026_pizzas_11.html
   ```

¡Listo! 🎉
