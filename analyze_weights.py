#!/usr/bin/env python3
import os
import sys

os.chdir('images')

print("=== DETALLE DE ARCHIVOS MAS PESADOS POR SECCION ===\n")

# 1. Carrusel
print("1. CARRUSEL DE ESPECIALIDADES (pizzas principales)")
archivos = sorted([(f'pizza-{i}.webp', os.path.getsize(f'pizza-{i}.webp')/1024) for i in range(1,15)], key=lambda x: x[1], reverse=True)
total = sum(a[1] for a in archivos)
for archivo, kb in archivos:
    print(f"   {archivo:20} {kb:6.0f} KB")
print(f"   {'SUBTOTAL':20} {total:6.0f} KB ({total/1024:.2f} MB)")

# 2. Menu
print("\n2. SECCION DE MENU (Pepperoni, Margarita, etc)")
menu_imgs = ['image_01.png', 'image-30.webp']
for i in range(30):
    if i != 1:
        menu_imgs.append(f'image_{i:02d}.webp')
archivos = []
for img in menu_imgs:
    if os.path.exists(img):
        kb = os.path.getsize(img)/1024
        archivos.append((img, kb))
archivos.sort(key=lambda x: x[1], reverse=True)
for archivo, kb in archivos[:10]:
    print(f"   {archivo:20} {kb:6.0f} KB")
print(f"   ... y {len(archivos)-10} imagenes mas")
total = sum(a[1] for a in archivos)
print(f"   {'SUBTOTAL':20} {total:6.0f} KB ({total/1024:.2f} MB)")

# 3. Empanadas
print("\n3. SECCION DE EMPANADAS")
archivos = [(f'empanada-{i}.webp', os.path.getsize(f'empanada-{i}.webp')/1024) for i in range(1,3)]
for archivo, kb in archivos:
    print(f"   {archivo:20} {kb:6.0f} KB")
total = sum(a[1] for a in archivos)
print(f"   {'SUBTOTAL':20} {total:6.0f} KB ({total/1024:.2f} MB)")

# 4. Combos
print("\n4. SECCION DE COMBOS")
archivos = [(f'combo-{i}.webp', os.path.getsize(f'combo-{i}.webp')/1024) for i in range(1,7)]
archivos.sort(key=lambda x: x[1], reverse=True)
for archivo, kb in archivos:
    print(f"   {archivo:20} {kb:6.0f} KB")
total = sum(a[1] for a in archivos)
print(f"   {'SUBTOTAL':20} {total:6.0f} KB ({total/1024:.2f} MB)")

# 5. Otros
print("\n5. LOGOS, EMOJIS Y OTROS")
otros = ['facebook-logo.png', 'instagram-logo.png', 'emoji de refresco.png', 'emoji jarritos.png', 'nueva ubicacion de garcias pizzas.webp', 'pizza-15.webp']
archivos = []
for img in otros:
    if os.path.exists(img):
        kb = os.path.getsize(img)/1024
        archivos.append((img, kb))
archivos.sort(key=lambda x: x[1], reverse=True)
for archivo, kb in archivos:
    print(f"   {archivo:30} {kb:6.0f} KB")
total = sum(a[1] for a in archivos)
print(f"   {'SUBTOTAL':30} {total:6.0f} KB ({total/1024:.2f} MB)")

print("\n=== RESUMEN GENERAL ===")
print("index.html:                         2.9 MB")
print("images/ total:                      8.13 MB")
print("PESO TOTAL PAGINA:                  11.0 MB")
