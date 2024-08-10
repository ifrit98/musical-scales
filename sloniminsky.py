# slonimsky scales generator

from music21 import clef, stream, note, bar, metadata
import argparse
import itertools

INTERPOLATIONS = [
    "interpolation", "ultrapolation", "infrapolation",
    # "infra-interpolation", "infra-ultrapolation", "infra-inter-ultrapolation"
]

def calc_pos(pos,nl):
    newpos = pos + nl
    if(newpos >= 1.):
        newpos = 0.
    
    return newpos
    
def make_slonim(oct, division, stuff_n, start_note, polation, use_muse):

    # Show arg info
    print("oct      = %d" % oct)
    print("division = %d" % division)
    print("stuff_n  = %d" % stuff_n)

    nl=0.25 # use 16th notes
    totaloct = oct * 12
    unit = int(totaloct / division) # semitones of one unit
    print("semitones of one unit = %d" % unit)
    
    # Check whether unit is appropriate
    if unit <= stuff_n:
        print("Error: Division too much or too many notes")
        quit()
    
    stuff_notes=[x for x in range(1,unit)]
    print("stuff notes = ",stuff_notes)
    comb = [el for el in itertools.combinations(stuff_notes,stuff_n)]
    print("combination of unit elements = ",comb)
    
    tc = clef.TrebleClef()
    strm = stream.Part()
    meas = stream.Measure()
    meas.append(tc)

    #for each combination
    for el in comb:
        pos = 0.
        curpitch = start_note
        noteList = []
        
        for i in range(0,division):
            nt = note.Note(curpitch,quarterLength = nl)
            nt.color = '#ff0000'
            noteList.append(nt)
            pos = calc_pos(pos,nl)
            
            for offset in el:
                nt = {
                    'interpolation': note.Note(curpitch + offset,quarterLength = nl),
                    'infrapolation': note.Note(curpitch - offset,quarterLength = nl),
                    'ultrapolation': note.Note((curpitch + unit) + offset,quarterLength = nl),
                }[polation]                
                # nt = note.Note(curpitch + offset, quarterLength = nl)
                noteList.append(nt)
                pos = calc_pos(pos,nl)
            curpitch += unit
            
        nt = note.Note(start_note + totaloct,quarterLength = nl)
        nt.color = '#ff0000'
        noteList.append(nt)
        pos = calc_pos(pos,nl)
        
        if pos != 0.:
            noteList.append(note.Rest(quarterLength = (1. - pos)))
                
        meas.append(noteList)
        meas.rightBarline = bar.Barline('double')
        strm.append(meas)
        meas = stream.Measure()
        
    caption = 'Equal Division of ' + str(oct) + ' Octave(s) into ' + str(division) + ' Parts \n{} of '.format(polation) + str(stuff_n) + ' Note(s): Root ' + (note.Note(start_note)).name
    s = stream.Score()
    s.insert(0, metadata.Metadata())
    s.metadata.title = caption
    s.insert(0, strm)

    if use_muse:
        # s.show('musicxml')
        s.show('musicxml', app='/Applications/MuseScore 4.app/Contents/MacOS/mscore')
    else:
        s.write('lilypond', 'output.ly')
        s.show('lily.png')


def test(use_muse):
    oct = 1
    division = 3
    stuff_n = 2
    polation = 'ultrapolation'
    start_note = 55
    make_slonim(oct, division, stuff_n, start_note, polation, use_muse)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--octaves", help="Total number of octaves", type=int, default=5)
    parser.add_argument("--division", help="Number of divisions across N octaves", type=int, default=3)
    parser.add_argument("--stuff_n", help="Number of interpolation notes to 'stuff' in between divisions", type=int, default=2)
    parser.add_argument("--start_note", help="Midi note to start on", type=int, default=55)  # Start on G4 default 
    parser.add_argument("--type", help="Interpolation Type", choices=INTERPOLATIONS, default="interpolation")
    parser.add_argument("--test", action="store_true", default=False, help="Run test without requiring arguments")
    parser.add_argument("--use_muse", action="store_true", default=False, help="Use MuseScore 4 instead of Lilypond")
    args = parser.parse_args()

    if args.test is True:
        test(args.use_muse)
        quit()

    if((args.octaves * 12) % args.division):
        print ("Error: octave % division != 0")
        quit()

    make_slonim(args.octaves, args.division, args.stuff_n, args.start_note, args.type, args.use_muse)
    

