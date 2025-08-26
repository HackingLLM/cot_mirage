# CoT Mirage Hacking

## ✨ Features

- **Dual Processing Modes**: Interactive mode for real-time prompt testing and batch mode for processing multiple prompts
- **Strong Reject Judge**: Built-in evaluation system to score and analyze prompts
- **Comprehensive Logging**: Configurable logging levels with file output support
- **Standardized Input/Output**: Process prompts from CSV files and save results with detailed statistics
- **Retry Mechanisms**: Configurable retry counts for both LLM and API operations
- **Detailed Statistics**: Automatic generation of summary statistics for batch processing

## 🔧 Prerequisites

- Python 3.12
- CUDA-capable GPU
- Claude API key
- OpenAI API key


## 🔬 Experiment Reproduction

### How to Reproduce Our Results

Follow these steps to reproduce the experimental results from our paper:

1. **Setup the Repository**
   
   Follow the installation instructions in the [Installation](#-installation) section below to set up the environment.

2. **Configure Experiment Settings**
   
   Edit the `.env` file with your API keys and our experimental parameters:
   ```bash
   # API Keys
   CLAUDE_API_KEY=your_claude_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Experimental Configuration (Our Paper Settings)
   LLM_RETRY_COUNT=3
   API_RETRY_COUNT=3
   API_INTERVAL=2.0
   MAX_JUDGER_RETRIES=10  # We use 10 retries for our experiment
   ```
   
   **Important**: For our experiments, we set `MAX_JUDGER_RETRIES=10` while keeping other parameters at default values.

3. **Run the Experiment**
   
   Execute the main experiment using our harmful prompts dataset:
   ```bash
   python main.py --input-csv ./examples/jo_harmful_prompts.csv --output-csv results.csv
   ```

4. **Expected Results**
   
   The experiment will:
   - Process all prompts from the Jo harmful prompts dataset
   - Apply CoT mirage hacking with up to 10 judge retry attempts
   - Generate detailed results in `results.csv`
   - Display summary statistics upon completion

5. **Verify Results**
   
   Check the output CSV file for:
   - Individual prompt scores
   - Refusal rates
   - Success/failure statistics
   
   The summary statistics should align with the findings reported in our paper.

### Alternative Datasets

To test with other datasets, simply replace the input CSV:
```bash
# Test with custom harmful prompts
python main.py --input-csv ./examples/custom_prompts.csv --output-csv custom_results.csv
```

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cot_mirage.git
   cd cot_mirage
   ```

2. **Create a conda environment**
   ```bash
   conda create --name cot_mirage python=3.12
   conda activate cot_mirage
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and settings
   ```

## ⚙️ Configuration

Create a `.env` file by copying the example:

```bash
cp .env.example .env
```

Edit the `.env` file with the following settings:

```bash
# API Keys - NEVER commit this file to version control
CLAUDE_API_KEY=your_claude_api_key_here
# Judge API Keys
OPENAI_API_KEY=your_openai_api_key_here

# Processing Configuration
LLM_RETRY_COUNT=3
API_RETRY_COUNT=3
API_INTERVAL=2.0
MAX_JUDGER_RETRIES=5
```

## 🚀 Usage

### Interactive Mode

Run the pipeline in interactive mode for real-time CoT hacking:

```bash
python main.py --interactive
```

### Batch Mode

Process multiple prompts from a CSV file:

```bash
python main.py --input-csv prompts.csv --output-csv results.csv
```

**Input CSV Format:**
```csv
prompt
"Your first prompt here"
"Your second prompt here"
```

### Command Line Arguments

| Argument | Description                                 | Default |
|----------|---------------------------------------------|---------|
| `--device` | Device for local LLM (cuda, cpu, or mps)    | cuda |
| `--interactive` | Run in interactive mode                     | False |
| `--input-csv` | Input CSV file with prompts                 | None |
| `--output-csv` | Output CSV file for results                 | results_YYYYMMDD_HHMMSS.csv |
| `--log-level` | Logging level (DEBUG, INFO, WARNING, ERROR) | INFO |
| `--log-file` | Log file path                               | None |
| `--llm-retry-count` | Override LLM_RETRY_COUNT env var            | From config |
| `--api-retry-count` | Override API_RETRY_COUNT env var            | From config |

### Examples

**Basic batch processing:**
```bash
python main.py --input-csv harmful_prompts.csv
```

**Interactive mode with custom device:**
```bash
python main.py --interactive --device cuda:1
```

**Batch mode with debug logging:**
```bash
python main.py --input-csv prompts.csv --log-level DEBUG --log-file debug.log
```

**Override retry settings:**
```bash
python main.py --input-csv prompts.csv --llm-retry-count 5 --api-retry-count 10
```

## 📊 Output Format

The pipeline generates CSV files with the following columns:

| Column | Description |
|--------|-------------|
| prompt | Original input prompt |
| score | Evaluation score from judge |
| refused | Whether the prompt was refused (True/False) |
| error | Error message if processing failed |
| timestamp | Processing timestamp |

### Summary Statistics

After batch processing, the pipeline displays:
- Total prompts processed
- Successful evaluations
- Failed evaluations
- Number of refused prompts
- Average score


## 🐛 Troubleshooting

### Debug Mode

Enable detailed logging for troubleshooting:
```bash
python main.py --log-level DEBUG --log-file debug.log
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

**Note:** This project is for research and educational purposes. Please ensure compliance with all applicable laws and ethical guidelines when using this pipeline.
