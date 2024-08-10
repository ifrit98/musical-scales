\version "2.24" 
\include "lilypond-book-preamble.ly"
    
color = #(define-music-function (parser location color) (string?) #{
        \once \override NoteHead #'color = #(x11-color color)
        \once \override Stem #'color = #(x11-color color)
        \once \override Rest #'color = #(x11-color color)
        \once \override Beam #'color = #(x11-color color)
     #})
    
\header { 
 title = "Equal Division of 2 Octave(s) into 4 Parts 
interpolation of 2 Note(s): Root C"   
  
  } 
 
\score  { 
 
      << \new Staff  = aawfxedfyw { \clef "treble" 
             c' 16  
             cis' 16  
             d' 16  
             fis' 16  
             g' 16  
             gis' 16  
             c,,, 16  
             cis,,, 16  
             d,,, 16  
             fis,,, 16  
             g,,, 16  
             gis,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             cis' 16  
             ees' 16  
             fis' 16  
             g' 16  
             a' 16  
             c,,, 16  
             cis,,, 16  
             ees,,, 16  
             fis,,, 16  
             g,,, 16  
             a,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             cis' 16  
             e' 16  
             fis' 16  
             g' 16  
             bes' 16  
             c,,, 16  
             cis,,, 16  
             e,,, 16  
             fis,,, 16  
             g,,, 16  
             bes,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             cis' 16  
             f' 16  
             fis' 16  
             g' 16  
             b' 16  
             c,,, 16  
             cis,,, 16  
             f,,, 16  
             fis,,, 16  
             g,,, 16  
             b,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             d' 16  
             ees' 16  
             fis' 16  
             gis' 16  
             a' 16  
             c,,, 16  
             d,,, 16  
             ees,,, 16  
             fis,,, 16  
             gis,,, 16  
             a,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             d' 16  
             e' 16  
             fis' 16  
             gis' 16  
             bes' 16  
             c,,, 16  
             d,,, 16  
             e,,, 16  
             fis,,, 16  
             gis,,, 16  
             bes,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             d' 16  
             f' 16  
             fis' 16  
             gis' 16  
             b' 16  
             c,,, 16  
             d,,, 16  
             f,,, 16  
             fis,,, 16  
             gis,,, 16  
             b,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             ees' 16  
             e' 16  
             fis' 16  
             a' 16  
             bes' 16  
             c,,, 16  
             ees,,, 16  
             e,,, 16  
             fis,,, 16  
             a,,, 16  
             bes,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             ees' 16  
             f' 16  
             fis' 16  
             a' 16  
             b' 16  
             c,,, 16  
             ees,,, 16  
             f,,, 16  
             fis,,, 16  
             a,,, 16  
             b,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
             c' 16  
             e' 16  
             f' 16  
             fis' 16  
             bes' 16  
             b' 16  
             c,,, 16  
             e,,, 16  
             f,,, 16  
             fis,,, 16  
             bes,,, 16  
             b,,, 16  
             c,, 16  
             r 8.  
             \bar "||"  %{ end measure 0 %} 
              } 
            
 
        >>
      
  } 
 
\paper { }
\layout {
  \context {
    \RemoveEmptyStaffContext
    \override VerticalAxisGroup #'remove-first = ##t
  }
 }
 
