"""
After looking at results of 00_train_baseline:
    1) BatchNorm and dropout are both v poor in this use-case
    2) Two training runs diverged after ~ 75 epochs.

"""
from VarDACAE.settings.models.resNeXt import ResNeXt

from VarDACAE import TrainAE, ML_utils, BatchDA


import shutil

#global variables for DA and training:
EPOCHS = 250 #50 #train for 150 more epochs
SMALL_DEBUG_DOM = False #For training
calc_DA_MAE = True
num_epochs_cv = 25
LR = 0.0003
print_every = 10
test_every = 10
GPU_DEVICE = 1

exp_base = "experiments/train/01_resNeXt_2/cont/0_b"
exp_load = "experiments/train/01_resNeXt_2/0/"
model_fp = "experiments/train/01_resNeXt_2/cont/0/60.pth"
def main():
    res_layers = [3, 9, 27]
    cardinalities = [1, 8, 32]


    idx = 0
    layer = 3
    cardinality = 1
    expdir = exp_base + str(0) + "/"

    print("Layers", layer)
    print("Cardinality", cardinality)

    kwargs = {"layers": layer, "cardinality": cardinality}
    _, settings = ML_utils.load_model_and_settings_from_dir(exp_load)
    settings.AE_MODEL_FP = model_fp
    settings.GPU_DEVICE = GPU_DEVICE
    settings.export_env_vars()

    expdir = exp_base + str(idx) + "/"


    trainer = TrainAE(settings, expdir, calc_DA_MAE)
    expdir = trainer.expdir #get full path


    model = trainer.train(EPOCHS, test_every=test_every, num_epochs_cv=num_epochs_cv,
                            learning_rate = LR, print_every=print_every, small_debug=SMALL_DEBUG_DOM)




if __name__ == "__main__":
    main()

