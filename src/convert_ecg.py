import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

def process_all_ecgs(directory="."):
    files = [f for f in os.listdir(directory) if f.endswith('.zqecg')]
    
    if not files:
        print("No se encontraron archivos .zqecg en el directorio.")
        return

    for file in files:
        print(f"Procesando: {file}...")
        try:
            # Offset técnico para saltar el header propietario
            raw = np.fromfile(file, dtype='<i4', offset=128)
            ids = raw[0::2]
            values = raw[1::2]
            unique_channels = np.unique(ids)

            pdf_name = file.replace(".zqecg", ".pdf")
            with PdfPages(pdf_name) as pdf:
                fig, axes = plt.subplots(len(unique_channels), 1, figsize=(10, 14))
                fig.suptitle(f"ECG Data Export - Source: {file}", fontsize=12)
                
                for i, ch_id in enumerate(unique_channels):
                    signal = values[ids == ch_id]
                    axes[i].plot(signal[:3000], color='red', linewidth=0.5)
                    axes[i].set_title(f"Channel ID: {ch_id}", fontsize=8)
                    axes[i].grid(True, which='both', color='red', linestyle=':', alpha=0.2)
                
                plt.tight_layout(rect=[0, 0.03, 1, 0.95])
                pdf.savefig()
                plt.close()
            print(f"Guardado como: {pdf_name}")
        except Exception as e:
            print(f"Error procesando {file}: {e}")

if __name__ == "__main__":
    process_all_ecgs()