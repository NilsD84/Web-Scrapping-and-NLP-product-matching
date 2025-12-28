import re
import unicodedata
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Category synonyms for matching guard logic
category_groups = {
    "eye": ["eye", "occhi", "yeux", "regard", "contour"],
    "cleanser": ["falls", "detergente", "struccante", "cleanser", "purifying", "mousse"],
    "hand": ["hand", "mani", "mains"]
}


def normalize_text(text):
    if not isinstance(text, str):
        return ""
    
    # 1. Accent removal
    text = "".join(c for c in unicodedata.normalize('NFD', text.lower()) if unicodedata.category(c) != 'Mn')
    
    # 2. Fix the specific typo found in your scrape ("Moistrurizing")
    text = text.replace('moistrurizing', 'moisturizing')
    
    # 3. BRIDGE THE GAP: Map "moisturizing cream" to "nutritive treatment" 
    if 'hand' in text:
        text = text.replace('moisturizing cream', 'nutritive treatment')
    
    # 4. Strip Volume patterns
    text = re.sub(r'\d+[\.,]?\d*\s*(ml|m|pezzo|pezzi|duo|gr|g|oz|pcs)\b', ' ', text)
    
    # 5. Noise Removal
    noise = [
        'storie veneziane', 'palazzo nobile', 'collezione privata', "l'elixir des glaciers", 'valmont',
        'fondotinta', 'siero', 'crema', 'idratante', 'eau de toilette', 
        'extrait de parfum', 'parfum', 'latte detergente', 'struccante', 'gelatina', 
        'rinfrescante', 'correttore', 'tonicita', 'contorno',
    ]
    
    for word in noise:
        text = re.sub(r'\b' + word + r'\b', ' ', text)
        
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    
    # Sort and deduplicate
    return " ".join(sorted(list(set(text.split()))))


def clean_capacity(cap, name_context=""):
    if not isinstance(cap, str):
        cap = str(cap) if cap else ""
    text = (cap + " " + name_context).lower()
    
    vol_match = re.search(r'(\d+[\.,]?\d*)\s*(ml|gr|g|oz|m\b)', text)
    if vol_match:
        val = vol_match.group(1).replace(',', '.')
        if val.endswith('.0'):
            val = val[:-2]
        unit = vol_match.group(2)
        if unit == 'm':
            unit = 'ml' 
        return f"{val}{unit}"
    
    count_match = re.search(r'(?:pack of|pezzi|pezzo|pcs|units|duo)\s*(\d+)', text)
    if not count_match:
        count_match = re.search(r'(\d+)\s*(?:pezzi|pezzo|pcs|units|duo|pack)', text)
    
    if count_match:
        return f"{count_match.group(1)}pcs"
        
    return "N/A"


def find_best_match(target_key, reference_list, threshold=0.4):
    if not reference_list:
        return None, 0
    all_names = [target_key] + list(reference_list)
    vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4))
    tfidf_matrix = vectorizer.fit_transform(all_names)
    sims = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    idx = np.argmax(sims)
    return (reference_list[idx], sims[idx]) if sims[idx] >= threshold else (None, 0)