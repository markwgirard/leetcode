import scraper

with open('readme.md', 'w') as outfile:
    for fname in ['readme_header.txt', 'mdlist.txt']:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
