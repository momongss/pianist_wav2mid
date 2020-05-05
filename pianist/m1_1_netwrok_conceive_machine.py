import wave
import mido
import numpy as np


def External_use(mid_filename, wav_filename, divide_len):             # 외부에서는 이 함수를 통해 이 모듈에 접근해야한다.

    import m2_1_conceive_preprocessing
    import m2_2_conceive_network

    conceive_wav_data, conceive_mid_data = m2_1_conceive_preprocessing.External_use(mid_filename, wav_filename,
                                                                                    divide_len)

if __name__ == "__main__":

    dir = "C:\\Users\\rkrp1\\Desktop\\Music\\practice_file\\"
    mid_filename = dir+"Grand_1.0_0.5.mid"
    wav_filename = dir+"Grand_1.0_0.5.mid"

    divide_len = 220

    External_use(mid_filename, wav_filename, divide_len)