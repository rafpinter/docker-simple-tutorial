"""
Teste de execução do código dentro de um container docker.
"""

import os
import platform

print("\nQual o sistema operacional??\n")
print(f"O nome do OS é {os.name}...")
print(f"e a plataforma é {platform.system()}")
print(f"sendo que a release é {platform.release()}\n")
print("Logo...\n")


if platform.system() == 'Darwin':
    print("To rodando no Mac")
else:
    print("Não estou mais executando no Mac.")
    
print("\n")