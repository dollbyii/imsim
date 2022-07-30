from imsim import Imsim

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conf_file = "C:/Users/leymar/PycharmProjects/imsim/test/imsim_conf_unitest.yml"
    imsim = Imsim(conf_file, "tesca_1")

    print(imsim.exposure_time_from_snr_mag(5, 21.5))
    print(imsim.limit_mag_from_snr_exposure_time(7, 450))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
