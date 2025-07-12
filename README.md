# 🧠 Reinforcement Learning Foundation Exercises

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-%3E%3D3.8-blue.svg)](https://www.python.org/downloads/)

A modular, production-grade curriculum for mastering foundational and intermediate concepts in Reinforcement Learning (RL). Designed for ML engineers, researchers, and students seeking rigorous, hands-on experience with agent-environment interaction cycles, value estimation, and scalable RL architectures.

---

## 🔑 Key Features

- **Concept-Driven Exercises:** Structured progression from agent-environment loops to advanced RL topics
- **Scaffolded Code Templates:** Partial implementations with guided instructions and extensible design
- **Timestep Abstraction:** Core focus on the agent-environment interaction cycle
- **Experimentation-Ready:** Easily extensible for research, benchmarking, or integration with external environments
- **Professional Standards:** Modular code, clear documentation, and reproducible results

---

## 🏗️ Architecture Overview

```text
rl_foundation_exercises/
├── README.md                      # Project documentation
├── requirements.txt               # Dependency specifications
├── timestep_loop.py               # Core abstraction for timestep-based control flow
├── part1_foundations/             # Exercises covering foundational concepts
│   └── exercise_01_state_loop.py  # Initial exercise on state transitions
└── part2_intermediate/            # Intermediate-level modules (Coming Soon)
```

---

## ⚡ Installation

### Prerequisites
- Python >= 3.8
- Recommended: [Poetry](https://python-poetry.org/) or [pipenv](https://pipenv.pypa.io/en/latest/) for environment management
- Familiarity with RL terminology (states, actions, rewards)

### Setup

```bash
# Clone the repository
git clone https://github.com/kira-ml/rl_foundation_exercises.git
cd rl_foundation_exercises

# Create and activate a virtual environment
python -m venv rl_env
# Windows
rl_env\Scripts\activate
# macOS/Linux
source rl_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage Example

Run a foundational RL exercise:

```bash
cd part1_foundations
python exercise_01_state_loop.py
```

Modify scripts to:
- Implement custom agents
- Adjust hyperparameters
- Integrate with external environments (e.g., `gymnasium`)

---

## 📂 Dataset Description

*No external datasets are required for foundational exercises. All environments are minimal and self-contained. For advanced modules, integration with OpenAI Gymnasium or custom datasets is supported.*

---

## 🏋️‍♂️ Training & Evaluation

- Each exercise is designed for stepwise implementation and validation.
- Evaluation metrics include episode reward, episode length, and policy performance.
- For benchmarking, extend modules to compare Monte Carlo, TD, and other RL methods.

---

## 📊 Results & Benchmarks

*This repository is educational and not optimized for SOTA performance. Future modules will include:*
- Empirical comparisons (e.g., Monte Carlo vs. TD learning)
- Training curves and episode rewards
- Policy evaluation metrics

---

## 🤝 Contribution Guidelines

We welcome contributions from the ML community:

- Submit issues for bugs, enhancements, or documentation improvements
- Add new exercises, environments, or RL algorithms
- Share experimental findings or alternative solutions

**How to contribute:**
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes with clear messages
4. Submit a pull request with a detailed explanation

Please follow modular design principles and include relevant tests/documentation.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📚 References & Citations

- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*
- OpenAI Gymnasium Documentation: [https://www.gymlibrary.dev](https://www.gymlibrary.dev)
- David Silver's RL Course: [https://www.davidsilver.uk/teaching/](https://www.davidsilver.uk/teaching/)
- [DeepMind RL Research](https://www.deepmind.com/research)

---

## 💬 Contact

For inquiries, ideas, or collaborations, please open a GitHub issue or start a discussion thread.

---

*If you use this repository for research or teaching, please cite appropriately and consider sharing your results or improvements with the community.*

