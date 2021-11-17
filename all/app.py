from process import preprocess
x = preprocess()
skin_gsr, gsr_hrv, phy = x.wrapper_function('P0720')
print(skin_gsr.shape, gsr_hrv.shape, phy.shape)