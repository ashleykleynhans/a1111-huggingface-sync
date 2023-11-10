#!/usr/bin/env python3
import os
import argparse
from huggingface_hub import HfApi


def get_args():
    parser = argparse.ArgumentParser(
        description='Sync files from Huggingface',
    )

    parser.add_argument(
        'repo_id',
        type=str,
        help='Huggingface repo_id'
    )

    parser.add_argument(
        'sync_path',
        type=str,
        help='Local sync path (eg. /workspace/stable-diffusion-webui/models'
    )

    return parser.parse_args()


if __name__ == '__main__':
    if not os.getenv('HF_TOKEN'):
        raise Exception('HF_TOKEN environment variable is not set')

    args = get_args()
    api = HfApi()
    models = api.list_repo_files(args.repo_id)
    sync_path = args.sync_path
    files_synced = 0

    for model in models:
        folder = os.path.dirname(model)
        filename = os.path.basename(model)
        dest_path = f'{sync_path}/{model}'

        if folder and not os.path.exists(dest_path):
            print(f'Syncing {model} to {dest_path}')

            uri = api.hf_hub_download(
                repo_id=args.repo_id,
                filename=model,
                local_dir=sync_path,
                local_dir_use_symlinks=False
            )

            if uri:
                files_synced += 1

    print('Syncing complete')
    print(f'{files_synced} models were synced with Huggingface')

