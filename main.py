import cProfile
from Configuration import Configuration
from BinPacker import BinPacker
import TestCases
import random
from util import plot_configuration, initialize_plot

if __name__ == "__main__":

    # Parameters
    rects = TestCases.cat1_p1
    plotting = False
    container_size = (20,20)
    # random.shuffle(rects)
    # print(rects)
    C = Configuration(size=container_size, unpacked_rects=rects[:], enable_plotting=plotting)
    packer = BinPacker(C)

    # For profiling     
    cProfile.run('C = packer.PackConfiguration(C)', sort="time")
    C = packer.PackConfiguration(C)
    if not plotting:
        initialize_plot(C, rects, 5)
        plot_configuration(C, last_frame=True)
    


