import mido
import re

def note_on_list(note):
    # [ channel, note, velocity, time ]

    num = re.findall(r'\d+', note)
    return num
def note_off_list(note):
    # [ channel, note, velocity, time ]
    num = re.findall(r'\d+', note)
    if "note_off" in note:
        num.append("note_off")
    else:
        num.append("note_on")
    return num
def track_to_list(track):

    note = []

    note_off = False

    for m in track:

        if "note_off" in str(m):
            note_off = True
            break
        else:
            continue

    if note_off:
        note.append("off_case")
        for m in track:

            if str(m)[0] != 'n':
                continue

            note.append(note_off_list(str(m)))
    else:
        note.append("on_case")
        for m in track:

            if str(m)[0] != 'n':
                continue

            note.append(note_on_list(str(m)))

    return note

def off(mid, bpm, sec):
    # new_mid : [note, velo, time]
    new_mid = []

    time = 0

    table = [False]*128

    for n in mid:

        t = int(n[3])

        if n[4] == "note_on":

            time += t / bpm * sec
            table[int(n[1])] = time

        elif n[4] == "note_off":

            new_mid.append([int(n[1]), int(n[2]), [table[int(n[1])], time + (t / bpm * sec)]])
            time += t / bpm * sec
            table[int(n[0])] = False



    return new_mid

def on(note):
    pass

def mid_processing(midi, bpm, sec):

    if midi[0] == "off_case":
        mid = off(midi[1:], bpm, sec)
    elif midi[0] == "on_case":
        mid = on(midi[1:], bpm, sec)
    else:
        mid = False
    return mid

def mid_picker(mid):              # multi 인 경우

    # 외부에서 이 모듈을 사용할 때는 이 함수를 사용하세요
    # midi 데이터에서 note data(건반 눌림 신호)만을 골라 list 로 만들어 return 한다.
    # parameter : filename : str, mid 파일 경로. 예 ) "C:\\Users\\TH\\Desktop\\music composer\\midi\\Flower_dance.mid"
    # return : note : list, len : 트랙의 개수
    #                 [channel, note, velocity, time]

    note = []

    for i in range(len(mid.tracks)):
        note.append(track_to_list(mid.tracks[i]))

    return note

def External_use(mid):

    process_mid = mid_picker(mid)

    return process_mid

if __name__ == "__main__":

    import mido

    dir = "C:\\Users\\TH\\Desktop\\Music\\music composer\\midi_mp3\\"
    mid_filename = dir + "way back home.mid"
    
    mid = mido.MidiFile(mid_filename)

    pick = External_use(mid)

    print(pick)