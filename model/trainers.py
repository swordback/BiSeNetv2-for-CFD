from ._AMRNet_trainer import AMRNetTrainer
from ._patched_UNet_trainer import PatchedUNetTrainer
from ._UNet_trainer import UNetTrainer
from ._pix2pixHD_trainer import Pix2PixHDTrainer
from ._effv2_cfd_trainer import Effv2_cfd_Trainer
from ._effv2_custom_cfd_trainer import Effv2_custom_cfd_Trainer

def get_trainer(name):
    TRAINERS = {
        'AMR_Net': AMRNetTrainer,
        'Patched_UNet': PatchedUNetTrainer,
        'UNet': UNetTrainer,
        'Pix2PixHD': Pix2PixHDTrainer,
        'Effv2_cfd': Effv2_cfd_Trainer,
        'Effv2_custom_cfd': Effv2_custom_cfd_Trainer,
    }

    for n, t in TRAINERS.items():
        # Compare as lowercase
        if n.lower() == name.lower():
            return t

    raise ValueError(f'trainer {name} is not defined')
