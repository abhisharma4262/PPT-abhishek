"""
add_slide_link: makes a text box (and its button shape, if any) jump to another slide when clicked.
The owner uses this on the services anchor slide ("Click here for use case deep dive").

  python3 add_slide_link.py deck.pptx out.pptx --on 8 --text "use case deep dive" --to 13

--on: slide holding the text (1-based). --text: part of the text to find. --to: target slide (1-based).
Any shape whose box contains the text box's centre and is less than three times its size (a button behind it,
not the card around it) gets the same link.
"""
import argparse
from pptx import Presentation


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('out')
    ap.add_argument('--on', type=int, required=True)
    ap.add_argument('--text', required=True)
    ap.add_argument('--to', type=int, required=True)
    a = ap.parse_args()
    prs = Presentation(a.src)
    slides = list(prs.slides)
    src, target = slides[a.on - 1], slides[a.to - 1]
    hits = [sh for sh in src.shapes if sh.shape_type != 6 and sh.has_text_frame and a.text.lower() in sh.text_frame.text.lower()]
    if not hits:
        raise SystemExit(f'no shape on slide {a.on} contains "{a.text}"')
    for sh in hits:
        sh.click_action.target_slide = target
        cx, cy = sh.left + sh.width // 2, sh.top + sh.height // 2
        for other in src.shapes:
            if other is sh or other.left is None or other.shape_type == 6:
                continue
            if other.left <= cx <= other.left + other.width and other.top <= cy <= other.top + other.height \
                    and other.width < sh.width * 3 and other.height < sh.height * 3 \
                    and (not other.has_text_frame or not other.text_frame.text.strip()):
                other.click_action.target_slide = target
    prs.save(a.out)
    print(f'linked {len(hits)} shape(s) on slide {a.on} to slide {a.to}; written {a.out}')


if __name__ == '__main__':
    main()
