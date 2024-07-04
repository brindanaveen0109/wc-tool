#! /usr/bin/env python3
import sys
import argparse

def countLines(text):
    return len(text.split())

def countWords(text):
    return len(text.split())

def countCharacter(text):
    return len(text)

def printCount(file, countLines, countWords, countCharacter):
    if countLines is not None:
        print(countLines)
    if countWords is not None:
        print(countWords)
    if countCharacter is not None:
        print(countCharacter)


def main():
    parser = argparse.ArgumentParser(description = "Count Lines, count words, count characters")
    parser.add_argument('file', type = str, help = "To process the file")
    parser.add_argument('-l', '--lines', action = 'store_true', help = "Count lines")
    parser.add_argument('-w', '--words', action = 'store_true', help = "Count Words")
    parser.add_argument('-c', '--chars', action = 'store_true', help = "Count characters")

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    lineCount  = countLines(text) if args.lines or not (args.lines or args.words or args.chars) else None
    wordCount  = countWords(text) if args.lines or not (args.lines or args.words or args.chars) else None
    charsCount  = countCharacter(text) if args.lines or not (args.lines or args.words or args.chars) else None

    printCount(args.file, lineCount, wordCount, charsCount)


if __name__ == '__main__':
    main()

