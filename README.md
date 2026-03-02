# Dimensionality Reduction Evaluation

This project evaluates PCA, t-SNE, and UMAP on city lifestyle data using **trustworthiness** and **distance correlation**.

## Run Locally (Without Docker)

1. Install dependencies:
pip install -r requirements.txt

2. Run the script:

- **All methods** (default):
python evaluate.py

- **Specific method** (`pca`, `tsne`, `umap`):
python evaluate.py --method umap

---

## Run With Docker

1. Build the image:
docker build -t dim-reduction .

2. Run container:

- **All methods**:
docker run --rm dim-reduction

- **Specific method**:
docker run --rm dim-reduction python evaluate.py --method umap

---

## Notes

- The `--method` argument can be: `pca`, `tsne`, `umap`, or `all` (default: all).  
- CSV files are in `outputs/`:
  - `pca_emb_2d.csv`
  - `tsne_emb_2d.csv`
  - `umap_emb_2d.csv`


## Bonus Features

### 1. Choose which methods to evaluate (+2 pts)
Use the `--method` argument to run only the methods you want:

```bash
python evaluate.py --method umap
docker run --rm dim-reduction python evaluate.py --method umap
  ```
### 2. Extra comparison metric (+0.5 pt)

The script calculates both:

  - Trustworthiness
  - Distance correlation
for each method.

### 3. Update code or data after dockerization (+1 pt)

You can edit your local scripts, notebooks, or CSV files without rebuilding the Docker image by mounting your project folder as a volume:

```bash
docker run -d -p 8080:5000 -v $(pwd)/evaluate.py:/app/evaluate.py dim-reduction
```

### 4. Develop collaboratively in the same environment (+2 pts)

All students can use the same Docker image to ensure consistent Python and library versions:

Build the image once:
```bash
docker build -t dim-reduction .
```

Work locally o using a volume:
```bash
docker run --rm -v $(pwd):/app dim-reduction
```

Changes are immediately available inside the container.



