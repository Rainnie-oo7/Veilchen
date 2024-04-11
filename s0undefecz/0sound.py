from pydub import AudioSegment
from pydub.playback import play


def apply_effects(input_file, output_file):
    sound = AudioSegment.from_wav(input_file)

    # Reverb
    reverb_sound = sound.fade_in(100).fade_out(100).reverb()

    # Distortion
    distorted_sound = sound.overdrive(2)

    # Wet/Dry
    wet_dry_ratio = 0.7
    wet_sound = sound * wet_dry_ratio
    dry_sound = sound * (1 - wet_dry_ratio)
    wet_dry_mixed = wet_sound + dry_sound

    # Exporting
    reverb_sound.export(output_file + "_reverb.wav", format="wav")
    distorted_sound.export(output_file + "_distorted.wav", format="wav")
    wet_dry_mixed.export(output_file + "_wetdry.wav", format="wav")


# Beispielaufruf
apply_effects("input.wav", "output")