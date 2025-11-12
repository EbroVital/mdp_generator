from tkinter import *
from tkinter import messagebox
import string
import random


class Application(Tk):
    def __init__(self):
        super().__init__()  # Initialiser Tk correctement
        
        self.title("Générateur de mot de passe")
        self.geometry("400x350")
        
        # Variables pour les checkbuttons
        self.use_letters = BooleanVar(value=False)
        self.use_numbers = BooleanVar(value=False)
        self.use_symbols = BooleanVar(value=False)
        
        # Création de l'interface
        self.create_widgets()
        
    def create_widgets(self):
        # Titre
        Label(self, text="Entrez la taille de votre mot de passe", 
              font=("Arial", 11)).pack(pady=10, padx=10)
        
        # Entrée pour la taille
        self.input = Entry(self, width=10, font=("Arial", 12))
        self.input.pack(pady=5)
        self.input.insert(0, "12")  # Valeur par défaut
        
        # Frame pour les checkbuttons
        frame_options = Frame(self)
        frame_options.pack(pady=15)
        
        Checkbutton(frame_options, text="Lettres (A-z)", 
                   variable=self.use_letters).pack(anchor=W)
        Checkbutton(frame_options, text="Nombres (0-9)", 
                   variable=self.use_numbers).pack(anchor=W)
        Checkbutton(frame_options, text="Caractères spéciaux (!@#...)", 
                   variable=self.use_symbols).pack(anchor=W)
        
        # Bouton de génération
        Button(self, text="Générer le mot de passe", 
               command=self.generate_password, 
               bg="#0C025D", fg="white", 
               font=("Arial", 10, "bold"),
               padx=20, pady=5).pack(pady=15)
        
        # Résultat
        self.result = Entry(self, width=35, font=("Arial", 11), 
                           justify=CENTER, state='readonly')
        self.result.pack(pady=5)
        
        # Bouton copier
        Button(self, text="Copier le mot de passe", 
               command=self.copy_password,
               bg="#0C025D", fg="white",
               padx=20, pady=5).pack(pady=10)
    
    def generate_password(self):
        try:
            # Récupérer la taille
            length = int(self.input.get())
            
            if length < 1:
                messagebox.showerror("Erreur", "La taille doit être au moins 1")
                return
            
            # Construire le pool de caractères
            characters = ""
            if self.use_letters.get():
                characters += string.ascii_letters
            if self.use_numbers.get():
                characters += string.digits
            if self.use_symbols.get():
                characters += string.punctuation
            
            # Vérifier qu'au moins une option est cochée
            if not characters:
                messagebox.showwarning("Attention", "Sélectionnez au moins un type de caractère")
                return
            
            # Générer le mot de passe
            password = ''.join(random.choice(characters) for _ in range(length))
            
            # Afficher le résultat
            self.result.config(state='normal')
            self.result.delete(0, END)
            self.result.insert(0, password)
            self.result.config(state='readonly')
            
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide")
    
    def copy_password(self):
        password = self.result.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            messagebox.showinfo("Succès", "Mot de passe copié dans le presse-papier!")
        else:
            messagebox.showwarning("Attention", "Générez d'abord un mot de passe")


if __name__ == "__main__":
    app = Application()
    app.mainloop()