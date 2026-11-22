from dataclasses import dataclass

@dataclass
class Segment:
    start: float
    end: float
    text: str

FILLERS = {'um', 'uh', 'like'}

def clean_text(text):
    words = text.split()
    kept = [w for w in words if w.strip('.,!?').lower() not in FILLERS]
    return ' '.join(kept).strip()

def build_edl(segments):
    edits = []
    for seg in segments:
        cleaned = clean_text(seg.text)
        if not cleaned:
            continue
        edits.append({
            'start': round(seg.start, 2),
            'end': round(seg.end, 2),
            'text': cleaned
        })
    return edits

def render_transcript(edits):
    return '\n'.join(
        '[{:.2f}-{:.2f}] {}'.format(e['start'], e['end'], e['text'])
        for e in edits
    )

def main():
    transcript = [
        Segment(0.0, 1.2, 'Um, welcome to the show.'),
        Segment(1.2, 2.8, 'Today we talk about, uh, AI editing.'),
        Segment(2.8, 4.0, 'Like, it removes filler words.'),
        Segment(4.0, 5.5, 'You know, text-based editing is fast.'),
    ]
    edits = build_edl(transcript)
    print('Edited transcript:')
    print(render_transcript(edits))
    print()
    print('Edit decision list:')
    for e in edits:
        print(e)

if __name__ == '__main__':
    main()
