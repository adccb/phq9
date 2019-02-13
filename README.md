# phq9

if you take the phq9 with any amount of regularity, you might like to use this cli one instead of a paper copy.

## requirements

- python3 (`$ brew install python3`)

## usage

i usually symlink into `/usr/local/bin/`; to do so, run `sudo ln -s /absolute/path/to/phq9 /usr/local/bin/phq9`. you'll also want to `pip3 install -r requirements.txt`.

when you have a `phq9` executable in your `$PATH`, you can run the following commands:

`$ phq9 take` to take the survey

`$ phq9 list` to list the surveys you've taken, and their results

## data storage

everything is stored locally on your machine at `~/.phq9`. don't damage or delete that folder, because we have no other way to store your data.

have fun, be safe, try to get a low score if you can
