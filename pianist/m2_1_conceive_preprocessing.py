def External_use(mid_filename, wav_filename, divide_len):             # 외부에서는 이 함수를 통해 이 모듈에 접근해야한다.

    import mido
    from pydub import AudioSegment

    mid = mido.MidiFile(mid_filename)
    sampling_rate = AudioSegment.from_wav(wav_filename).frame_rate
    wav = wave_opener(wav_filename)

    len_wav = len(wav[0])

    import m3_1_conceive_mid_preprocessing
    import m3_2_conceive_wav_preprocessing

    conceive_wav_data = m3_2_conceive_wav_preprocessing.External_use(wav, divide_len)
    conceive_mid_data = m3_1_conceive_mid_preprocessing.External_use(mid, divide_len, sampling_rate, len_wav)

    return conceive_wav_data, conceive_mid_data

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

    mid_filename = "C:\\Users\\TH\\Desktop\\music composer\\midi\\way back home.mid"
    wav_filename = "C:\\Users\\TH\\Desktop\\music composer\\midi\\way back home.wav"

    divide_len = 220

    conceive_wav_data, conceive_mid_data = External_use(mid_filename, wav_filename, divide_len)

    print(len(conceive_wav_data))
    print(len(conceive_wav_data[0]))
    print(len(conceive_wav_data[0][0]))
    print('//////////////////////////')
    print(len(conceive_mid_data))
    print(len(conceive_mid_data[0]))


