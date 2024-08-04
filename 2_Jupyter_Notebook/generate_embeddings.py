import argparse
import networkx as nx
import numpy as np

from typing import Dict

parser = argparse.ArgumentParser(description='VERSE GraphEmbedding')
parser.add_argument('-d', '--data', type=str, default="hfc", help='dataset')
parser.add_argument('-t', '--threshold', type=int, default=50, help='threshold of filtering low coverage bins')
parser.add_argument('-g', '--graph', type=str, default="corr", help='graph construction method: corr, corr_exp or corr_kNN')
parser.add_argument('-sc', '--scale', type=str, default="none", help='how to scale the sparse corr')
parser.add_argument('-sa', '--sample', type=str, default="none", help='how to sample cells for the sparse corr')
parser.add_argument('-m', '--model', type=str, default="verse", help='which graph embedding method is used')
parser.add_argument('-k', '--kNN_graph', type=int, default=100, help='dimension of the embedding size')
parser.add_argument('-es', '--embed_size', type=int, default=32, help='dimension of the embedding size')
parser.add_argument('-alpha', '--alpha', type=float, default=0.85, help='damping factor for verse')
parser.add_argument('-nsamples', '--nsamples', type=int, default=3, help='number of negative samples')
parser.add_argument('-o', '--output', type=str, required=True, help='output filename for the embedding')
args = parser.parse_args()

class Embedding(object):
    def __init__(self, embedding_path: str, dimensions: int, index_path: str = None):
        self.dimensions = dimensions
        self.embeddings = self.load_embeddings(embedding_path)
        self.index: Dict[str, int] = {}
        if index_path:
            self.load_index(index_path)

    def load_embeddings(self, file_name: str) -> np.ndarray:
        print("Loading embeddings...")
        embeddings = np.fromfile(file_name, dtype=np.float32)
        length = embeddings.shape[0]
        assert length % self.dimensions == 0, f"The number of floats ({length}) in the embeddings is not divisible by" \
                                              f"the number of dimensions ({self.dimensions})!"
        embedding_shape = [int(length / self.dimensions), self.dimensions]
        self.embedding_shape = embedding_shape
        embeddings = embeddings.reshape(embedding_shape)
        print(f"Done loading embeddings (shape: {embeddings.shape}).")
        return embeddings

    def load_index(self, index_path: str) -> None:
        print("Loading uri index...")
        with open(index_path, "r") as file:
            for line in [line.strip() for line in file.readlines()]:
                index, uri = line.split(",", 1)
                self.index[uri] = int(index)
        print(f"Done loading {len(self.index)} items.")

    def __getitem__(self, item) -> np.ndarray:
        if self.index and isinstance(item, str):
            return self.embeddings[self.index[item]]
        return self.embeddings[item]
    
    def save_emb(self, path):
        for i in range(self.embedding_shape[0]):
            if i == 0:
                emb = self.embeddings[0]
            else:
                emb = np.vstack((emb,self.embeddings[i]))
        np.save(path, emb)

embeddings = Embedding("./tmp/tmp.bin", args.embed_size)

############################################################################################################################
############################################################################################################################
############################################################################################################################

path = args.data

# Save the embedding using the specified output filename
embeddings.save_emb(path+"corr_0_1_VERSE_"+str(args.output)+".npy")
