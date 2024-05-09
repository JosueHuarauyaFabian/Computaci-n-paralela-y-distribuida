import re
import asyncio
from concurrent.futures import ThreadPoolExecutor
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Definición de stopwords
stop_words = set(stopwords.words('english'))

# Funciones puras para el pre-procesamiento de textos
def clean_text(text):
    """Limpia el texto eliminando caracteres especiales y convirtiéndolo a minúsculas."""
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    return text

def remove_stopwords(text):
    """Elimina las stopwords de un texto."""
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def preprocess_text(text):
    """Combina todas las operaciones de preprocesamiento de texto."""
    text = clean_text(text)
    text = remove_stopwords(text)
    return text

# Función pura para análisis de sentimiento
def analyze_sentiment(text):
    """Analiza el sentimiento de un texto dado y devuelve el resultado."""
    analysis = TextBlob(text)
    return {'polarity': analysis.sentiment.polarity, 'subjectivity': analysis.sentiment.subjectivity}

# Función para preprocesar y analizar textos de manera concurrente
def preprocess_and_analyze(text):
    """Preprocesa y analiza el sentimiento de un texto."""
    preprocessed_text = preprocess_text(text)
    sentiment = analyze_sentiment(preprocessed_text)
    return sentiment

# Uso de concurrent.futures para paralelizar el análisis
def analyze_texts_concurrently(texts):
    """Analiza una lista de textos concurrentemente."""
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(preprocess_and_analyze, texts))
    return results

# Integración con asyncio para manejo asincrónico
async def collect_and_process_data(stream_data):
    """Asíncronamente recolecta y procesa datos de un flujo."""
    processed_data = await asyncio.get_event_loop().run_in_executor(None, analyze_texts_concurrently, stream_data)
    print("Sentiment Analysis Results:", processed_data)

async def simulate_streaming_data():
    """Simula la llegada de datos de texto de un flujo en tiempo real."""
    sample_data = [
        "I love this product!",
        "This is the worst service ever.",
        "I'm not sure if I like this.",
        "Absolutely fantastic!"
    ]
    await collect_and_process_data(sample_data)

if __name__ == "__main__":
    asyncio.run(simulate_streaming_data())
