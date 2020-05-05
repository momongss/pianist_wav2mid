import tensorflow as tf
import numpy as np

def network(wav, mid, divide_len, songname):

    def one_note_processing(mid):

        one_mid = []
        for m in mid:
            if m == [0,0]:
                one_mid.append(0)
            elif m == [0,1]:
                one_mid.append(1)
            elif m == [1,0]:
                one_mid.append(2)
            elif m == [1,1]:
                one_mid.append(3)
            else:
                return 'multi_note_cass'

        return one_mid

    def mono_case(wav):
        mono_wav = []
        for w in wav:
            mono_wav.append(w[0])
        return  mono_wav

    mono_wav = mono_case(wav)
    one_mid = one_note_processing(mid)

    print(one_mid)

    x_train = np.array(mono_wav)
    y_train = np.array(one_mid)

    x_train = x_train / 2200.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(220,)),
        tf.keras.layers.Dense(330, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(330, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    print(x_train.shape)
    print(y_train.shape)

    def trainNsave_conceive(songname):
        file = 'C:\\Users\\TH\\Desktop\\music composer\\network\\conceive\\'+songname+'.h5'
        count = 0
        while count < 10:
            model.fit(x_train, y_train, epochs=10)
            model.save(file)
            count += 1

    trainNsave_conceive(songname)

def load_n_train(wav, mid, divide_len,songname):

    def one_note_processing(mid):

        one_mid = []
        for m in mid:
            if m == [0,0]:
                one_mid.append(0)
            elif m == [0,1]:
                one_mid.append(1)
            elif m == [1,0]:
                one_mid.append(2)
            elif m == [1,1]:
                one_mid.append(3)
            else:
                return 'multi_note_cass'

        return one_mid

    def mono_case(wav):
        mono_wav = []
        for w in wav:
            mono_wav.append(w[0])
        return  mono_wav

    mono_wav = mono_case(wav)
    one_mid = one_note_processing(mid)

    x_train = np.array(mono_wav)
    y_train = np.array(one_mid)

    x_train = x_train / 2200.0

    file = 'C:\\Users\\TH\\Desktop\\music composer\\network\\conceive\\' + songname + '.h5'

    model = tf.keras.models.load_model(file)

    def trainNsave_conceive(songname):
        file = 'C:\\Users\\TH\\Desktop\\music composer\\network\\conceive\\'+songname+'.h5'
        count = 0
        while count < 1000:
            model.fit(x_train, y_train, epochs=10)
            model.save(file)
            print('model saved')
            count += 1

    trainNsave_conceive(songname)

def External_use(conceive_wav_data, conceive_mid_data, divide_len, songname):             # 외부에서는 이 함수를 통해 이 모듈에 접근해야한다.

    network(conceive_wav_data, conceive_mid_data, divide_len, songname)
    #load_n_train(conceive_wav_data, conceive_mid_data, divide_len, songname)

if __name__ == "__main__":

    import m2_1_conceive_preprocessing

    dir = "C:\\Users\\rkrp1\\Desktop\\Music\\practice_file\\"
    songname = "Grand_1.0_0.5"
    mid_filename = dir + "Grand_1.0_0.5.mid"
    wav_filename = dir + "Grand_1.0_0.5.mid"

    divide_len = 220

    conceive_wav_data, conceive_mid_data = m2_1_conceive_preprocessing.External_use(mid_filename, wav_filename, divide_len)

    External_use(conceive_wav_data, conceive_mid_data, divide_len, songname)