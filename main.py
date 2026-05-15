from pathlib import Path

import yaml


def repertoire_list(yaml_source: Path) -> dict[str, list[str]]:
    with open(yaml_source, "r") as fin:
        src = yaml.safe_load(fin)
    out = {}
    for _, concerts in src.items():
        for concert in concerts:
            _, details = next(iter(concert.items()))
            if "repertoire" not in details:
                continue
            for music in details["repertoire"]:
                composer = music["composer"].replace("arr.", "").strip()
                if composer not in out:
                    out[composer] = []
                title = music["title"].strip()
                if title not in out[composer]:
                    out[composer] += [title]
    return out


def main():
    for yml in Path(".").glob("*.yaml"):
        if yml.name.startswith("."):
            continue
        print(f"--- {' '.join(t.capitalize() for t in yml.stem.split('_'))} ---")
        rep = repertoire_list(yml)
        keys = sorted(rep.keys(), key=lambda k: k.split()[-1].lower())
        for key in keys:
            print(f"{key}: {', '.join(sorted([f'"{t}"' for t in rep[key]]))}")


"""
2022-2023
10/20/2022 - CONCERT: St. John's Episcopal Cathedral - 7:30p.m.



"""

if __name__ == "__main__":
    main()
