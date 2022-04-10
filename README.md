# Scrapbox Radio Maker

共同編集しているScrapboxのページの文字列から、[VOICEVOX](https://voicevox.hiroshiba.jp/)を使いラジオのような音声を作成するプログラムです

デモ音声は[こちら](demo/scrapbox-radio-maker.mp3)
このデータの基となったScrapboxのページは[こちら](https://scrapbox.io/inajob/Scrapbox%E3%83%A9%E3%82%B8%E3%82%AA)

## 中身

- scrapbox2list.py
  - Scrapboxのテキストファイルからicon記法を基に話者を計算し中間データを作る
- make.py
  - 中間データをもとに音声ファイルを1行ずつ作成
  - VOICEVOXのAPIを呼び出している
  - 分量によるが結構時間がかかる
- mklist.sh
  - ffmpegで結合するためのファイル一覧を作成
- mkwav.sh
  - ffmpegでwavファイルを結合
  - `output.wav` というファイルが作成される
- all.sh
  - `origina.txt`というファイルからここまでのすべてのスクリプトを一気に実行する

## 動作に必要なソフトウェア

- VOICEVOXを起動しておく
- Docker(ffmpegを実行するために使用している。直接ffmpegを実行するように改造することもできそう)
- Python 3系
- シェルスクリプトが実行できる環境

- inajobはgit for windows環境で実行しています
