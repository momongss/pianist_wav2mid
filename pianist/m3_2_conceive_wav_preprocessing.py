def External_use(wav, divide_len):            # 외부에서는 이 함수를 통해 이 모듈에 접근해야한다.

    index = 0

    wav1 = wav[0]
    wav2 = wav[1]

    conceive_wav1 = []
    for i in range(int(len(wav1) / divide_len)):
        conceive_wav1.append(wav1[index:index+divide_len])
        index += divide_len

    conceive_wav2 = []
    for i in range(int(len(wav2) / divide_len)):
        conceive_wav2.append(wav2[index:index+divide_len])
        index += divide_len

    conceive_wav_data = []

    for i in range(len(conceive_wav1)):
        temp = [conceive_wav1[i],conceive_wav2[i]]
        conceive_wav_data.append(temp)

    return conceive_wav_data


def wave_opener(file):

    import wave
    import numpy as np

    with wave.open(file, 'r') as wav_file:
        # Extract Raw Audio from Wav File
        signal = wav_file.readframes(-1)
        signal = np.fromstring(signal, 'Int16')

        # Split the data into channels
        channels = [[] for channel in range(wav_file.getnchannels())]
        for index, datum in enumerate(signal):
            channels[index % len(channels)].append(datum)

        return channels

if __name__ == "__main__":

    # dir = "C:\\Users\\TH\\Desktop\\Music\\music composer\\midi_mp3\\"
    dir = "C:\\Users\\rkrp1\\Desktop\\전공\\이번 학기\\1. 전자 HW설계\\Term Project\\소리\\"

    # mid_filename = dir + "sample.mid"
    wav_filename = dir + "siren.wav"

    wav = wave_opener(wav_filename)

    print(len(wav))
    print(len(wav[0]))
    print(wav[0][:200])

    wav2 = []
    for i in range(14700):
        if i%10==0:
            wav2.append(wav[0][i])

    print(wav2)
    print(len(wav2))

    sampling_rate = 44100
    frame_time = 0.01  # 1개 프레임의 시간
    divide_len = int(sampling_rate * frame_time)

    conceive_wav_data = External_use(wav, divide_len)

    # print(len(conceive_wav_data))
    # print(len(conceive_wav_data[0]))
    # print(len(conceive_wav_data[0][0]))