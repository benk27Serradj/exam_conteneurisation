import pandas as pd
import numpy as np
import argparse

from sklearn.preprocessing import StandardScaler
from sklearn.manifold import trustworthiness
from sklearn.metrics import pairwise_distances


def load_original_data():
    df = pd.read_csv("data/city_lifestyle_dataset.csv")
    df_numeric = df.drop(columns=["city_name", "country"])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_numeric)

    return X_scaled


def evaluate_method(method_name, file_path, X_original):
    df_reduced = pd.read_csv(file_path)
    X_reduced = df_reduced.values

    trust = trustworthiness(X_original, X_reduced, n_neighbors=5)

    # BONUS METRIC: corrélation des distances
    D_original = pairwise_distances(X_original)
    D_reduced = pairwise_distances(X_reduced)

    corr = np.corrcoef(D_original.flatten(), D_reduced.flatten())[0, 1]

    print(f"\n--- {method_name} ---")
    print(f"Trustworthiness: {trust:.4f}")
    print(f"Distance correlation: {corr:.4f}")

    return trust, corr


def main():
    print("Hello, this is the exam!")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--method",
        type=str,
        default="all",
        choices=["pca", "tsne", "umap", "all"],
        help="Méthode à évaluer"
    )

    args = parser.parse_args()

    X_original = load_original_data()

    methods = {
        "pca": ("PCA", "outputs/pca_emb_2d.csv"),
        "tsne": ("t-SNE", "outputs/tsne_emb_2d.csv"),
        "umap": ("UMAP", "outputs/umap_emb_2d.csv"),
    }

    if args.method == "all":
        for key in methods:
            name, path = methods[key]
            evaluate_method(name, path, X_original)
    else:
        name, path = methods[args.method]
        evaluate_method(name, path, X_original)


if __name__ == "__main__":
    main()