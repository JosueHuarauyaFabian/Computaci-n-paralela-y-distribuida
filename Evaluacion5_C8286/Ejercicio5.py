import asyncio
from multiprocessing import Pool
import json
import aiofiles  # Importar aiofiles para manejo asincrónico de archivos

# Funciones puras para el procesamiento genómico
def filter_variants(variants, min_depth=10, min_quality=20):
    return [variant for variant in variants if variant['depth'] >= min_depth and variant['quality'] >= min_quality]

def calculate_allele_frequencies(variants):
    allele_counts = {}
    for variant in variants:
        alleles = variant['alleles']
        for allele in alleles:
            allele_counts[allele] = allele_counts.get(allele, 0) + 1
    total_alleles = sum(allele_counts.values())
    return {allele: count / total_alleles for allele, count in allele_counts.items()}

def process_sample(sample):
    filtered_variants = filter_variants(sample['variants'])
    allele_frequencies = calculate_allele_frequencies(filtered_variants)
    return {'sample_id': sample['id'], 'allele_frequencies': allele_frequencies}

def process_genomic_data(data):
    with Pool(processes=4) as pool:
        results = pool.map(process_sample, data)
    return results

async def load_genomic_data(file_path):
    """Carga datos genómicos de forma asíncrona desde un archivo JSON usando aiofiles."""
    async with aiofiles.open(file_path, 'r') as file:
        data = await file.read()
    return json.loads(data)

async def analyze_genomic_data(file_path):
    data = await load_genomic_data(file_path)
    results = await asyncio.get_event_loop().run_in_executor(None, process_genomic_data, data)
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(analyze_genomic_data('path_to_genomic_data.json'))
