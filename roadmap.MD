# ML Trading Strategy Research Project — Full Roadmap

**Duration:** 16 weeks (~4 months)
**Daily commitment:** ~1.5 hours during Block 3 of your bootcamp schedule, 6 days/week
**Total estimated effort:** ~140 hours

---

## Project Thesis

Investigate whether ML-driven strategies can outperform a passive buy-and-hold benchmark on equities and crypto, using rigorous out-of-sample evaluation that accounts for transaction costs, slippage, and look-ahead bias.

**The point is not to make money.** The point is to learn the full ML pipeline (data engineering → modelling → evaluation → deployment → communication) with the intellectual honesty that distinguishes real research from CV theatre. An honest negative result ("ML did not beat buy-and-hold after costs") is a far stronger output than a fake 95% accuracy that secretly leaks data — and recruiters who matter can tell the difference instantly.

---

## What Success Looks Like at Week 16

A GitHub repository containing:

- A proper Python package structure with documented modules
- A custom backtesting engine with realistic transaction costs and slippage
- 6+ model implementations spanning classical ML, deep learning, and NLP-augmented approaches
- Walk-forward evaluation harness with proper time-series cross-validation
- A live deployed demo (Streamlit Cloud or HuggingFace Spaces) linked from the README
- A polished README with motivation, methods, results, equity curves, and lessons learned
- A 1,500–2,000 word blog post / Medium article walking through the project
- An ablation table comparing every approach honestly

This puts you in roughly the top 5% of junior ML portfolio projects.

---

## Phase 1 — Foundation & Honest Baseline (Weeks 1–3)

**Goal:** Build the infrastructure and establish a baseline. By the end of this phase you will be confronted with the brutal reality of financial ML — that's a feature, not a bug.

**Course alignment:** ML Specialization Course 1 (Supervised Learning)

### Week 1 — Repo setup, data pipeline, EDA

Tasks:

- Initialize the GitHub repo. Suggested structure: `data/`, `models/`, `backtest/`, `notebooks/`, `tests/`, plus `README.md`, `requirements.txt`, `.gitignore`.
- Pick a universe of 5–10 liquid tickers: e.g., SPY, QQQ, AAPL, MSFT, NVDA, BTC-USD, ETH-USD.
- Pull 10+ years of daily OHLCV data with `yfinance`. Save as parquet files locally.
- Compute returns, log returns, rolling volatility (20-day, 60-day).
- Plot: price series, return distributions, autocorrelation of returns and squared returns.

Libraries: `yfinance`, `pandas`, `numpy`, `matplotlib`, `seaborn`.

Deliverable: a `notebooks/01_eda.ipynb` with findings, plus a `data/load.py` module.

### Week 2 — Backtesting engine

Tasks:

- Write a simple event-driven backtester from scratch. Don't use a library — building it teaches you the mechanics.
- Implement: position tracking, equity curve, transaction costs (start with 5 basis points per trade), simple slippage assumption.
- Implement the core performance metrics: total return, annualized return, Sharpe ratio, max drawdown, Calmar ratio.
- Sanity-check by running buy-and-hold through it.

Libraries: pure `pandas` and `numpy`. No `backtrader` or `vectorbt` yet — write it yourself.

Deliverable: a `backtest/engine.py` module with tests.

### Week 3 — First baselines

Tasks:

- Implement non-ML baselines: buy-and-hold, simple moving average crossover (20/50), 12-1 momentum.
- Implement first ML baseline: logistic regression predicting next-day direction.
- Features: lagged returns (1, 5, 10 days), 20-day rolling volatility, 14-day RSI.
- Critical: use a time-based train/test split. **Never** random k-fold on time-series data.
- Compare the ML model honestly against the non-ML baselines using the same backtester.

Libraries: `scikit-learn`.

Deliverable: First "trading model" + a comparison table. Probably the ML model will not beat buy-and-hold. Write down why honestly.

### Self-study for Phase 1

- Financial metrics: Sharpe, Sortino, max drawdown, Calmar.
- Why time-series cross-validation is fundamentally different from random k-fold.
- Basic technical indicators (RSI, MACD, Bollinger bands).

### Reading for Phase 1

- "Advances in Financial Machine Learning" by Marcos López de Prado, chapters 1–3 (or summarised blog posts if the book is too heavy).
- Ernie Chan's "Quantitative Trading", chapters 1–3.

---

## Phase 2 — Classical ML Expansion (Weeks 4–7)

**Goal:** Try more models, learn rigorous evaluation, and develop feature engineering intuition.

**Course alignment:** Finishing Course 1, starting Course 2.

### Week 4 — Feature engineering

Tasks:

- Expand feature set: RSI, MACD, Bollinger band positions, volume ratios, calendar dummies (day of week, month), volatility regime indicator.
- **Lookahead bias audit:** for every feature, verify it is computable using only information available at decision time. Document this in a `FEATURES.md` file.
- Normalize/standardize features properly — fit scaler on training data only, apply to test.

Deliverable: documented feature pipeline.

### Week 5 — Tree-based models

Tasks:

- Random Forest classifier on next-day direction.
- XGBoost classifier (this is the workhorse of practical ML).
- LightGBM as a third comparison.
- Walk-forward validation: rolling 3-year train window, 6-month test window, advancing through history.
- Handle class imbalance via class weights.
- SHAP analysis for feature importance.

Libraries: `xgboost`, `lightgbm`, `shap`.

Deliverable: notebook comparing tree models against logistic regression.

### Week 6 — Robust evaluation

Tasks:

- Multi-metric evaluation harness: accuracy, F1, AUC, plus *strategy* metrics (Sharpe net of costs, max drawdown).
- Statistical significance testing (bootstrapped confidence intervals on Sharpe).
- Test on multiple assets — does the model generalize across tickers?
- Build a results dashboard (matplotlib or plotly) showing equity curves side by side.

Deliverable: `evaluation/harness.py`, plus a results notebook.

### Week 7 — Consolidation and writeup

Tasks:

- Hyperparameter tuning via expanding-window cross-validation (carefully — beware overfitting on time series).
- Pick the best classical approach as your locked-in "classical baseline" for later comparisons.
- Write a Phase 2 section in the repo: what worked, what didn't, what surprised you.

Deliverable: `docs/phase2_findings.md` and a clean classical baseline.

### Self-study for Phase 2

- Walk-forward and combinatorial purged cross-validation.
- XGBoost mechanics (gradient boosting, regularization).
- SHAP values — what they are and aren't.
- Bootstrapping for confidence intervals.

### Reading for Phase 2

- López de Prado chapters 4–7 (sample weights, cross-validation in finance, feature importance).
- XGBoost paper (Chen & Guestrin, 2016) — at least skim it.

---

## Phase 3 — Deep Learning for Time Series (Weeks 8–10)

**Goal:** Apply neural networks to the same problem and learn PyTorch.

**Course alignment:** ML Specialization Course 2 (Advanced Learning Algorithms). The course uses TensorFlow; you'll learn TF concepts there but build the project in PyTorch.

### Week 8 — PyTorch fundamentals + simple MLP

Tasks:

- Work through the official PyTorch 60-min blitz.
- Build a simple MLP for next-day direction prediction.
- Train/eval/test loop written cleanly.
- Compare against XGBoost baseline on the same features.

Libraries: `torch`.

Deliverable: PyTorch baseline notebook.

### Week 9 — LSTMs for sequence modelling

Tasks:

- Implement an LSTM model that takes the past N days of features as a sequence.
- Sequence length experiments: 5, 20, 60 days. Document the trade-offs.
- Proper rolling-window training to avoid look-ahead.
- Consider using attention as a stretch.

Deliverable: LSTM module + analysis notebook.

### Week 10 — 1D CNNs + comprehensive comparison

Tasks:

- 1D CNN — often competitive with LSTM, faster to train, simpler.
- Comprehensive comparison table: logistic regression → XGBoost → MLP → LSTM → CNN.
- Honest assessment: where does deep learning help? Where does it not?
- Plot training/validation curves to show overfitting behavior.

Deliverable: Phase 3 writeup section.

### Self-study for Phase 3

- PyTorch fundamentals (tensors, autograd, modules, optimizers, schedulers).
- RNN/LSTM/GRU mechanics — understand vanishing gradients and what LSTMs solve.
- 1D convolutions for time series.

### Reading for Phase 3

- "The Unreasonable Effectiveness of RNNs" (Karpathy blog post).
- PyTorch official tutorials.
- "Attention Is All You Need" (skim — relevant for Phase 4).

---

## Phase 4 — NLP & Alternative Data (Weeks 11–13)

**Goal:** Incorporate textual signals, learn modern NLP / transformer ecosystem. This is where the project becomes genuinely differentiated.

**Course alignment:** Course 3 (Unsupervised, Recommenders, RL) — mostly self-study from here.

### Week 11 — Text data collection

Tasks:

- Scrape financial news headlines for your tickers. Sources: Yahoo Finance, Finviz, free tier of NewsAPI.
- Optional: pull Reddit posts from r/stocks, r/investing using PRAW.
- Build a dated headline dataset, properly timestamped so it aligns with price data without look-ahead.

Libraries: `requests`, `beautifulsoup4`, `praw`.

Deliverable: text dataset with proper timestamps.

### Week 12 — Sentiment extraction with FinBERT

Tasks:

- Use the pretrained FinBERT model from HuggingFace to score sentiment of each headline.
- Aggregate to daily sentiment per ticker (mean, count, dispersion).
- EDA: does sentiment correlate with same-day or next-day returns? Lag analysis.
- Try sentence-transformers as an alternative for richer embeddings.

Libraries: `transformers`, `sentence-transformers`.

Deliverable: sentiment time series + correlation analysis.

### Week 13 — Combined model

Tasks:

- Add sentiment features to your best Phase 2 / Phase 3 model.
- Run the full walk-forward evaluation again with the augmented features.
- Be honest: does the NLP signal actually help? Many studies suggest it does very weakly or not at all once you account for costs.
- Document findings, even if negative.

Deliverable: NLP-augmented model + Phase 4 writeup.

### Self-study for Phase 4

- HuggingFace `transformers` library basics.
- FinBERT — what it is and how it was trained.
- Sentence embeddings vs token-level sentiment scores.
- Web scraping ethics and rate-limiting.

### Reading for Phase 4

- HuggingFace NLP course (chapters 1–2 are sufficient).
- FinBERT paper (Araci, 2019).
- "Sentence-BERT" paper (Reimers & Gurevych, 2019).

---

## Phase 5 — Polish, Deploy, Write (Weeks 14–16)

**Goal:** Make it shippable. Half the value of the project is in this phase.

### Week 14 — Streamlit dashboard + deployment

Tasks:

- Build an interactive Streamlit app:
  - Pick a ticker
  - View model predictions over a historical window
  - Compare equity curves of all approaches
  - Show key metrics (Sharpe, max drawdown, hit rate)
- Deploy to Streamlit Community Cloud or HuggingFace Spaces (both free).
- Add the demo link prominently to the README.

Libraries: `streamlit`, `plotly`.

Deliverable: live demo link.

### Week 15 — README + blog post

Tasks:

- Polish the README. It should answer: What is this? Why did I build it? What did I learn? How do I run it? What were the results? Include charts and tables inline.
- Write a 1,500–2,000 word blog post (Medium, Substack, or a personal site). Walk through the methodology, the results, and what surprised you. Be honest about negative results.
- Make all charts publication-quality. Consistent style, clear labels, proper legends.
- Add a `LESSONS_LEARNED.md` documenting mistakes and what you'd do differently.

Deliverable: polished repo + published blog post.

### Week 16 — Stretch goals (pick one)

Option A — Reinforcement learning agent:

- Implement a simple Deep Q-Network agent that learns to size positions.
- Use `stable-baselines3` or hand-roll a minimal DQN.
- Compare against your supervised baselines.

Option B — Additional rigor:

- Run the full evaluation on a second asset class (e.g., crypto if you did equities).
- Add purged k-fold cross-validation à la López de Prado.
- Statistical tests for strategy comparison (deflated Sharpe ratio).

Option C — Presentation polish:

- Record a 5-minute video walkthrough of the project.
- Create animated equity curve comparisons.
- Polish the blog post into a longer Medium feature.

Deliverable: whichever stretch you picked.

---

## Quality Standards — What "Good" Looks Like

Hold yourself to these bars throughout:

- **Reproducibility:** anyone should be able to clone the repo, `pip install -r requirements.txt`, and reproduce your headline numbers. Pin your dependencies. Set random seeds.
- **Documentation:** every module has a docstring. Every notebook has prose explaining what you're doing and why.
- **Code style:** use `black` for formatting, `ruff` for linting. Set up `pre-commit` hooks once and forget about it.
- **Version control:** commit often, write meaningful commit messages, use feature branches for big changes.
- **Tests:** at least the backtesting engine should have unit tests. If your backtester is wrong, every result is wrong.
- **Honesty:** if a model performs badly, say so. If you found a bug that invalidated earlier results, document it.

---

## Common Pitfalls — Things That Sink Student Projects

- **Lookahead bias.** Using information that wouldn't have been available at decision time. The single most common error in finance ML. Check every feature.
- **Survivorship bias.** If you select tickers based on which companies still exist today, your backtest is contaminated.
- **Random k-fold CV on time series.** It leaks future information into training. Always use walk-forward or purged CV.
- **Ignoring transaction costs.** A strategy that "wins" before costs and "loses" after is normal. Always report net-of-costs Sharpe.
- **Overfitting on hyperparameters.** If you tune 50 hyperparameters and report the best result, you've overfit your evaluation procedure, not just your model.
- **Reporting only the best result.** Always report the full ablation, including failures. This is what distinguishes science from hype.
- **Implementing libraries instead of using them.** Don't waste a week building your own gradient boosting library. Build the *backtester* yourself because mechanics matter; use XGBoost off the shelf.

---

## Master Reading List (in priority order)

Books and key papers, ordered by when they become useful:

1. López de Prado, *Advances in Financial Machine Learning* — the canonical text for rigorous ML in finance. Chapters 1–7 are most relevant.
2. Ernie Chan, *Quantitative Trading* — practical, accessible, less mathy.
3. Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks" — blog post.
4. Chen & Guestrin, *XGBoost: A Scalable Tree Boosting System* (2016).
5. Araci, *FinBERT: Financial Sentiment Analysis with Pre-trained Language Models* (2019).
6. Reimers & Gurevych, *Sentence-BERT* (2019).
7. Vaswani et al., *Attention Is All You Need* (2017) — for general transformer context.
8. Bailey & López de Prado, *The Deflated Sharpe Ratio* — for honest evaluation.

---

## Recommended Stack

- **Language:** Python 3.11+
- **Data:** `pandas`, `numpy`, `yfinance`, `pyarrow` (for parquet)
- **Classical ML:** `scikit-learn`, `xgboost`, `lightgbm`
- **Deep learning:** `torch`
- **NLP:** `transformers`, `sentence-transformers`
- **Visualization:** `matplotlib`, `plotly`, `seaborn`
- **Backtesting:** roll your own first, optionally compare to `vectorbt` later
- **Deployment:** `streamlit`, deployed on HuggingFace Spaces or Streamlit Cloud
- **Dev tooling:** `black`, `ruff`, `pytest`, `pre-commit`, `uv` or `poetry` for env management
- **Compute:** Google Colab free tier for any GPU-needing work. CPU is fine for most of this project.

---

## Weekly Check-in Ritual

Every Sunday (your rest day from the bootcamp), spend 20 minutes:

1. Review what you completed this week. Update the relevant phase doc in the repo.
2. Identify what's blocking you. If you've been stuck on the same problem for 3+ days, ask for help (forums, Reddit, Discord) — don't grind in silence.
3. Look at next week's tasks and adjust if needed. The roadmap is a guide, not a contract.
4. Commit and push a "Week N summary" markdown file. Future you (and recruiters reading your commit history) will appreciate it.

---

## Final Thought

The best CV/GitHub projects are not the ones with the most impressive-sounding tech stack. They are the ones where it's evident the author *thought hard*. Rigorous evaluation, honest results, and clear writing are rarer and more valuable than another fine-tuned transformer.

By Week 16 you will have built something that demonstrates: data engineering, classical ML, deep learning, NLP, deployment, scientific rigor, and technical writing. That's the full ML practitioner skill set in one repo.

Good luck. Ship it.
