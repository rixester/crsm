import tkinter as tk
from tkinter import messagebox, ttk
from urllib.parse import quote


def get_proxy_config():
    root = tk.Tk()
    root.title("Configuração do Proxy")
    root.attributes('-topmost', True)


     # Lista de proxies
    proxy_map = {"COM1DN":"proxy-1dn.mb:6060","COM2DN":"proxy-2dn.mb:6060","COM3DN":"proxy-3dn.mb:6060",
                 "COM4DN":"proxy-4dn.mb:6060","COM5DN":"proxy-5dn.mb:6060","COM6DN":"proxy-6dn.mb:6060",
                 "COM7DN":"proxy-7dn.mb:6060","COM8DN":"proxy-8dn.mb:6060","COM9DN":"proxy-9dn.mb:6060"}

    proxies = list(proxy_map.keys())

    # Campos
    tk.Label(root, text="SENHA DA INTERNET NA SUA OM").grid(row=0, column=1, padx=1, pady=1, sticky="n")

    tk.Label(root, text="Usuário:").grid(row=1, column=0, padx=1, pady=1, sticky="e")
    usuario_entry = tk.Entry(root, width=25)
    usuario_entry.grid(row=1, column=1, padx=1, pady=1)
    
    tk.Label(root, text="Senha:").grid(row=2, column=0, padx=1, pady=1, sticky="e")
    senha_entry = tk.Entry(root, show="*", width=25)
    senha_entry.grid(row=2, column=1, padx=1, pady=1)

    # Checkbox para mostrar/ocultar senha
    def toggle_password():
        if senha_entry.cget('show') == '':
            senha_entry.config(show='*')
        else:
            senha_entry.config(show='')

    tk.Checkbutton(root, text="Mostrar senha", command=toggle_password).grid(row=2, column=2, padx=1, pady=1)

    # Dropdown para Proxy
    tk.Label(root, text="Seu DN:").grid(row=3, column=0, padx=1, pady=8, sticky="e")
    proxy_combobox = ttk.Combobox(root, values=proxies, state="readonly",justify="center", width=22)
    proxy_combobox.grid(row=3, column=1, padx=1, pady=8)
    proxy_combobox.set(proxies[2])  # Define o (COM3DN) como padrão
    
    tk.Label(root, text="").grid(row=4, column=0, padx=1, pady=18, sticky="e")

    # Ajusta tamanho automaticamente antes de centralizar
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 3

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

     # Resultado
    resultado = {"usuario": None, "senha": None, "proxy": None, "area": None,}

    def submit():
        usuario = usuario_entry.get().strip()
        senha = senha_entry.get().strip()
        proxy = proxy_combobox.get().strip()

        if not usuario or not senha or not proxy:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")
            return

        # Obter o proxy real a partir do nome amigável
        try:
            proxy = proxy_map[proxy]
        except KeyError:
            messagebox.showerror("Erro", f"Proxy inválido: {proxy}")
            return

        senha_codificada = quote(senha)
        
        resultado.update({
            "usuario": usuario,
            "senha": senha_codificada,
            "proxy": proxy
        })

        root.destroy()

    tk.Button(root, text="Confirmar", command=submit).grid(row=4, column=1, padx=1, pady=5, sticky="n")
    root.mainloop()
    return resultado


# --- Uso ---
proxy_info = get_proxy_config()

proxy_url = f"http://{proxy_info['usuario']}:{proxy_info['senha']}@{proxy_info['proxy']}"
PROXIES = {
    "http": proxy_url,
    "https": proxy_url
}
messagebox.showinfo("DADOS DO USUARIO",f"ESSE PAINEL É UM TESTE\n[INFO] Proxy configurado: '{PROXIES}'")
