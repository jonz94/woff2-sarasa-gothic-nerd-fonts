import os
from fontTools.ttLib import TTFont


def generate_font(inputsDir, outputsDir, filename, flavor):
    print("generating... " + filename.replace("ttf", flavor))
    font = TTFont(inputsDir + filename)
    font.flavor = flavor
    font.save(outputsDir + filename.replace("ttf", flavor))
    font.close()


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE") or os.path.abspath(__file__).replace(
        "/ci/scripts/main.py", ""
    )

    inputsDir = workspace + "/ci/inputs/"
    outputsDir = workspace + "/ci/outputs/"

    for file in os.listdir(os.fsencode(inputsDir)):
        filename = os.fsdecode(file)
        if filename.endswith(".ttf"):
            generate_font(inputsDir, outputsDir, filename, "woff2")


if __name__ == "__main__":
    main()
