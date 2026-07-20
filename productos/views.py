from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Q
from django.core.paginator import Paginator

from .models import Producto
from .forms import ProductoForm


def lista_productos(request):

    buscar = request.GET.get("buscar")

    productos = Producto.objects.all()

    # Buscador
    if buscar:
        productos = productos.filter(
            Q(nombre__icontains=buscar) |
            Q(codigo__icontains=buscar)
        )

    # Estadísticas
    total_productos = productos.count()

    stock_total = productos.aggregate(
        total=Sum("stock")
    )["total"] or 0

    productos_activos = productos.filter(
        activo=True
    ).count()

    valor_inventario = sum(
        producto.precio * producto.stock
        for producto in productos
    )
    # Paginación
    paginador = Paginator(productos, 10)

    numero_pagina = request.GET.get("page")

    productos = paginador.get_page(numero_pagina)

    contexto = {
        "productos": productos,
        "total_productos": total_productos,
        "stock_total": stock_total,
        "productos_activos": productos_activos,
        "valor_inventario": valor_inventario,
    }

    return render(
        request,
        "productos/lista_productos.html",
        contexto
    )


def crear_producto(request):

    if request.method == "POST":

        formulario = ProductoForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                "Producto registrado correctamente."
            )

            return redirect("lista_productos")

    else:

        formulario = ProductoForm()

    return render(
        request,
        "productos/crear_producto.html",
        {
            "formulario": formulario
        }
    )


def editar_producto(request, id):

    producto = get_object_or_404(
        Producto,
        id=id
    )

    if request.method == "POST":

        formulario = ProductoForm(
            request.POST,
            instance=producto
        )

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                "Producto actualizado correctamente."
            )

            return redirect("lista_productos")

    else:

        formulario = ProductoForm(
            instance=producto
        )

    return render(
        request,
        "productos/crear_producto.html",
        {
            "formulario": formulario
        }
    )


def eliminar_producto(request, id):

    producto = get_object_or_404(
        Producto,
        id=id
    )

    if request.method == "POST":

        producto.delete()

        messages.success(
            request,
            "Producto eliminado correctamente."
        )

        return redirect("lista_productos")

    return render(
        request,
        "productos/eliminar_producto.html",
        {
            "producto": producto
        }
    )