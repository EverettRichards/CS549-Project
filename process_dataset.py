import numpy as np
import pandas as pd
from urllib.parse import urldefrag
from sklearn.decomposition import PCA

common_tlds = ['com', 'org', 'net', 'de', 'uk', 'ca', 'edu', 'br', 'nl', 'info', 'au', 'ru', 'it', 'jp', 'pl', 'fr', 'gov', 'vn', 'eu', 'cn']

def process_dataset(df,TEST_MODE=False,PCA_DIM=2,NORMALIZE_TLD=False):

    dup_mask = df.duplicated()
    dup_count = dup_mask.sum()
    print("Duplicates to be removed:",dup_count)

    # Remove duplicate entries
    df.drop_duplicates(inplace=True) # Removes the 10,066 duplicates found below

    # Remove incomplete data points
    df.dropna(inplace=True) # There are no empty values in the dataset, but this is kept here for good measure

    # Convert "type" to binary digits
    df['type'] = df['type'].apply(lambda x: 0 if x == 'benign' else 1)

    # Calculate number of BENIGN and MALICIOUS URLs in the dataset
    benign_count = df['type'].value_counts().get(0, 0)
    malicious_count = df['type'].value_counts().get(1, 0)
    print(f"Total BENIGN URLs: {benign_count}")
    print(f"Total MALICIOUS URLs: {malicious_count}")

    class_to_remove = 0 if benign_count > malicious_count else 1

    # Remove abs(benign_count-malicious_count) data points with type=class_to_remove, at random, from the dataset
    difference = abs(benign_count - malicious_count)
    if difference > 0:
        df_class_to_remove = df[df['type'] == class_to_remove]
        df_class_to_remove_sampled = df_class_to_remove.sample(n=difference, random_state=42)
        df.drop(df_class_to_remove_sampled.index, inplace=True)

    print(f"Removed {difference} data points of class *{'malicious' if class_to_remove else 'benign'}* to balance the dataset.")
    
    # Convert url to lowercase
    df['url'] = df['url'].str.lower()

    # Determine if the url is an HTTPS address (secure)
    df['is_https'] = df['url'].apply(lambda x: 1 if 'https://' in x else 0)

    # Purge http(s):// -- it's just noise.
    df['url'] = df['url'].str.replace('http://', '')
    df['url'] = df['url'].str.replace('https://', '')
    df['url'] = df['url'].str.replace('www.', '')

    # Remove port from consideration
    df['url'] = df['url'].str.split(":").str[0]

    # Remove URL fragments (using a library)
    df['url'] = df['url'].apply(lambda u: urldefrag(u).url)

    # Record the length of each URL
    df['url_length'] = df['url'].apply(len)

    # Find the full domain (including subdomains)
    df['full_domain'] = df['url'].str.split("/").str[0]

    # Count the number of subdomains
    df['subdomain_count'] = df['full_domain'].apply(lambda x: len(x.split('.')) - 1)
    
    # Count the number of special characters found in the address
    df['count_special_chars'] = df['url'].apply(lambda u: sum(u.count(c) for c in '!@#$%^&*()[]{};:,./<>?|`~-=+'))
    
    # Record the ratio between numerical digits and the total length of the URL
    df['digit_to_length_ratio'] = df['url'].apply(lambda u: sum(c.isdigit() for c in u) / len(u) if len(u) > 0 else 0)
    
    # Remove URL and other non-numeric artifacts
    df["TLD"] = df['full_domain'].apply(lambda x: x.split('.')[-1] if '.' in x else '')
    if NORMALIZE_TLD:
        counts = df["TLD"].value_counts()
        norm_counts = (counts - counts.min()) / (counts.max() - counts.min())
        df["TLD_freq"] = df["TLD"].map(norm_counts).astype(float)
    else:
        counts = df["TLD"].value_counts()
        df["TLD_freq"] = df["TLD"].map(counts).astype(int)

    # Remove unneeded non-numeric columns
    if not TEST_MODE:
        df.drop(['url', 'full_domain', 'TLD'], axis=1, inplace=True)

    # Split into X (features) and y (labels)
    X_full = df.drop('type', axis=1)
    y_full = df['type']

    # Apply PCA to reduce dimensionality to PCA_DIM components for visualization and simplification
    if not TEST_MODE:
        pca = PCA(n_components=PCA_DIM)
        X_full_pca = pd.DataFrame(pca.fit_transform(X_full))
        # Print out correlations between each feature in X_full with each PC
        for col in X_full.columns:
            for pc in X_full_pca.columns:
                corr = np.corrcoef(X_full[col], X_full_pca[pc])[0, 1]
                print(f"Correlation between {col} and PC{pc+1}: {corr}")
        X_full = X_full_pca

    return X_full,y_full