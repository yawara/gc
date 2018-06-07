# Homebrew formula to install OpenJTalk  

## Tap it:

```
brew tap yawarwa/open-jtalk
```

## Install OpenJTalk:

```
brew install open-jtalk
```

## How to use:

Text from standard input

```
open_jtalk -x $(brew --prefix open-jtalk)/dic -m $(brew --prefix open-jtalk)/voice/mei/mei_normal.htsvoice  -ow out.wav
```

Text from a file whose name is sample.txt

```
open_jtalk -x $(brew --prefix open-jtalk)/dic -m $(brew --prefix open-jtalk)/voice/mei/mei_normal.htsvoice  -ow out.wav sample.txt
```

to play output wave file in CLI

```
afplay out.wav
```
