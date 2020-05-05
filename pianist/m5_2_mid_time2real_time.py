def mid_time2real_time(ticks, tempo):

    import mido

    real_time = mido.tick2second(1, ticks, tempo)

    return real_time

def External_use(process_mid, ticks):

    middle_mid = []

    for p in process_mid:
        middle = []
        mid = p[1:]
        velocity = [0]*200
        note  = [0]*200
        present_time = 0
        for m in mid:
            present_time += int(m[3])
            if m[-1] == 'note_on':
                velocity[int(m[1])] = int(m[2])
                note[int(m[1])] = present_time
            elif m[-1] == 'note_off':
                new = [int(m[1]),velocity[int(m[1])],[note[int(m[1])],present_time]]
                middle.append(new)
            else:
                return "error"
        middle_mid.append(middle)

    time = mid_time2real_time(ticks, 500000)

    for middle in middle_mid:
        for m in middle:
            m[2][0] = m[2][0] * time
            m[2][1] = m[2][1] * time

    return middle_mid

if __name__ == "__main__":

    import mido
    import m5_1_D_midi

    mid_filename = "C:\\Users\\TH\\Desktop\\music composer\\midi\\way back home.mid"
    wav_filename = "C:\\Users\\TH\\Desktop\\music composer\\midi\\way back home.wav"
    mid = mido.MidiFile(mid_filename)
    pick = m5_1_D_midi.External_use(mid)

    print(pick)

    ticks = mid.ticks_per_beat

    middle_mid = External_use(pick, ticks)

    print(middle_mid)

    print(middle_mid[1][-1])