# A1111 Huggingface Sync

Synchronises A1111 models with a Huggingface repository.

## Installation

```bash
git clone https://github.com/ashleykleynhans/a1111-huggingface-sync.git
cd a1111-huggingface-sync
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Upload a model to Huggingface

```bash
export HF_TOKEN="hf_xxxxxxxxxxxxxxxxxxxxxxxx"
python3 upload.py model.safetensors Stable-diffusion/model.safetensors ashleykleynhans/a1111-models
```

## Sync models from Huggingface

```bash
export HF_HUB_CACHE="/workspace/.cache/huggingface/hub"
export HF_TOKEN="hf_xxxxxxxxxxxxxxxxxxxxxxxx"
python3 sync.py ashleykleynhans/a1111-models /workspace/stable-diffusion-webui/models
```
