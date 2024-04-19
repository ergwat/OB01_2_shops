import tkinter as tk


class Store:
    def __init__(self, name, address, items={}):
        self.name = name
        self.address = address
        self.items = items # словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
    def add_products(self, product, price):
        pass
    def remove_products(self, product):
        pass
    def get_price(self, product):
        pass
    def price_update(self, product, new_price):
        pass

def store_add():
    name = shop_name_field.get()
    address = shop_address_field.get()
    if name and address:
        new_store = Store(name, address)
        stores_list.append(new_store)
        all_shops.insert(tk.END, new_store.name)


stores_list = []

'''def add_task():
    new_task = task_name_field.get()
    if new_task:
        task_list_new.insert(tk.END, new_task)
        task_name_field.delete(0, tk.END)

def on_enter(event):
    add_task()


def remove_task():
    if task_list_new.curselection():
        selected_task = task_list_new.curselection()
        task_list_new.delete(selected_task)
    elif task_list_in_progress.curselection():
        selected_task = task_list_in_progress.curselection()
        task_list_in_progress.delete(selected_task)
    elif task_list_done.curselection():
        selected_task = task_list_done.curselection()
        task_list_done.delete(selected_task)


def new_2_progress():
    selected_task = task_list_new.curselection()
    if selected_task:
        selected_task_name = task_list_new.get(selected_task)
        task_list_in_progress.insert(tk.END, selected_task_name)
        task_list_new.delete(selected_task)


def progress_2_new():
    selected_task = task_list_in_progress.curselection()
    if selected_task:
        selected_task_name = task_list_in_progress.get(selected_task)
        task_list_new.insert(tk.END, selected_task_name)
        task_list_in_progress.delete(selected_task)


def progress_2_done():
    selected_task = task_list_in_progress.curselection()
    if selected_task:
        selected_task_name = task_list_in_progress.get(selected_task)
        task_list_done.insert(tk.END, selected_task_name)
        task_list_done.itemconfig(tk.END, bg="SpringGreen")
        task_list_in_progress.delete(selected_task)


def done_2_progress():
    selected_task = task_list_done.curselection()
    if selected_task:
        selected_task_name = task_list_done.get(selected_task)
        task_list_in_progress.insert(tk.END, selected_task_name)
        task_list_done.delete(selected_task)


def save_data():
    text = task_list_new.get(0, tk.END)
    with open("new_tasks.txt", "w") as file:
        for text in text: #перебираем все элементы по одному
            new_text=str(text)+"\n"
            file.write(new_text)

    text = task_list_in_progress.get(0, tk.END)
    with open("in_progress_tasks.txt", "w") as file:
        for text in text:
            new_text = str(text) + "\n"
            file.write(new_text)

    text = task_list_done.get(0, tk.END)
    with open("done_tasks.txt", "w") as file:
        for text in text:
            new_text=str(text)+"\n"
            file.write(new_text)


def load_data():
    with open("new_tasks.txt", "r") as file:
        for line in file: #каждая строчка читается отдельно
            if line != "\n": task_list_new.insert(tk.END, line)

    with open("in_progress_tasks.txt") as file:
        for line in file:
            if line != "\n": task_list_in_progress.insert(tk.END, line)

    with open("done_tasks.txt") as file:
        for line in file:
            if line != "\n": task_list_done.insert(tk.END, line)
'''

root = tk.Tk()
root.title("Global store network planning system")



label3 = tk.Label(root, text="Список магазинов:")
label3.grid(row=0, column=0, pady=5, padx=5, sticky="W")

all_shops = tk.Listbox(root, width=30, height=10)
all_shops.grid(row=1, column=0, pady=10, padx=5)

label4 = tk.Label(root, text="Товары:")
label4.grid(row=0, column=3, pady=0, padx=5, sticky="W")

all_goods = tk.Listbox(root, width=30, height=10)
all_goods.grid(row=1, column=3, pady=0, padx=5, sticky="W")

label5 = tk.Label(root, text="Цены:")
label5.grid(row=0, column=4, pady=0, padx=5, sticky="W")

all_prices = tk.Listbox(root, width=30, height=10)
all_prices.grid(row=1, column=4, pady=0, padx=5, sticky="W")

# == блок добавления нового магазина ==
# =====================================
add_new_store_label = tk.Label(root, text="Добавление нового магазина:")
add_new_store_label.grid(row=2, column=0, columnspan = 3, pady=10, padx=5, sticky = "W")

new_store_name_label = tk.Label(root, text="Название:")
new_store_name_label.grid(row=3, column=0, pady=10, padx=5, sticky="W")

shop_name_field = tk.Entry(root, width=40)
shop_name_field.grid(row=3, column=1, pady=10, padx=5, sticky="W")
#shop_name_field.bind('<Return>', on_enter)

new_store_address_label = tk.Label(root, text="Адрес:")
new_store_address_label.grid(row=3, column=2, pady=10, padx=5)

shop_address_field = tk.Entry(root, width=40)
shop_address_field.grid(row=3, column=3, pady=10, padx=5, sticky="W")

add_new_shop_button = tk.Button(root, text="Добавить магазин", width=20, command=store_add)
add_new_shop_button.grid(row=3, column=4, pady=5, padx=5)
# =====================================


# === блок добавления нового товара ===
# =====================================
new_product_label = tk.Label(root, text="Добавление нового товара:")
new_product_label.grid(row=4, column=0, columnspan = 3, pady=10, padx=5, sticky = "W")

new_product_name_label = tk.Label(root, text="Товар:")
new_product_name_label.grid(row=5, column=0, pady=10, padx=5, sticky="W")
new_product_name_field = tk.Entry(root, width=40)
new_product_name_field.grid(row=5, column=1, pady=10, padx=5, sticky="W")

new_product_price_label = tk.Label(root, text="Цена:")
new_product_price_label.grid(row=5, column=2, pady=10, padx=5)
new_product_price_field = tk.Entry(root, width=40)
new_product_price_field.grid(row=5, column=3, pady=10, padx=5, sticky="W")

add_new_product_button = tk.Button(root, text="Добавить товар", width=20) #, command=store_add)
add_new_product_button.grid(row=5, column=4, pady=5, padx=5)
# =====================================


# === блок обновления цены товара ===
# =====================================
update_price_block_label = tk.Label(root, text="Обновление цены товара:")
update_price_block_label.grid(row=6, column=0, columnspan = 3, pady=10, padx=5, sticky = "W")

update_price_product_name_label = tk.Label(root, text="Товар:")
update_price_product_name_label.grid(row=7, column=0, pady=10, padx=5, sticky="W")
update_price_product_name_label = tk.Label(root, text="Здесь будет название товара")
update_price_product_name_label.grid(row=7, column=1, pady=10, padx=5, sticky="W")

update_price_product_price_label = tk.Label(root, text="Новая цена:")
update_price_product_price_label.grid(row=7, column=2, pady=10, padx=5)
update_price_new_price_field = tk.Entry(root, width=40)
update_price_new_price_field.grid(row=7, column=3, pady=10, padx=5, sticky="W")

update_price_button = tk.Button(root, text="Обновить цену", width=20) #, command=store_add)
update_price_button.grid(row=7, column=4, pady=5, padx=5)
# =====================================




'''

label2 = tk.Label(root, text="Задачи в работе:")
label2.grid(row=1, column=2, pady=5, padx=5)
label3 = tk.Label(root, text="Завершённые задачи:")
label3.grid(row=1, column=4, pady=5, padx=5)

task_list_new = tk.Listbox(root, width=30, height=10)
task_list_new.grid(row=5, rowspan=4, column=0, pady=10, padx=5)

new_2_progress_button = tk.Button(root, text=" > ", width=10, command=new_2_progress)
new_2_progress_button.grid(row=6, column=1)

progress_2_new = tk.Button(root, text=" < ", width=10, command=progress_2_new)
progress_2_new.grid(row=7, column=1)

task_list_in_progress = tk.Listbox(root, width=30, height=10)
task_list_in_progress.grid(row=5,  rowspan=4, column=2, pady=10, padx=5)

progress_2_done_button = tk.Button(root, text=" > ", width=10, command=progress_2_done)
progress_2_done_button.grid(row=6, column=3, pady=5)

done_2_progress_button = tk.Button(root, text=" < ", width=10, command=done_2_progress)
done_2_progress_button.grid(row=7, column=3)

task_list_done = tk.Listbox(root, width=30, height=10)
task_list_done.grid(row=5,  rowspan=4, column=4, pady=10, padx=5)

button4 = tk.Button(root, text = "Загрузить данные", command=load_data)
button4.grid(row=10, column=2, pady=5, padx=5)

button2 = tk.Button(root, text = "Сохранить данные", command=save_data)
button2.grid(row=10, column=3, pady=5, padx=5)

button3 = tk.Button(root, text="Удалить задачу", width=20, command=remove_task)
button3.grid(row=10, column=4, pady=5, padx=5)
'''

root.mainloop()