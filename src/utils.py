import json
import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from difflib import SequenceMatcher


def analyzeBeatsDiff(all_beatsdiff):
    diff = []
    #for beats in all_beatsdiff:
    diff = numpy.array(all_beatsdiff[0]) - numpy.array(all_beatsdiff[1])
    #x = numpy.arange(len(beats))
    #y = numpy.array(beats)
    #pylab.plot([x, y])
    # pylab.show()
    print("________________")
    print(diff)


def calculateBeatsDiff(beats):
    return list((numpy.diff(beats)))


def writeFeaturesOnAnalysisFile(out, f):
    print("Print features on files")
    name = str(out["metadata"]["tags"]["file_name"])
    length = str(out["metadata"]["audio_properties"]["length"])
    bitrate = str(out["metadata"]["audio_properties"]["bit_rate"])
    samplerate = str(out["metadata"]["audio_properties"]["sample_rate"])
    bpm = str(out["rhythm"]["bpm"])
    instrumental = str(out["highlevel"]["voice_instrumental"]["value"])
    beat_positions = out["rhythm"]["beats_position"]

    f.write(name + "," + length + "," + bitrate + "," + samplerate + "," + bpm + "," + str(
        len(beat_positions)) + "," + instrumental + "\n")

    return beat_positions

