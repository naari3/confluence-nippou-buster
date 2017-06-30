# confluence-nippou-buster

コンフルにmdで書かれた日報を提出するスクリプト

## usage

```bash
push markdown to stdout command here | python main.py [strftime format] [space] [parent page name]
```

example

```bash
cat nippou_2017_0630.md | python main.py 日報_naari_%Y%m%d 日報開発チーム 日報_naari
```
