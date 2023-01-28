from collections import Counter
import heapq

class huffman:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def crear_huffman(text):
    frecuencia = Counter(text)
    heap= []
    for char,freq in frecuencia.items():
        heapq.heappush(heap, huffman(char,freq))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = huffman(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)
    return heap[0]

frecuencias = {"A":0.2, "F":0.17, "1":0.13, "3":0.21, "0":0.05, "M":0.09, "T":0.15}
arbol = crear_huffman(frecuencias)

def hacer_codigos(raiz, code, codigos):
    if raiz is None:
        return
    if raiz.char is not None:
        codigos[raiz.char] = code
        return
    hacer_codigos(raiz.left, code + "0", codigos)
    hacer_codigos(raiz.right, code + "1", codigos)

def encoding(text):
    raiz = crear_huffman(text)
    codigos = {}
    hacer_codigos(raiz, "", codigos)
    encoded_text = ""
    for char in text:
        encoded_text += codigos[char]
    return encoded_text,raiz

def decoding(encoded_text, raiz):
    current = raiz
    decoded_text = ""
    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            decoded_text += current.char
            current = raiz
    return decoded_text

def prueba_huffman():
    text = "afat"
    print("Texto original: ", text)
    encoded_text, raiz = encoding(text)
    print("Texto codificado: ", encoded_text)
    decoded_text = decoding(encoded_text, raiz)
    print("Texto decodificado: ", decoded_text)

prueba_huffman()
