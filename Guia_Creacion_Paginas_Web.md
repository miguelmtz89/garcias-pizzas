# GUÍA DE CREACIÓN DE PÁGINAS WEB
## Restaurantes y Pizzerías - Sistema Plantilla Reutilizable

---

## TABLA DE CONTENIDOS
1. Introducción
2. Los 6 Pasos del Proceso
3. Qué NO Debe Cambiar (Código Inmutable)
4. Qué SÍ Puede Cambiar (Contenido Dinámico)
5. Orden Eficiente de Trabajo
6. Estructura de Configuración
7. Checklist de Implementación

---

## 1. INTRODUCCIÓN

Esta guía proporciona un proceso estructurado para crear páginas web de restaurantes y pizzerías de forma rápida y eficiente, utilizando una plantilla reutilizable que se adapta a diferentes negocios sin requerir cambios en el código funcional.

**Objetivo:** Crear un sistema donde el 80% de la página es código inmutable y el 20% es contenido configurable.

**Beneficios:**
- Menor tiempo de desarrollo
- Menor riesgo de errores
- Fácil replicación para nuevos clientes
- Mantenimiento simplificado

---

## 2. LOS 6 PASOS DEL PROCESO

### PASO 1: RECOLECTAR INFORMACIÓN
**Duración:** 1-2 horas
**Nota:** No requiere cambios en el código. Solo recopilación de datos.

**Información a recopilar:**
- Logo en diferentes formatos (PNG, SVG, JPG)
- Nombre del restaurante/pizzería
- Paleta de colores corporativos (máximo 3-4 colores)
- Tipografía preferida (Arial, Helvetica, Georgia, etc.)
- Fotos de alta calidad de productos (pizzas, empanadas)
- Menú completo con precios actualizados
- Redes sociales (Facebook, Instagram, TikTok)
- Número de WhatsApp para pedidos
- Ubicación completa y dirección
- Horarios de atención
- Política de delivery (costo, zonas de cobertura)
- Formas de pago aceptadas
- Datos del dueño/contacto

---

### PASO 2: CONFIGURAR ESTRUCTURA VISUAL
**Duración:** 1-2 horas
**⚠️ CRÍTICO: SE HACE UNA SOLA VEZ - NO CAMBIAR DESPUÉS**

**Acciones:**
- Definir variables CSS de color (--color-primary, --color-secondary, etc.)
- Seleccionar tipografía y crear variables de fuente
- Establecer espaciados y tamaños base
- Configurar responsive design (breakpoints)
- Ajustar bordes, sombras y efectos visuales

**Por qué no cambiar después:**
Modificar esto requiere revisar y actualizar TODO el CSS, lo que puede romper la responsividad en dispositivos móviles y crear inconsistencias visuales.

---

### PASO 3: CONFIGURAR NÚMERO DE WHATSAPP
**Duración:** 15 minutos
**⚠️ INMUTABLE - Buscar y reemplazar es tedioso después**

**Mejor práctica:**
Crear una variable global en JavaScript que se use en todas las funciones de WhatsApp:

```javascript
var WHATSAPP_NUMBER = "5215659941905"; // Cambiar aquí una sola vez
var whatsappLink = "https://wa.me/" + WHATSAPP_NUMBER + "?text=...";
```

---

### PASO 4: AGREGAR IMÁGENES Y LOGOS
**Duración:** 2-3 horas
**✅ Completamente modificable y fácil de cambiar**

**Tareas:**
- Copiar logo en carpeta /images
- Actualizar rutas src en HTML
- Optimizar imágenes para web (comprimir)
- Agregar fotos de productos
- Crear/ajustar imagen animada personalizada

---

### PASO 5: CARGAR CONTENIDO (MENÚS Y PRECIOS)
**Duración:** 2-4 horas
**✅ Fácilmente modificable - puede actualizarse sin riesgos**

**Cambios:**
- Actualizar nombres de pizzas
- Actualizar precios
- Modificar descripciones
- Agregar/quitar opciones de combos
- Ajustar políticas de delivery

**Nota:** Todos estos cambios están en HTML o variables de configuración, SIN tocar el código funcional.

---

### PASO 6: PRUEBAS Y LANZAMIENTO
**Duración:** 1-2 horas

**Pruebas funcionales:**
- Flujo de pedido completo (Pizza y Combo)
- Cálculo correcto de precios y delivery
- Envío a WhatsApp con datos completos
- Responsividad en móvil, tablet y desktop
- Prueba en diferentes navegadores

---

## 3. QUÉ NO DEBE CAMBIAR (CÓDIGO INMUTABLE)

⚠️ **CRÍTICO:** Estos elementos NO deben modificarse, ya que romperían la funcionalidad

| Sección | Razón | Si cambia, rompe... |
|---------|-------|------------------|
| `nextStep()` | Lógica del flujo de pedidos | Flujo de 6 pasos en el formulario |
| `updateProgressBar()` | Actualización de barra de progreso | Indicador visual de avance |
| `submitOrder()` | Envío a WhatsApp | Pedidos no se reciben |
| IDs HTML: #step1, #menu, #purchaseForm | Selectores para JavaScript | Funcionalidad completa del sitio |
| Estructura de validaciones | Seguridad de datos | Pedidos incompletos o inválidos |
| Estructura HTML de combos | Mapeo a funciones JavaScript | Selección de combos no funciona |
| Cálculo de precios | Lógica matemática | Precios incorrectos |

**Funciones JavaScript que NO deben tocarse:**
- setOrderType()
- selectCombo()
- selectPizza()
- selectDrink()
- updatePrice()
- submitOrder()
- nextStep()
- nextStepCombo()
- nextStepDirection()
- updateProgressBar()
- scrollToNextSection()
- orderWithQty()
- Cualquier función que comience con "window.open(whatsappLink)"

---

## 4. QUÉ SÍ PUEDE CAMBIAR (CONTENIDO DINÁMICO)

✅ **Estos elementos se pueden modificar sin riesgo.** De hecho, DEBEN cambiar para cada cliente.

| Elemento | Ubicación | Impacto al cambiar |
|----------|-----------|------------------|
| Logo | src en `<img>` | Visual - NINGUNO en funcionalidad |
| Colores (CSS variables) | Variables en `:root` | Visual - Toda la página adapta automáticamente |
| Nombres de pizzas | `<option>` en select | Contenido - Se muestra en resumen |
| Precios | data-price en HTML | Contenido - Cálculo automático actualiza |
| Fotos de productos | src en `<img>` | Visual - NINGUNO en funcionalidad |
| Texto de descripciones | Contenido HTML | Visual - NINGUNO en funcionalidad |
| Dirección del restaurante | HTML o variable JavaScript | Contenido - Se muestra en contacto |
| Datos de delivery | Variables JavaScript | Cálculo - Precio actualiza automáticamente |
| Redes sociales | Enlaces href | Visual - NINGUNO en funcionalidad |

---

## 5. ORDEN EFICIENTE DE TRABAJO

Este orden minimiza rework y asegura que cada paso prepara el terreno para el siguiente:

1. **INFORMACIÓN** → Recopilar todo (1-2 horas)
2. **COLORES/TIPOGRAFÍA** → Configurar en CSS (1-2 horas) - NO CAMBIAR DESPUÉS
3. **WHATSAPP** → Establecer número (15 min) - NO CAMBIAR DESPUÉS
4. **IMÁGENES/LOGOS** → Copiar y optimizar (2-3 horas)
5. **CONTENIDO** → Menús y precios (2-4 horas)
6. **PRUEBAS** → Verificar funcionalidad (1-2 horas)
7. **LANZAMIENTO** → Publicar (30 min)

**⏱️ Tiempo total estimado: 8-15 horas por sitio**

---

## 6. ESTRUCTURA DE CONFIGURACIÓN

Para máxima reutilización, crear un archivo `config.js` que centralice todos los datos que cambiarán por cliente:

```javascript
// config.js - Cambiar SOLO este archivo para nuevo cliente
const CONFIG = {
  // Datos del negocio
  restaurantName: "Garcia's Pizzas",
  address: "Calle Principal 123",

  // Contacto
  whatsappNumber: "5215659941905",
  phone: "+52 1 565-994-1905",
  email: "info@garciaspizzas.com",

  // Colores (si deseas cambiarlos dinámicamente)
  colors: {
    primary: "#E74C3C",
    secondary: "#2C3E50"
  },

  // Delivery
  delivery: {
    freeAbove: 120,
    smallCost: 30
  },

  // Redes sociales
  socialMedia: {
    facebook: "https://facebook.com/garciaspizzas",
    instagram: "https://instagram.com/garciaspizzas",
    whatsapp: "5215659941905"
  }
};
```

Luego, referencia CONFIG en el código principal:

```javascript
// En submitOrder() o cualquier función que envíe a WhatsApp:
var whatsappLink = 'https://wa.me/' + CONFIG.whatsappNumber + '?text=' + encodeURIComponent(message);
```

---

## 7. CHECKLIST DE IMPLEMENTACIÓN

Usa esta lista para asegurar que no olvides pasos:

### ✓ PASO 1: INFORMACIÓN
- [ ] Logo recolectado en 3+ formatos
- [ ] Colores corporativos definidos
- [ ] Tipografía seleccionada
- [ ] Menú con precios confirmado
- [ ] Número WhatsApp verificado
- [ ] Fotos de productos en alta resolución

### ✓ PASO 2: CONFIGURACIÓN VISUAL
- [ ] Variables CSS de color creadas
- [ ] Tipografía aplicada en estilos
- [ ] Responsive design verificado
- [ ] Colores testeados en todos los navegadores

### ✓ PASO 3: NÚMERO WHATSAPP
- [ ] Número actualizado en variable WHATSAPP_NUMBER
- [ ] Verificado en todos los formularios
- [ ] Testeado envío real

### ✓ PASO 4: IMÁGENES
- [ ] Logo copiado a /images
- [ ] Rutas src actualizadas
- [ ] Imágenes optimizadas para web
- [ ] Fotos de productos listos

### ✓ PASO 5: CONTENIDO
- [ ] Nombres de pizzas actualizados
- [ ] Precios correctos en HTML
- [ ] Descripciones ajustadas
- [ ] Combos configurados
- [ ] Datos de delivery actualizados

### ✓ PASO 6: PRUEBAS
- [ ] Flujo completo Pizza → Pedido
- [ ] Flujo completo Combo → Pedido
- [ ] Precios calculados correctamente
- [ ] WhatsApp recibe formato correcto
- [ ] Responsividad verificada (móvil, tablet, desktop)
- [ ] Navegadores probados (Chrome, Firefox, Safari, Edge)

### ✓ PASO 7: LANZAMIENTO
- [ ] Dominio configurado
- [ ] SSL/HTTPS instalado
- [ ] SEO básico (títulos, meta descriptions)
- [ ] Analytics instalado (Google Analytics/Facebook Pixel)
- [ ] Backup realizado
- [ ] URL compartida con cliente

---

## CONCLUSIÓN

Siguiendo este proceso, lograrás:

✅ Crear páginas web de restaurantes en 8-15 horas
✅ Plantilla reutilizable sin cambios en código funcional
✅ Menor riesgo de errores
✅ Fácil onboarding para nuevos desarrolladores
✅ Rápida implementación de cambios para clientes
✅ Mantenimiento simplificado

**La clave está en SEPARAR lo inmutable (código) de lo dinámico (contenido).**

---

*Documento generado: Enero 2025*
*Versión: 1.0*
