from pipeline.settings.models_.resNeXt import Baseline1Block
from pipeline.AEs.AE_general import MODES as M


class CLIC(Baseline1Block):
    """Settings class for ResNext variants
    Args:
        layers - number of layers of ResNeXt
        cardinality - width of each layer (in terms of number of res blocks)
    """

    def __init__(self, model_name, block_type, Cstd):
        super(CLIC, self).__init__()
        assert model_name in ["Tucodec"]
        assert block_type in ["vanilla", "NeXt"]
        self.BLOCKS = [M.S, (1, model_name, {"B": block_type, "Cstd": Cstd})]
        self.REM_FINAL = False
        self.CHANNELS = "see model def"

class GRDNBaseline(CLIC):
    def __init__(self, block_type, Cstd):
        super(CLIC, self).__init__()
        assert block_type in ["vanilla", "NeXt"]
        GRDN_kwargs = {"B": block_type, "Cstd": Cstd}

        self.BLOCKS = [M.S, (1, "GRDN", GRDN_kwargs), (7, "conv")]
        down = [[], [0, 0, 1, 1, 1, 1, 1]]
        down_z = [[], [0, 0, 1, 1, 1, 0, 0]]
        self.DOWNSAMPLE__  = (down, down, down_z)
        channels  = self.get_channels()
        channels[0] = 1
        channels[1] = 2
        self.update_channels(channels)
