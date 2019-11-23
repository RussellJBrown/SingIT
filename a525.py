import mir_eval



refernce_beats = mir_eval.io.load_events("Label Track Template.txt")
estimate_beats = mir_eval.io.load_events("adeleSegmenterOut.txt")

refernce_beats = mir_eval.beat.trim_beats(refernce_beats)
estimate_beats = mir_eval.beat.trim_beats(estimate_beats)

f_measure = mir_eval.beat.f_measure(refernce_beats,estimate_beats)

print(f_measure)
