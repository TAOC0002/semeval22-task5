# Copyright (c) Facebook, Inc. and its affiliates.

import os
import warnings

from mmf.common.registry import registry
from mmf.datasets.builders.stereotype.dataset import (
    stereotypeFeaturesDataset,
    stereotypeImageDataset,
)
from mmf.datasets.mmf_dataset_builder import MMFDatasetBuilder
from mmf.utils.configuration import get_mmf_env
from mmf.utils.file_io import PathManager
from mmf.utils.general import get_absolute_path


@registry.register_builder("stereotype")
class stereotypeBuilder(MMFDatasetBuilder):
    def __init__(
        self,
        dataset_name="stereotype",
        dataset_class=stereotypeImageDataset,
        *args,
        **kwargs
    ):
        super().__init__(dataset_name, dataset_class, *args, **kwargs)
        self.dataset_class = stereotypeImageDataset

    @classmethod
    def config_path(self):
        return "configs/datasets/stereotype/defaults.yaml"

    def load(self, config, dataset_type, *args, **kwargs):
        config = config
        
        if config.use_features:
            self.dataset_class = stereotypeFeaturesDataset

        self.dataset = super().load(config, dataset_type, *args, **kwargs)

        return self.dataset

    def build(self, config, *args, **kwargs):
        # First, check whether manual downloads have been performed
        data_dir = get_mmf_env(key="data_dir")
        test_path = get_absolute_path(
            os.path.join(
                data_dir,
                "datasets",
                self.dataset_name,
                "defaults",
                "annotations",
                "train_stereotype.jsonl",
            )
        )
        # NOTE: This doesn't check for files, but that is a fine assumption for now
        # assert PathManager.exists(test_path), (
        #     "Hateful Memes Dataset doesn't do automatic downloads; please "
        #     + "follow instructions at https://fb.me/hm_prerequisites"
        # )
        super().build(config, *args, **kwargs)

    def update_registry_for_model(self, config):
        if hasattr(self.dataset, "text_processor") and hasattr(
            self.dataset.text_processor, "get_vocab_size"
        ):
            registry.register(
                self.dataset_name + "_text_vocab_size",
                self.dataset.text_processor.get_vocab_size(),
            )
        registry.register(self.dataset_name + "_num_final_outputs", 2)
