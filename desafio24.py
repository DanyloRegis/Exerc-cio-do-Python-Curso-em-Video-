
cidade = input("Digite o nome da cidade: ").strip().lower()
# Verifica se a cidade começa com "santo"   
if cidade.startswith("santo") or cidade.startswith("Santo "):
    print("A cidade começa com 'Santo'.")
else:
    print("A cidade não começa com 'Santo'.")