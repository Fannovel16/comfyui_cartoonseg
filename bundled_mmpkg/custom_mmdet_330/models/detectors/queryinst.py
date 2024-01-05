# Copyright (c) OpenMMLab. All rights reserved.
from custom_mmdet_330.registry import MODELS
from custom_mmdet_330.utils import ConfigType, OptConfigType, OptMultiConfig
from .sparse_rcnn import SparseRCNN


@MODELS.register_module()
class QueryInst(SparseRCNN):
    r"""Implementation of
    `Instances as Queries <http://arxiv.org/abs/2105.01928>`_"""

    def __init__(self,
                 backbone: ConfigType,
                 rpn_head: ConfigType,
                 roi_head: ConfigType,
                 train_cfg: ConfigType,
                 test_cfg: ConfigType,
                 neck: OptConfigType = None,
                 data_preprocessor: OptConfigType = None,
                 init_cfg: OptMultiConfig = None) -> None:
        super().__init__(
            backbone=backbone,
            neck=neck,
            rpn_head=rpn_head,
            roi_head=roi_head,
            train_cfg=train_cfg,
            test_cfg=test_cfg,
            data_preprocessor=data_preprocessor,
            init_cfg=init_cfg)
