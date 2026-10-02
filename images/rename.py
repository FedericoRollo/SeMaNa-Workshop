import os

def rename_images():
    # Estensioni valide per le immagini
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    
    # Prendi tutti i file nella cartella corrente che hanno un'estensione valida
    files = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
    
    # Ordina i file alfabeticamente per rinominarli in modo consistente
    files.sort()

    print(f"Trovate {len(files)} immagini da rinominare...")

    for index, filename in enumerate(files, start=1):
        # Ottieni l'estensione del file (es: .jpg)
        ext = os.path.splitext(filename)[1].lower()
        
        # Crea il nuovo nome (es: foto1.jpg)
        new_name = f"foto{index}{ext}"
        
        # Evita di sovrascrivere o rinominare file già correttamente rinominati
        if filename != new_name:
            os.rename(filename, new_name)
            print(f"Rinominato: {filename} -> {new_name}")

    print("Completato con successo!")

if __name__ == "__main__":
    rename_images()
