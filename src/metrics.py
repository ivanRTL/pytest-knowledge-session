from typing import List
import random

class Model:
    def __init__(self, model_weights: str):
        # imagine loading weights
        self.model = model_weights

    def inference(img_path):
        return random.randint(0, 10)

class Metrics:
    def __init__(self, model: Model, imgs: List[str]):
        self.predictions = [model(img) for img in imgs]

    def get_metric(self, gts: List[int], mode="accuracy"):
        if mode == "accuracy":
            return sum([int(p == gt) for p, gt in zip(self.predictions, gts)]) / len(gts)
        elif mode == "precision":
            pass
        elif mode == "recall":
            pass