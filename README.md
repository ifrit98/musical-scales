### Understanding Sloniminsky Patterns and Their Impetus

**Sloniminsky Patterns** originate from the work of Nicolas Slonimsky, particularly his influential book, *Thesaurus of Scales and Melodic Patterns* (1947). This book is a comprehensive catalog of scales, patterns, and sequences that push the boundaries of traditional Western music theory. These patterns are used extensively by composers and improvisers, especially in jazz and avant-garde music, to explore new harmonic and melodic possibilities.

#### **Impetus Behind Sloniminsky Patterns**
Slonimsky's work emerged from a desire to explore the full spectrum of musical possibilities, going beyond the conventional diatonic scales and traditional harmonic progressions. His patterns reflect a systematic approach to music, often based on mathematical principles, where intervals are manipulated to create complex, non-traditional sequences.

1. **Mathematical Foundations**:
   - Slonimsky's patterns often use concepts such as symmetrical divisions of the octave, interval cycles, and chromatic permutations. This mathematical rigor allows for the generation of new melodic and harmonic structures that are not bound by the traditional rules of Western tonality.
   - For example, dividing the octave symmetrically into equal parts (like dividing into three parts to create an augmented triad) leads to unique chord structures that can be expanded into melodic sequences.

2. **Expanding Harmonic Language**:
   - The traditional harmonic language is based largely on major and minor scales and their corresponding chords. Slonimsky’s patterns introduce a vast array of scales, including exotic and synthetic scales, which provide a broader harmonic palette.
   - This expanded harmonic language is particularly useful in genres like jazz, where musicians seek to create tension, release, and unexpected twists in their improvisation.

3. **Breaking Conventional Melodic Patterns**:
   - Conventional melodies are typically constructed using stepwise motion or simple leaps within a scale. Slonimsky's patterns encourage the use of wider intervals and unusual sequences, creating melodies that sound more modern and abstract.
   - Musicians and composers use these patterns to break away from predictable melodic lines, allowing for more dynamic and intricate music.

#### **Practical Application of Sloniminsky Patterns**
Musicians like John Coltrane, Frank Zappa, and countless others have applied Slonimsky’s patterns in their work to create complex and innovative music. Here's how these patterns might be used:

1. **Improvisation**:
   - Jazz musicians often use Slonimsky’s patterns to create intricate solos. By practicing these patterns, they internalize unusual intervallic relationships and scale sequences, which they can then employ spontaneously during performances.

2. **Composition**:
   - Composers may use Slonimsky’s patterns as a foundation for writing new pieces. By applying these patterns, they can generate novel melodic material or develop unique harmonic progressions that stand out from traditional compositions.

3. **Analysis and Study**:
   - Analyzing Slonimsky’s patterns offers musicians a deeper understanding of intervallic structures and scale systems. This study can inform their approach to both performance and composition, leading to a more sophisticated musical expression.

#### **Examples of Sloniminsky Patterns**
- **Chromatic Mediant Cycles**: These involve the use of mediant relationships (a third apart) with chromatic movement. For example, moving from C to E to Ab to C.
- **Diminished and Augmented Patterns**: These patterns use the symmetrical properties of diminished and augmented intervals, which divide the octave into equal parts, creating cyclical sequences.
- **Interpolation Techniques**: As mentioned earlier, interpolation and its various forms (infra, ultra, etc.) involve systematically adding notes to a sequence, leading to complex melodic lines.

In essence, Slonimsky’s patterns are tools for exploring the outer edges of musical possibility, encouraging creativity, and breaking free from conventional tonal frameworks. They offer musicians a way to delve into the unknown and to find new ways to express themselves through sound.


### Primer on Sloniminsky Interpolations

**Sloniminsky Interpolation** is a set of techniques based on the work of Russian music theorist and composer Nicolas Slonimsky. His concepts have become influential in modern music theory, particularly in jazz and avant-garde compositions, as they explore non-traditional scales and note sequences. The goal of these interpolations is to expand the possibilities of melodic and harmonic development by systematically altering note sequences.

#### 1. **Interpolation**
   - **Definition**: Interpolation involves inserting additional notes into a given melodic or harmonic sequence. This process creates new patterns by adding intermediate notes between the original pitches.
   - **Example**: If you have a sequence of C and E, interpolation might involve adding a D in between, forming a new sequence: C-D-E.

#### 2. **Infrapolation**
   - **Definition**: Infrapolation extends interpolation by focusing on adding notes below the original sequence's pitches. It is a form of downward interpolation.
   - **Example**: If the original sequence is C and E, infrapolation could add a B below the C and a D below the E, creating a sequence like B-C-D-E.

#### 3. **Ultrapolation**
   - **Definition**: Ultrapolation is the opposite of infrapolation, where notes are added above the original sequence's pitches. This technique is a form of upward interpolation.
   - **Example**: Given a sequence of C and E, ultrapolation could add a D above the C and an F above the E, resulting in a sequence like C-D-E-F.

#### 4. **Infra-Interpolation**
   - **Definition**: This technique combines infrapolation with interpolation, where notes are added both below and within the original sequence. It results in a more complex melodic or harmonic structure.
   - **Example**: Starting with a sequence of C and E, infra-interpolation might add a B below the C and a D between C and E, forming a sequence like B-C-D-E.

#### 5. **Infra-Ultrapolation**
   - **Definition**: Infra-ultrapolation involves adding notes both below and above the original sequence, creating a fuller, more expanded sound.
   - **Example**: If the original sequence is C and E, infra-ultrapolation might add a B below the C and an F above the E, leading to a sequence like B-C-E-F.

#### 6. **Infra-Inter-Ultrapolation**
   - **Definition**: This is the most complex form of interpolation, where notes are added below, within, and above the original sequence. It synthesizes all the previous methods into a single, highly detailed sequence.
   - **Example**: Starting with a sequence of C and E, infra-inter-ultrapolation might result in a sequence like B-C-D-E-F, adding notes below, within, and above the original pitches.

These techniques, derived from Slonimsky's explorations, provide a structured way to break free from conventional tonal patterns, allowing composers and improvisers to create more intricate and unpredictable musical ideas.


### Install
```bash
conda create -n music python=3.12
conda activate music
python -m pip install music21 pandas numpy


## If using lilypond

# MacOS
brew install lillypond

# Linux
wget https://gitlab.com/lilypond/lilypond/-/releases/v2.24.4/downloads/lilypond-2.24.4-linux-x86_64.tar.gz
tar -xvzf lilypond-2.24.4-linux-x86_64.tar.gz
sudo mv lilypond-2.24.4 /opt/
sudo ln -s /opt/lilypond-2.24.4/bin/lilypond /usr/local/bin/lilypond
lilypond --version # verify install


## If using MusicXML

# MacOS
brew install --cask musescore
```


### Usage
`scales.py`
```bash
python scales.py --n 4096 # Generates all major pattern permutations within a 12-tone system 
```


`sloniminsky.py`
```bash
python sloniminsky.py --octaves 3 --division 4 --stuff_n 2 --type interpolation
```