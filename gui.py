# gui.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from product_service import *


# -------------------------
# FUNÇÕES
# -------------------------

def clear_fields():
    """
    Limpa os campos da interface.
    """
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)


def load_products():
    """
    Carrega todos os produtos do banco
    e mostra na tabela.
    """

    for row in tree.get_children():
        tree.delete(row)

    products = get_products()

    for product in products:
        tree.insert("", tk.END, values=product)


def add_product_gui():
    """
    Adiciona produto pela interface.
    """

    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    if name == "" or quantity == "" or price == "":
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    add_product(name, int(quantity), float(price))

    clear_fields()
    load_products()


def select_product(event):
    """
    Quando o usuário seleciona um produto
    na tabela, os dados vão para os campos.
    """

    selected = tree.focus()

    values = tree.item(selected, "values")

    if values:
        entry_name.delete(0, tk.END)
        entry_name.insert(0, values[1])

        entry_quantity.delete(0, tk.END)
        entry_quantity.insert(0, values[2])

        entry_price.delete(0, tk.END)
        entry_price.insert(0, values[3])


def update_product_gui():
    """
    Atualiza produto selecionado.
    """

    selected = tree.focus()

    values = tree.item(selected, "values")

    if not values:
        return

    product_id = values[0]

    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    update_product(product_id, name, int(quantity), float(price))

    load_products()


def delete_product_gui():
    """
    Remove produto selecionado.
    """

    selected = tree.focus()

    values = tree.item(selected, "values")

    if not values:
        return

    confirm = messagebox.askyesno(
        "Confirmar",
        "Deseja remover este produto?"
    )

    if confirm:

        product_id = values[0]

        delete_product(product_id)

        load_products()


def search_gui():
    """
    Busca produtos.
    """

    term = entry_search.get()

    results = search_products(term)

    for row in tree.get_children():
        tree.delete(row)

    for product in results:
        tree.insert("", tk.END, values=product)


# -------------------------
# JANELA PRINCIPAL
# -------------------------

window = tk.Tk()
window.title("Inventory Management System")
window.geometry("700x500")


# -------------------------
# CAMPOS
# -------------------------

tk.Label(window, text="Product Name").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Quantity").pack()
entry_quantity = tk.Entry(window)
entry_quantity.pack()

tk.Label(window, text="Price").pack()
entry_price = tk.Entry(window)
entry_price.pack()


# -------------------------
# BOTÕES
# -------------------------

tk.Button(window, text="Add Product", command=add_product_gui).pack(pady=5)

tk.Button(window, text="Update Product", command=update_product_gui).pack(pady=5)

tk.Button(window, text="Delete Product", command=delete_product_gui).pack(pady=5)


# -------------------------
# BUSCA
# -------------------------

entry_search = tk.Entry(window)
entry_search.pack(pady=5)

tk.Button(window, text="Search", command=search_gui).pack()


# -------------------------
# TABELA
# -------------------------

tree = ttk.Treeview(window, columns=("ID", "Name", "Quantity", "Price"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")

tree.pack(fill="both", expand=True)

tree.bind("<<TreeviewSelect>>", select_product)


load_products()

window.mainloop()