from pathlib import Path

import yaml


def repertoire_list(yaml_source: Path) -> dict[str, list[str]]:
    with open(yaml_source, "r") as fin:
        src = yaml.safe_load(fin)
    out = {}
    for _, concerts in src.items():
        for concert in concerts:
            _, details = next(iter(concert.items()))
            for music in details["repertoire"]:
                composer = music["composer"].replace("arr.", "").strip()
                if composer not in out:
                    out[composer] = []
                title = music["title"].strip()
                if title not in out[composer]:
                    out[composer] += [title]
    return out


def main():
    rep = repertoire_list(Path("knoxville_choral_society.yaml"))
    keys = sorted(rep.keys(), key=lambda k: k.split()[-1].lower())
    for key in keys:
        print(f"{key}: {', '.join(sorted([f'"{t}"' for t in rep[key]]))}")


if __name__ == "__main__":
    main()
