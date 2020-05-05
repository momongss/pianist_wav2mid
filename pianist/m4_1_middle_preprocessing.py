def External_use(mid, ticks):

    import m5_1_D_midi
    import m5_2_mid_time2real_time

    process_mid = m5_1_D_midi.External_use(mid)
    middle_mid = m5_2_mid_time2real_time.External_use(process_mid, ticks)

    return middle_mid

if __name__ == "__main__":

    dir = "C:\\Users\\rkrp1\\Desktop\\Music\\practice_file\\"
    mid_filename = dir + "Grand_1.0_0.5.mid"
    wav_filename = dir + "Grand_1.0_0.5.mid"

    import mido
    mid = mido.MidiFile(mid_filename)
    middle_mid = External_use(mid, mid.ticks_per_beat)
    print(middle_mid)
    print(middle_mid[0][0])