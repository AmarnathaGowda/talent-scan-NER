import os
import sys
from ner.exception import NerException
from ner.pipeline.train_pipeline import TrainPipeline

from ner.constants import *

def training():
    try:
        print("Training started")
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        print("Training completed")

    except Exception as e:
        raise NerException(e, sys) from e
    
if __name__ == "__main__":
    training()