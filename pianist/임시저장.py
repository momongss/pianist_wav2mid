import mido
import D_midi
import re

def find_tempo(track):

    # tempo setting은 첫번째 트랙에서 전담한다고 가정

    message_index = []

    for i in range(len(track)):
        m_type = type(track[i])
        if 'MetaMessage' in str(m_type):
            message_index.append(i)

    tempo = []

    for i in message_index:
        if 'set_tempo' in str(track[i]):
            t = re.findall(r'\d+', str(track[i]))
            tempo.append([i,int(t[0])])

    return tempo

def mid_time2real_time(ticks, tempo):

    real_time = mido.tick2second(1, ticks, tempo)

    return real_time

def preprocessing_machine(mid_filename):

    mid = mido.MidiFile(mid_filename)

    note = []

    tempo = find_tempo(mid.tracks[0])

    print(tempo)

    print(mid.ticks_per_beat)

    for i in range(len(tempo)):
        tempo[i][1] = mid_time2real_time(mid.ticks_per_beat, tempo[i][1])

    print(tempo)

    midi = D_midi.mid_to_list_stereo(mid_filename)

    present_time = 0

    i = 0

    for m in midi[0][1:]:
        if present_time >
            present_time += float(m[3])*tempo[i][1]

    print(total_time)

    conceive_mid_data = []
    return conceive_mid_data

if __name__ == "__main__":

    mid_filename = "C:\\Users\\TH\\Desktop\\music composer\\midi\\Monody.mid"

    mid = D_midi.mid_to_list_stereo(mid_filename)

    preprocessing_machine(mid_filename)


    # present_time = 0
    #
    # real_time_table = []
    #
    # for t in tempo:
    #     i = 0
    #     while i < t[0]:
    #         if 'note_on' in str(mid.tracks[0][i]):
    #             integer = re.findall(r'\d+', str(mid.tracks[0][i]))
    #             present_time += float(integer[-1])*t[1]
    #         elif 'note_off' in str(mid.tracks[0][i]):
    #             integer = re.findall(r'\d+', str(mid.tracks[0][i]))
    #             present_time += float(integer[-1])*t[1]
    #         i+=1
    #     real_time_table.append(present_time)
    #
    # print(real_time_table)