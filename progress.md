# 大谷メーター 30日運用 進捗チェックリスト

更新方法: `[ ]` を `[x]` に変えるだけ。ClaudeはこのファイルをReadして進捗を把握します。

---

## 凡例

- 担当: 👤 人間 / 🤖 Claude / 👥 両方
- リポジトリ: `[public]` `[private]` `[X]`

---

## インフラ・基盤整備（Week 1: 4/6〜4/12）

- [x] `index.html`（About）公開 👤 `[public]`
- [x] `method.html`（指標の考え方）公開 👤🤖 `[public]`
- [x] GoatCounter アカウント登録（ohtani-meter） 👤
- [x] GoatCounter 設置コード 全HTMLに追加 🤖 `[public]`
- [x] `case-study.html` 草案作成（プレースホルダー形式） 🤖 `[public]`
- [x] GoatCounter 動作確認（ページを開いてダッシュボードにアクセスが記録されるか） 👤
- [x] X 固定ポスト・プロフィールと index.html / method.html の内容整合チェック 👤 `[X]`
- [x] 全ページ共通ナビゲーション追加（About / Method リンク） 🤖 `[public]`

---

## ケーススタディ公開（Week 2: 4/16〜4/22）

- [x] ケーススタディ対象期間・数値を確認する 👤 `[private]`
  - 対象期間（年月・試合数）
  - 週次または月次の内容スコア・結果スコア
  - 4指標の具体値（チェイス率・空振り率・コンタクト率・打球速度）
  - 結果スコアが低迷した要因（BABIP・対戦投手など）
  - 回復した時期と数値
- [x] `case-study.html` プレースホルダーにデータを入力 🤖 `[public]`
- [x] `case-study.html` 内容・表現レビュー 👤 `[public]`
- [x] `case-study.html` commit / push 承認 → 実行 👤🤖 `[public]`
- [ ] ケーススタディ告知投稿（短文）を X に投稿 👤 `[X]`
- [ ] ケーススタディ深掘り投稿を X に投稿 👤 `[X]`

---

## 定期投稿の開始（Week 2〜）

- [ ] 最新スコア投稿（URL付き）を週1回のペースで開始 👤 `[X]`
  - スコアは毎試合後にローリング更新される。週1回その時点の最新スコアをURL付きで投稿する
  - UTM付きURLを使う（例: `?utm_source=twitter&utm_medium=post`）
  - URL付けるかどうかの判断: スコアのズレが大きい日・週1定期報告 → URL付き / 短い一言コメント・平常運転 → URLなし

---

## FAQ 公開（Week 3: 4/23〜4/29）

- [ ] `faq.html` 草案作成 🤖 `[public]`
- [ ] `faq.html` 内容レビュー・修正指示 👤 `[public]`
- [ ] `faq.html` commit / push 承認 → 実行 👤🤖 `[public]`
- [ ] FAQ告知・「よくある誤解」系の短文投稿 👤 `[X]`

---

## KPI確認・調整（Week 4: 4/30〜5/6）

- [ ] 主KPI確認（X流入・反応・GoatCounter） 👤 `[X]` `[GoatCounter]`
- [ ] 修正ルール判断（下記ルール参照） 👤
- [ ] 必要に応じた HTML 修正・commit / push 承認 👤🤖 `[public]`

---

## 1ヶ月振り返り（5/7〜5/8）

- [ ] KPI達成状況の整理 👤🤖
- [ ] 第2弾ケーススタディ（候補C: スランプ報道と内容スコアの乖離）対象期間確認 👤 `[private]`
- [ ] 次月計画の更新 🤖

---

## 👤 人間のタスクリスト（頻度別）

### 試合のあった日（毎回）
1. `bash scripts/ohtani_daily.sh` を実行 `[private]`
2. スコアと補足文を確認
3. 投稿するか見送るかを判断
4. 投稿する場合 → 短文をXに投稿（URLなし）`[X]`
5. セーブコマンド実行 `[private]`

### 週1回（タイミングは任意）
1. その時点の最新スコアをURL付きでXに投稿 `[X]`
   - URL: `https://carterheywood56-spec.github.io/ohtani-meter-public/index.html?utm_source=twitter&utm_medium=post`
   - スコアのズレが大きい日があればそのタイミングに合わせてもよい

### 毎週日曜（初回: 4/12）
1. URL付き投稿のリンククリック数・ブックマーク数をスプレッドシートに記録 `[X]`
2. GoatCounterダッシュボードを確認（PV・X経由数）をスプレッドシートに記録 `[GoatCounter]`
3. progress.md の計測記録メモテーブルに数値を記入
4. KPI判断（修正ルール発動の要否）

### スポット作業（Claudeから依頼があった時）
1. HTMLの内容・表現レビュー
2. commit / push の承認

---

## 試合日の日次作業（試合のあった日に毎回）

毎試合後に行う作業です。30日計画とは別に継続して発生します。

- [ ] スクリプト実行 👤 `[private]`
  ```
  bash scripts/ohtani_daily.sh
  ```
- [ ] スコア・補足文を確認して X 投稿内容を判断 👤
- [ ] X に投稿（UTM付きURLを使う） 👤 `[X]`
- [ ] セーブコマンド実行（private repo への保存） 👤 `[private]`

---

## 週次作業（毎週日曜）

チェック項目は週ごとに独立して管理する。完了したら `[ ]` → `[x]`。

---

### Week 1（4/6〜4/12）初回: 4/12

- [x] X アナリティクス確認 👤 `[X]`
  - URL付き投稿のリンククリック数（HTML流入の主指標）
  - ブックマーク・引用・「参考・納得」系の返信数
  - ※URLなし投稿のインプレッションは記録不要
- [x] GoatCounter 確認 👤 `[GoatCounter]`
  - ページ別PV（index / method / case-study）
  - Campaigns欄（UTM別流入: fixed_post / post / post_casestudy）
  - Top referrers（t.co の割合）
- [ ] 主KPI判断（修正ルール発動の要否） 👤
- [x] 計測記録メモに数値を記入 👤

**計測メモ:**
| 指標 | 値 | 備考 |
|---|---|---|
| X リンククリック | 4 | 4/10投稿（固定ポスト更新） |
| 「参考・納得」反応 | 0 | |
| GoatCounter PV | index:10 / method:4 / case-study:2 | X経由6PV |

---

### Week 2（4/13〜4/20）日曜: 4/20

- [ ] X アナリティクス確認 👤 `[X]`
- [ ] GoatCounter 確認 👤 `[GoatCounter]`
- [ ] 主KPI判断（修正ルール発動の要否） 👤
- [ ] 計測記録メモに数値を記入 👤

**計測メモ:**
| 指標 | 値 | 備考 |
|---|---|---|
| X リンククリック | | |
| 「参考・納得」反応 | | |
| GoatCounter PV | | |

---

### Week 3（4/21〜4/27）日曜: 4/27

- [ ] X アナリティクス確認 👤 `[X]`
- [ ] GoatCounter 確認 👤 `[GoatCounter]`
- [ ] 主KPI判断（修正ルール発動の要否） 👤
- [ ] 計測記録メモに数値を記入 👤

**計測メモ:**
| 指標 | 値 | 備考 |
|---|---|---|
| X リンククリック | | |
| 「参考・納得」反応 | | |
| GoatCounter PV | | |

---

### Week 4（4/28〜5/4）日曜: 5/4

- [ ] X アナリティクス確認 👤 `[X]`
- [ ] GoatCounter 確認 👤 `[GoatCounter]`
- [ ] 主KPI判断（修正ルール発動の要否） 👤
- [ ] 計測記録メモに数値を記入 👤

**計測メモ:**
| 指標 | 値 | 備考 |
|---|---|---|
| X リンククリック | | |
| 「参考・納得」反応 | | |
| GoatCounter PV | | |

---

### Week 5（5/5〜5/8）日曜: 5/11（最終振り返り前）

- [ ] X アナリティクス確認 👤 `[X]`
- [ ] GoatCounter 確認 👤 `[GoatCounter]`
- [ ] 主KPI判断（修正ルール発動の要否） 👤
- [ ] 計測記録メモに数値を記入 👤

**計測メモ:**
| 指標 | 値 | 備考 |
|---|---|---|
| X リンククリック | | |
| 「参考・納得」反応 | | |
| GoatCounter PV | | |

---

## KPI未達時の修正ルール（参照用）

| 状況 | アクション |
|---|---|
| HTMLクリックが週5未満 × 2週 | X投稿内のURL誘導文を変更する |
| 「参考・納得・保存」反応ゼロ × 2週 | 深掘り投稿（パターンE/F）を週2回に増やす |
| インプレッション低いが反応率は高い | 修正しない。信頼蓄積フェーズとして継続 |
| 投稿・HTMLの内容に矛盾 | HTML修正（承認後push）＋Xで短く告知 |

---

## UTM付与ルール（参照用）

| 投稿の種類 | UTMパラメータ |
|---|---|
| 固定ポスト | `?utm_source=twitter&utm_medium=fixed_post` |
| 通常投稿（週次スコア） | `?utm_source=twitter&utm_medium=post` |
| プロフィール欄 | `?utm_source=twitter&utm_medium=profile` |
| ケーススタディ告知 | `?utm_source=twitter&utm_medium=post_casestudy` |
