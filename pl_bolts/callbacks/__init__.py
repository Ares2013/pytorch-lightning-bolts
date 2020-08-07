"""
Collection of PyTorchLightning callbacks
"""
from pl_bolts.callbacks.printing import PrintTableMetricsCallback
from pl_bolts.callbacks.variational import LatentDimInterpolator
from pl_bolts.callbacks.self_supervised import BYOLMAWeightUpdate, SSLOnlineEvaluatorCallback
