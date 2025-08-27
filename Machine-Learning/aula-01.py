# Aula 1
# Cosseno de similaridade, TF-IDF

# Imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Conjunto de documentos
documentos = [
    "O metaverso está transformando a educação.",
    "A inteligência artificial é usada em diagnósticos médicos.",
    "O metaverso e a realidade virtual impactam empresas e escolas."
]

# Consulta (query)
consulta = ["metaverso na educação"]

# Criação do modelo TF-IDF
vectorizer = TfidfVectorizer()

# Ajustar o vocabulário com documentos + consulta
tfidf_matrix = vectorizer.fit_transform(documentos + consulta)

# Separar vetores
docs_tfidf = tfidf_matrix[:-1]  # todos os documentos
query_tfidf = tfidf_matrix[-1]  # consulta

# Calcular similaridade entre consulta e cada documento
similaridades = cosine_similarity(query_tfidf, docs_tfidf).flatten()

# Ordenar documentos por relevância
ranking = np.argsort(similaridades)[::-1]  # ordem decrescente

# Mostrar resultados
print("Consulta:", consulta[0])
print("\nRanking dos documentos:")
for i in ranking:
    print(f"Documento {i+1}: '{documentos[i]}' - Similaridade: {similaridades[i]:.4f}")
