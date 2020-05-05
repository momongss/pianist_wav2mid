import fluidsynth

fluidsynth()



sound_font = 'C:\\Users\\TH\\Desktop\\music composer\\trainwhistlesv1.0\\trainwhistlesv1.0\\whistle.sf2'

FluidSynth(sound_font)

fs = FluidSynth()

mid_filename = 'C:\\Users\\TH\\Desktop\\music composer\\midi\\way back home.mid'
flac_filename = 'C:\\Users\\TH\\Desktop\\music composer\\wav\\test.wav'
# FLAC, a lossless codec, is supported as well (and recommended to be used)
fs.midi_to_audio(mid_filename, flac_filename)