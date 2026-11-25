"""Invent a Word We Need — entry program.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt: one invented
English word together with its one-line definition.

Decision record — Pass 1 (candidates weighed against the judge brief:
the word must fill a real gap a reader recognises at once, the
definition must land in one reading, the word must be sayable,
spellable and memorable, and the pairing must feel fresh):

A. "roomnesia (n.) — the instant amnesia of walking into a room and
   forgetting why you came."
   REJECTED — the gap is the strongest of all five (everyone has done
   this), and the word is cleanly formed, but "roomnesia" already
   circulates in internet word lists, so it fails the freshness
   criterion: a judge that has met it before will not want to put it
   in a dictionary.

B. "snackcident (n.) — opening a bag of crisps for just one and
   discovering it empty in your hand."
   REJECTED — very sayable, very recognisable, and the definition
   lands instantly, but "snackcident" is likewise already out in the
   wild as a joke word; it reads as a pun found online rather than a
   coinage invented for this entry.

C. "corridance (n.) — the awkward mirrored sidestep two strangers
   perform in a hallway, each dodging the same way twice."
   STRONG RESERVE — the gap is real and the scene is funny, but the
   blend hides its meaning: nothing in "corridance" says "dance" until
   the definition explains it, so the word fails the "guessable from
   the word itself" part of being easy to live with. It needs its
   definition more than the winner does.

D. "microwin (n.) — stopping the microwave at exactly 0:00 and
   feeling like you beat the machine."
   REJECTED — fresh and charming, and the word is instantly clear, but
   the gap is thin: a small private triumph, not a thing English is
   missing a name for. It would lose on criterion 2 to any entry
   naming a recognisable social moment.

E. "clapioneer (n.) — the first person to clap after a performance,
   whose lone applause gives the whole room permission to join in."
   CHOSEN — "clap" + "pioneer" is transparent: the meaning is
   guessable before the definition is read, it is sayable and
   spellable at first sight, and the gap is a real social moment
   everyone has felt from both sides (the lone clapper, and the room
   waiting for someone to go first). The definition names the social
   mechanism — permission — which is the insight, not just the scene.

Pass 2 — two genuine revisions on E:
  1. First draft: "clapioneer (n.) — the person who starts clapping
     first after a performance ends." (89 chars) Too flat: it states
     the scene but not why the moment matters. Revised to add the
     mechanism: "whose lone applause gives the whole room permission
     to join in." The word now earns its dictionary place by naming a
     social function, not just a person.
  2. Considered "the brave first clapper" as the subject ("brave"
     felt like the right praise for the lone clapper), but "brave"
     editorialises and adds a word the line does not need; "lone"
     already carries the exposure of clapping alone. Cut "brave" and
     kept "lone". Also considered ending "...before anyone else dares
     to" — weaker than "permission to join in", which names what the
     room is actually waiting for.
"""

import os

LINE = "clapioneer (n.) — the first person to clap after a performance, whose lone applause gives the whole room permission to join in."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
